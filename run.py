from PySide2.QtWidgets import QApplication, QStyleFactory
import sys

from views import MainUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    window = MainUI()
    window.show()
    sys.exit(app.exec_())