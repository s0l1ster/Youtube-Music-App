import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class YouTubeMusicApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Music App")
        self.setGeometry(100, 100, 1200, 800)

        self.setWindowIcon(QIcon("MAIN.png"))


        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QPushButton {
                background-color: #1f1f1f;
                color: white;
                border: 1px solid #333;
                padding: 8px;
                font-size: 40px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #292929;
            }
            QPushButton:pressed {
                background-color: #404040;
            }               
            QMenuBar {
                background-color: #292929;
                color: dark;
            }
            QMenuBar::item {
                padding: 6px;
                background: transparent;
            }
            QMenuBar::item:selected {
                background: #404040;
            }
        """)

        # Create browser widget
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://music.youtube.com/"))

        menu = self.menuBar()

        nav = menu.addMenu("Navigation")

        # Buttons (Optional)
        back_action = QAction("←", self)
        forward_action = QAction("→", self)
        refresh_action = QAction("⟳", self)

        back_action.triggered.connect(self.browser.back)
        forward_action.triggered.connect(self.browser.forward)
        refresh_action.triggered.connect(self.browser.reload)

        nav.addAction(back_action)
        nav.addAction(forward_action)
        nav.addAction(refresh_action)

        # Set layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeMusicApp()
    window.show()
    sys.exit(app.exec_())
