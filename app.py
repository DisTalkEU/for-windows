import sys
import ctypes
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon

# Taskleisten-Icon korrekt setzen
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("distalk.app")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DisTalk")
        self.setWindowIcon(QIcon("icon.ico"))

        # Anfangsgröße, Minimum und Maximum für Vollbild
        self.resize(1200, 800)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(16777215, 16777215)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowMaximizeButtonHint)

        # Browserfenster
        browser = QWebEngineView()
        browser.setUrl(QUrl("https://app.distalk.eu"))
        self.setCentralWidget(browser)

        # Vollbild per F11
        self.is_fullscreen = False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F11:
            if self.is_fullscreen:
                self.showNormal()
                self.is_fullscreen = False
            else:
                self.showFullScreen()
                self.is_fullscreen = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())