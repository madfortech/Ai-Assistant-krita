from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
)

from .settings import (
    save_api_url,
    save_api_key,
    get_api_url,
    get_api_key,
)


class SettingsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("AI Assistant Settings")
        self.setMinimumWidth(450)

        layout = QVBoxLayout(self)

        # API URL
        layout.addWidget(QLabel("API URL"))

        self.api_url = QLineEdit()
        self.api_url.setPlaceholderText(
            "https://aiassistant.test/api/generate"
        )
        self.api_url.setText(get_api_url())
        layout.addWidget(self.api_url)

        # API Key
        layout.addWidget(QLabel("Unique Key"))

        self.api_key = QLineEdit()
        self.api_key.setEchoMode(QLineEdit.Password)
        self.api_key.setPlaceholderText("Enter your Unique Key")
        self.api_key.setText(get_api_key())
        layout.addWidget(self.api_key)

        # Buttons
        button_layout = QHBoxLayout()

        self.save_btn = QPushButton("Save")
        self.cancel_btn = QPushButton("Cancel")

        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.cancel_btn)

        layout.addLayout(button_layout)

        self.save_btn.clicked.connect(self.save_settings)
        self.cancel_btn.clicked.connect(self.close)

    def save_settings(self):
        save_api_url(self.api_url.text().strip())
        save_api_key(self.api_key.text().strip())

        QMessageBox.information(
            self,
            "Settings",
            "Settings saved successfully."
        )

        self.accept()