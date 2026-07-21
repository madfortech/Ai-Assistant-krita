from krita import DockWidget
from .settings_dialog import SettingsDialog
from .protocol import Protocol
from .executor import Executor

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QMessageBox,
)


from .api import generate, me


DOCKER_TITLE = "AI Assistant"


class DockerTemplate(DockWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(DOCKER_TITLE)

        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Title
        title = QLabel("🤖 AI Assistant")
        layout.addWidget(title)

        self.settings_btn = QPushButton("⚙ Settings")
        self.settings_btn.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_btn)

        self.name_label = QLabel("Name : -")
        layout.addWidget(self.name_label)

        self.plan_label = QLabel("Plan : -")
        layout.addWidget(self.plan_label)

        self.credit_label = QLabel("Credits : -")
        layout.addWidget(self.credit_label)

        # ==========================
        # Prompt
        # ==========================

        layout.addWidget(QLabel("Prompt"))

        self.prompt_box = QTextEdit()
        self.prompt_box.setPlaceholderText(
            "Describe what you want to create..."
        )
        layout.addWidget(self.prompt_box)

        # Generate
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.generate_image)
        layout.addWidget(self.generate_btn)

        self.setWidget(widget)
        self.load_user_info()

    def generate_image(self):
        prompt = self.prompt_box.toPlainText().strip()

        if not prompt:
            QMessageBox.warning(
                None,
                "AI Assistant",
                "Please enter a prompt."
            )
            return

        try:
            result = generate(prompt)
            print("RESULT:", result)
            # Update user info
            self.plan_label.setText(
                f"Plan : {result.get('plan', '-')}"
            )

            self.credit_label.setText(
                f"Credits : {result.get('credits_remaining', 0)}"
            )

            # Parse AI commands
            commands = Protocol.parse(result)

          
            print("COMMANDS:", commands)
            print("COUNT:", len(commands))

            from PyQt5.QtWidgets import QMessageBox

            QMessageBox.information(
                None,
                "Commands Count",
                str(len(commands))
            )

            # Execute commands
            Executor().execute(commands)

            # Optional: show status
            self.prompt_box.setPlainText(
                f"Executed {len(commands)} command(s)"
            )

        except Exception as e:
            QMessageBox.critical(
                None,
                "Error",
                str(e)
            )
        
    def open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec_()
    
    def load_user_info(self):
        try:
            user = me()

            self.name_label.setText(
                f"Name : {user['name']}"
            )

            self.plan_label.setText(
                f"Plan : {user['plan']}"
            )

            self.credit_label.setText(
                f"Credits : {user['credits_remaining']}"
            )

        except Exception:
            self.name_label.setText("Name : Offline")

    def canvasChanged(self, canvas):
        pass