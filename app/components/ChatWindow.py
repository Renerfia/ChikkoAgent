from PySide6.QtWidgets import QWidget, QTextBrowser, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Signal
from config.model_config import response_agent

class ChatInterface(QWidget):
    navigate_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.messages = QTextBrowser()
        self.input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.message_history = []

        self.input.returnPressed.connect(self.send_message)
        self.send_button.clicked.connect(self.send_message)

        row = QHBoxLayout()
        row.addWidget(self.input)
        row.addWidget(self.send_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.messages)
        layout.addLayout(row)

        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_button)


    def open_settings(self):
        self.navigate_requested.emit("settings")

    def send_message(self):
        text = self.input.text().strip()
        if not text:
            return

        self.message_history.append({"role": "user", "message": text})
        self.messages.append(f"You: {text}")
        self.input.clear()
        try:
            response = response_agent.run_sync(text)
        except Exception as error:
            self.messages.append(f"Error: {error or type(error).__name__}")
            return

        self.messages.append(f"Chikko: {response.output}")
        self.message_history.append(
            {"role": "assistant", "message": str(response.output)}
        )
