import sys
import json
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QFileDialog, QDialog,
                             QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QInputDialog, QWidget)
from cryptography.fernet import Fernet


class PasswordManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.resize(400, 300)

        # Initialize the Fernet cipher with a randomly generated key
        self.fernet = Fernet.generate_key()
        self.fernet = Fernet(self.fernet)

        # Create the GUI
        self.create_menu()
        self.create_layout()

    def create_menu(self):
        # Create the File menu
        file_menu = self.menuBar().addMenu("&File")

        # Add the Open action to the File menu
        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_password_file)
        file_menu.addAction(open_action)

    def create_layout(self):
        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the username label and line edit
        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        self.username_edit = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_edit)

        # Create the password label and line edit
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_edit)

        # Create the save button
        save_button = QPushButton("Save Password")
        save_button.clicked.connect(self.save_passwords)

        # Add the layouts and button to the main layout
        main_layout.addLayout(username_layout)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(save_button)

        # Create the widget and set the layout
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def open_password_file(self):
        # Allow the user to select a password file to open
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Password File", "", "Password Files (*.pwm)",
                                                   options=options)
        if file_name:
            with open(file_name, "rb") as f:
                try:
                    decrypted_data = self.fernet.decrypt(f.read()).decode()
                    password_data = json.loads(decrypted_data)
                except:
                    QMessageBox.warning(self, "Password Manager",
                                        "Incorrect master password or invalid file format.")
                    #return

                # Display the username and password in the selected file
                self.username_edit.setText(self.fernet.decrypt(password_data["username"].encode()).decode())
                self.password_edit.setText(self.fernet.decrypt(password_data["password"].encode()).decode())

    def save_passwords(self):
        # Allow the user to select a file name and location to save the password data
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Passwords File", "", "Password Manager Files (*.pwm)",
                                                   options=options)
        if file_name:
            # Make sure the file name ends with the correct extension
            if not file_name.endswith(".pwm"):
                file_name += ".pwm"

            # Read the existing passwords from the file, or create an empty dictionary if the file doesn't exist
            passwords = {}
            if os.path.exists(file_name):
                with open(file_name, "rb") as f:
                    try:
                        decrypted_data = self.fernet.decrypt(f.read()).decode()
                        passwords = json.loads(decrypted_data)
                    except:
                        QMessageBox.warning(self, "Password Manager", "Invalid file format.")
                        return

            # Add the new password to the dictionary
            username = self.username_edit.text()
            password = self.password_edit.text()
            if username and password:
                passwords[username] = self.fernet.encrypt(password.encode()).decode()

            # Write the updated dictionary back to the file
            with open(file_name, "wb") as f:
                f.write(self.fernet.encrypt(json.dumps(passwords).encode()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    password_manager = PasswordManager()
    password_manager.show()
    sys.exit(app.exec_())
