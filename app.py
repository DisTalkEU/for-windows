import sys
import ctypes
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon, QPixmap

# Taskleisten-Icon korrekt setzen
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("distalk.app")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DisTalk")
        self.setWindowIcon(QIcon("icon.ico"))

        # Maximiert starten
        self.showMaximized()

        # Browserfenster
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Feature-Permission für Mikrofon/Kamera
        self.page = QWebEnginePage()
        self.page.featurePermissionRequested.connect(self.on_feature_permission)
        self.browser.setPage(self.page)

        # URL laden
        self.browser.setUrl(QUrl("https://app.distalk.eu"))

        # Vollbild per F11
        self.is_fullscreen = False

    def on_feature_permission(self, url, feature):
        # Mikrofon/Kamera erlauben
        if feature in (
            QWebEnginePage.Feature.MediaAudioCapture,
            QWebEnginePage.Feature.MediaVideoCapture,
            QWebEnginePage.Feature.MediaAudioVideoCapture
        ):
            self.browser.page().setFeaturePermission(
                url, feature, QWebEnginePage.PermissionPolicy.PermissionGrantedByUser
            )

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

    # Splashscreen
    splash_pix = QPixmap("splash.png")
    splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()
    time.sleep(2)

    window = MainWindow()
    window.show()
    splash.finish(window)

    sys.exit(app.exec())