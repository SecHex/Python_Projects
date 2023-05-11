import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class GitHubUserSearch(QWidget):
    def __init__(self):
        super().__init__()

        # set up GUI elements
        self.setWindowTitle('GitHub User Search')
        self.user_label = QLabel('Enter GitHub username:')
        self.user_input = QLineEdit()
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_user)
        self.name_label = QLabel('')
        self.bio_label = QLabel('')
        self.location_label = QLabel('')
        self.followers_label = QLabel('')
        self.following_label = QLabel('')


        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.name_label)
        layout.addWidget(self.bio_label)
        layout.addWidget(self.location_label)
        layout.addWidget(self.followers_label)
        layout.addWidget(self.following_label)
        self.setLayout(layout)

    def search_user(self):
        username = self.user_input.text()
        response = requests.get(f'https://api.github.com/users/{username}')

        if response.status_code == 200:
            user_data = response.json()
            self.name_label.setText(f"Name: {user_data['name']}")
            self.bio_label.setText(f"Bio: {user_data['bio']}")
            self.location_label.setText(f"Location: {user_data['location']}")
            self.followers_label.setText(f"Followers: {user_data['followers']}")
            self.following_label.setText(f"Following: {user_data['following']}")
        else:
            QMessageBox.warning(self, 'Error', f"Could not fetch user information for {username}. "
                                               f"Error message: {response.json()['message']}")


if __name__ == '__main__':
    app = QApplication([])
    user_search = GitHubUserSearch()
    user_search.show()
    app.exec_()
