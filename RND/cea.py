class CaesarEncryptionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.input_label = QLabel("Text, der verschlüsselt werden soll:")
        self.input_text = QLineEdit()
        self.shift_label = QLabel("Anzahl der Zeilen, um die verschoben werden soll:")
        self.shift_value = QLineEdit()
        self.output_label = QLabel("Verschlüsselter Text:")
        self.output_text = QTextEdit()
        self.encrypt_button = QPushButton("Verschlüsseln")
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button = QPushButton("Entschlüsseln")
        self.decrypt_button.clicked.connect(self.decrypt)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_value)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def encrypt(self):
        text = self.input_text.text()
        shift = int(self.shift_value.text())
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += char
                
        self.output_text.setText(encrypted_text)

    def decrypt(self):
        encrypted_text = self.output_text.toPlainText()
        shift = int(self.shift_value.text())
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += char
                
        self.input_text.setText(decrypted_text)
