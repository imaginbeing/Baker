from PyQt5.QtWidgets import QApplication
from mainform_window import MainForm
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    mf = MainForm()
    mf.show()

    app.exec()