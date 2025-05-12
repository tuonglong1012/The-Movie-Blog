# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from views.login_views import LoginDialog
from views.signup_views import SignUpDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Review App")
        self.setGeometry(100, 100, 800, 600)

        self.show_login_dialog()

    def show_login_dialog(self):
        login_dialog = LoginDialog(self)
        if login_dialog.exec_() == login_dialog.Accepted:
            QMessageBox.information(self, "Success", "Logged in successfully!")

    def open_signup_dialog(self):
        signup_dialog = SignUpDialog(self)
        if signup_dialog.exec_() == signup_dialog.Accepted:
            self.show_login_dialog()

    def open_login_dialog(self):
        self.show_login_dialog()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
