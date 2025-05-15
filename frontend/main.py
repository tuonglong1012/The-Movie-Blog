import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget
from views.account_views.login_views import LoginDialog
from views.account_views.signup_views import SignUpDialog
from views.trangchu.trangchu_views import AnimeListPage  
from views.chat_lounge_views import AnimeWatchApp
from views.admin.ad_trangchu_logic import AdminTrangChu
from controllers.trangchu_controller import get_all_movies

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
    

    def show_login_dialog(self):
        login_dialog = LoginDialog(self)
        if login_dialog.exec_() == login_dialog.Accepted:
            self.user_info = login_dialog.get_user_info()
            QMessageBox.information(self, "Success", "Logged in successfully!")

            # Kiểm tra role và điều hướng
            if self.user_info.get("role") == 0:
                self.open_admin_page()
            else:
                self.open_home_page()

        else:
            self.close()
            
    def open_home_page(self):
        self.home_page = AnimeListPage(main_window=self)
        self.central_widget.addWidget(self.home_page)
        self.central_widget.setCurrentWidget(self.home_page)
    def open_admin_page(self):
        self.admin_page = AdminTrangChu(main_window=self)
        self.central_widget.addWidget(self.admin_page)
        self.central_widget.setCurrentWidget(self.admin_page)

    
    def go_to_chat(self):
        self.main_window.open_chat_page()
    
    def return_to_chat(self):
        if self.chat_window:
            self.chat_window.show()
        self.close()
    def init_ui(self):
        

        # Gọi API lấy dữ liệu phim
        movies = []
        result = get_all_movies()
        if isinstance(result, list):
            movies = result
        else:
            print("Lỗi khi lấy dữ liệu:", result.get("error", "Không rõ lỗi"))

        # Gán trang AnimeListPage làm central widget
        self.anime_page = AnimeListPage(main_window=self, movies=movies)
        self.setCentralWidget(self.anime_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
