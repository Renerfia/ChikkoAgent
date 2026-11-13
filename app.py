import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from app.components.ChatWindow import ChatInterface


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pages = {
            "chat": ChatInterface(),
        }

        self.stack = QStackedWidget()

        for page in self.pages.values():
            self.stack.addWidget(page)
            page.navigate_requested.connect(self.show_page)

        self.setCentralWidget(self.stack)
        self.show_page("chat")

    @Slot(str)
    def show_page(self, page_name: str):
        self.stack.setCurrentWidget(self.pages[page_name])


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()