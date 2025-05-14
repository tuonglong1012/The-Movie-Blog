import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget
from frontend.views.account_views.login_views import LoginDialog
from frontend.views.account_views.signup_views import SignUpDialog
from frontend.views.trangchu.trangchu_views import AnimeListPage  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Review App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QStackedWidget(self)  
        self.setCentralWidget(self.central_widget)

        # Hiển thị login dialog ngay khi bắt đầu
        self.show_login_dialog()

    def show_login_dialog(self):
        login_dialog = LoginDialog(self)
        if login_dialog.exec_() == login_dialog.Accepted:
            QMessageBox.information(self, "Success", "Logged in successfully!")
            self.open_home_page()
        else:
            self.close()  # Đóng ứng dụng nếu login thất bại

    def open_home_page(self):
        home_page = AnimeListPage(self)
        self.central_widget.addWidget(home_page)  
        self.central_widget.setCurrentWidget(home_page)  

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
