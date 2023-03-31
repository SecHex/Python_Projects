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

        # arrange GUI elements in layout
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
        # get username from input field
        username = self.user_input.text()

        # make API request to get user information
        response = requests.get(f'https://api.github.com/users/{username}')

        # check if API request was successful
        if response.status_code == 200:
            # display user information in GUI
            user_data = response.json()
            self.name_label.setText(f"Name: {user_data['name']}")
            self.bio_label.setText(f"Bio: {user_data['bio']}")
            self.location_label.setText(f"Location: {user_data['location']}")
            self.followers_label.setText(f"Followers: {user_data['followers']}")
            self.following_label.setText(f"Following: {user_data['following']}")
        else:
            # display error message in GUI
            QMessageBox.warning(self, 'Error', f"Could not fetch user information for {username}. "
                                               f"Error message: {response.json()['message']}")


if __name__ == '__main__':
    app = QApplication([])
    user_search = GitHubUserSearch()
    user_search.show()
    app.exec_()
