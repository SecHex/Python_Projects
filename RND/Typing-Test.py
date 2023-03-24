import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer

class TypingSpeedTest(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.correct_chars = 0
        self.total_chars = 0
        self.accuracy = 0
        self.time_elapsed = 0
        self.lbl_text = QLabel("Type the following text:")
        self.txt_input = QTextEdit()
        self.txt_input.setPlaceholderText("Type here")
        self.btn_start = QPushButton("Start Test")
        self.lbl_result = QLabel()
        self.lbl_result.setAlignment(Qt.AlignCenter)
        self.lbl_result.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.btn_start.clicked.connect(self.startTest)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_text)
        vbox.addWidget(self.txt_input)
        vbox.addWidget(self.btn_start)
        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl_result)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.setWindowTitle("Typing Speed Test")
        self.setGeometry(100, 100, 400, 200)

    def startTest(self):
        self.correct_chars = 0
        self.total_chars = 0
        self.accuracy = 0
        self.time_elapsed = 0
        self.text_to_type = "The quick brown fox jumps over the lazy dog"
        self.lbl_text.setText("Type the following text: " + self.text_to_type)
        self.btn_start.setDisabled(True)
        self.txt_input.setFocus()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)

    def updateTimer(self):
        self.time_elapsed += 1
        
        input_text = self.txt_input.toPlainText()
        self.total_chars = len(input_text)
        self.correct_chars = sum(1 for i, j in zip(input_text, self.text_to_type) if i == j)
        self.accuracy = (self.correct_chars / self.total_chars) * 100 if self.total_chars > 0 else 0
        self.lbl_result.setText("Time Elapsed: {} seconds | Accuracy: {:.2f}%".format(self.time_elapsed, self.accuracy))

        if input_text == self.text_to_type:


            self.timer.stop()
            self.btn_start.setDisabled(False)
            self.txt_input.clear()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = TypingSpeedTest()
    ex.show()
    sys.exit(app.exec_())
