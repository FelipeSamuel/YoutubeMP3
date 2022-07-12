from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QTextCursor, QPixmap
from views.ui_main import Ui_MainWindow
import os
import re
from pytube import YouTube
from pytube import Playlist
import webbrowser

class MainUI(QMainWindow, Ui_MainWindow):

    result =''

    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.loadComponents()

    def loadComponents(self):
        path = os.path.dirname(os.path.abspath(__file__))
        icon = path + '/../assets/icon.png'
        self.lbLogo.setPixmap(QPixmap(icon))

        self.setLoading(False)
        self.btnDownload.clicked.connect(self.download)
        self.actionExit.triggered.connect(self.close)
        self.actionDeveloper.triggered.connect(self.openSite)
        self.actionOpenFolder.triggered.connect(self.openFolder)

    def openSite(self):
        webbrowser.open('https://awaketecnologia.com.br/')

    def openFolder(self):
        webbrowser.open(os.path.realpath('../Downloads'))
        
    def setLoading(self, loading):
        self.pbStatus.setVisible(loading)
        self.lbStatus.setVisible(loading)
        self.btnDownload.setEnabled(not loading)
        self.leLink.setEnabled(not loading)



    def download(self):
        if(self.validate()):
            self.teResult.clear()
            self.result = ''
            self.thread = QThread()
            self.worker = Worker(self.leLink.text())
            self.worker.moveToThread(self.thread)

            self.worker.result.connect(self.onResult)
            self.worker.status.connect(self.onStatus)
            self.worker.loading.connect(self.setLoading)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.onEnd)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.started.connect(self.worker.run)

            self.thread.start()

    def onResult(self, r):
        self.result+=r
        self.teResult.setText(self.result)
        self.teResult.moveCursor(QTextCursor.End)


    def onEnd(self):
        QMessageBox.information(self, '...', 'Download finalizado')

    def onStatus(self, tex):
        self.lbStatus.setText(tex)

    def validate(self)->bool:
        if self.leLink.text() == '':
            QMessageBox.warning(self, 'Ops...', 'Informe a URL do video ou playlist')
            return False
        return True



class Worker(QThread):

    finished = Signal()
    loading = Signal(bool)
    result = Signal(str)
    status = Signal(str)

    def __init__(self, url=None):
        QThread.__init__(self)
        self.url = url

    def run(self):
        self.loading.emit(True)

        self.totalVideos = 0
        self.downloadedVideos = 0
        try:
            playlist_url = self.url

            play = Playlist(playlist_url)
            play._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

            path  = '../Downloads/'+play.title

            self.result.emit("*****\n")
            self.result.emit("Título: " + play.title+"\n")
            self.result.emit("Total de " + str(len(play.video_urls))+" vídeos "+"\n")
            self.result.emit("Pertence a: " + play.owner+"\n")
            self.result.emit("*****\n")
            self.totalVideos = len(play.video_urls)
            for url in play.video_urls:
                yt = YouTube(url)
                self.result.emit("\nBaixando: " + yt.title)
                self.status.emit(f"Baixando {self.downloadedVideos+1}/{self.totalVideos}: " + yt.title)
                video = yt.streams.filter(only_audio=True).first()
                downloaded_file = video.download(path)
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                os.rename(downloaded_file, new_file)
                self.result.emit("\nDownload completo.\n")
                self.status.emit("Download completo de " + yt.title)
                self.result.emit("******")
                self.downloadedVideos+=1
                        
            self.result.emit("\n*****")
            self.result.emit('Download Finalizado')
        except Exception as e:
            self.result.emit(str(e))
        finally:
            self.loading.emit(False)
            self.finished.emit()