from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from requests import get
import requests
import sys
import os



# Thêm thư mục gốc của dự án vào PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from frontend.views.admin.ad_nguoidung_logic import AdNguoiDung
from frontend.views.admin.ad_phim_logic import AdminPhim
from frontend.views.admin.ad_trangchu import Ui_ad_trangchu
from frontend.views.admin.ad_themsuachitietphim_logic import AdminManagerFilm
class AdminTrangChu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ad_trangchu()
        self.ui.setupUi(self)

        # Kết nối các nút với hàm xử lý
        self.ui.ad_menu_trangchu.triggered.connect(self.resfesh)
        self.ui.tableWidget.cellDoubleClicked.connect(self.show_movie_details)
        self.ui.ad_menu_quanly_nguoidung.triggered.connect(self.open_admin_user)
        self.ui.ad_menu_quanly_phim.triggered.connect(self.open_admin_phim)
        self.ui.ad_trangchu_timkiem.clicked.connect(self.tim_kiem_phim)
        self.ui.ad_trangchu_them.clicked.connect(self.them_phim)
        self.ui.ad_trangchu_sua.clicked.connect(self.sua_phim)
        self.ui.ad_trangchu_xoa.clicked.connect(self.xoa_phim)

        # Tải danh sách phim khi khởi động
        # self.get_movies_from_web()
        self.load_movies(self.get_movies())

    def get_movies(self):
        try:
            response = requests.get("http://127.0.0.1:8000/api/movies")
            response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
            movies = response.json()
            
            return movies
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách phim: {e}")
            return []


    def load_movies(self, movies):
            movies = sorted(movies, key=lambda movie: movie.get("rank", float('inf')))
            self.ui.tableWidget.setColumnCount(5)
            print(len(movies))
            self.ui.tableWidget.setRowCount(len(movies))  # Đặt số hàng cho bảng

            try:
                for row, movie in enumerate(movies):
                    # Tạo các QTableWidgetItem và căn giữa nội dung
                    rank_item = QTableWidgetItem(str(movie.get("rank", "N/A")))
                    rank_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    title_item = QTableWidgetItem(movie.get("title", "N/A"))
                    title_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

                    score_item = QTableWidgetItem(str(movie.get("score", "N/A")))
                    score_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    episodes_item = QTableWidgetItem(str(movie.get("episodes", "N/A")))
                    episodes_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    detail_button = QPushButton("Xem chi tiết")
                    detail_button.setStyleSheet("background-color: rgb(105 105 105); color: rgb(245 245 245); font-weight: bold;")
                    detail_button.clicked.connect(self.show_movie_details)

                    # Thêm các mục vào bảng
                    self.ui.tableWidget.setItem(row, 0, rank_item)
                    self.ui.tableWidget.setItem(row, 1, title_item)
                    self.ui.tableWidget.setItem(row, 2, score_item)
                    self.ui.tableWidget.setItem(row, 3, episodes_item)
                    self.ui.tableWidget.setCellWidget(row, 4, detail_button)

                self.ui.tableWidget.viewport().update()
            except KeyError as e:
                print(f"Missing key {e} in movie data: {movie}")
       
        
    def tim_kiem_phim(self):
        """Tìm kiếm phim theo từ khóa"""
        print("Searching for movies...")
        keyword = self.ui.ad_trangchu_thanhtimkiem.text().strip()
        if not keyword:
            self.load_movies(self.get_movies())  # Tải lại danh sách phim nếu không có từ khóa
            return

        try:
            # Gọi API để tìm kiếm phim (giả sử API hỗ trợ tìm kiếm theo từ khóa)
            response = requests.get("http://127.0.0.1:8000/api/movies")
            response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
            movies = response.json()

            filtered_movies = [movie for movie in movies if keyword.lower() in movie["title"].lower()]

            if not filtered_movies:
                QMessageBox.information(self, "Kết quả tìm kiếm", "Không tìm thấy phim nào với từ khóa này.")
                return
            self.load_movies(filtered_movies)  # Tải danh sách phim đã lọc vào bảng
            self.clear_fileds()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tìm kiếm phim: {e}")

    def them_phim(self):
        """Xử lý thêm phim"""
        self.new_window = AdminManagerFilm()
        self.new_window.show()
        self.close()

    def sua_phim(self):
        """Xử lý sửa phim"""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một phim để sửa!")
            return
        
        rank = str(self.ui.tableWidget.item(selected_row, 0).text())
        title = str(self.ui.tableWidget.item(selected_row, 1).text())
        score = str(self.ui.tableWidget.item(selected_row, 2).text())
        episodes = str(self.ui.tableWidget.item(selected_row, 3).text())

        movies_list = self.get_movies()

        matching_movie = None

        for movie in movies_list:
            if (str(movie.get("rank", "")) == rank and
                str(movie.get("title", "")) == title and
                str(movie.get("score", "")) == score and
                str(movie.get("episodes", "")) == episodes):
                matching_movie = movie
                break
        
        self.new_window = AdminManagerFilm(matching_movie, edit=True)
        self.new_window.show()
        self.close()





    def xoa_phim(self):
        """Xử lý xóa phim"""
        selected_row = self.ui.tableWidget.currentRow()
        print(selected_row)
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một phim để xóa!")
            return
        rank = str(self.ui.tableWidget.item(selected_row, 0).text())
        title = str(self.ui.tableWidget.item(selected_row, 1).text())
        score = str(self.ui.tableWidget.item(selected_row, 2).text())
        episodes = str(self.ui.tableWidget.item(selected_row, 3).text())
        
        print(rank, title, score, episodes)

        movies_list = self.get_movies()

        matching_movie_delete = None
        for movie in movies_list:
            if (str(movie.get("rank", "")) == rank and
                str(movie.get("title", "")) == title and
                str(movie.get("score", "")) == score and
                str(movie.get("episodes", "")) == episodes):
                matching_movie_delete = movie
                break

        
        print(matching_movie_delete)
        # xóa phim có trong matching_movie_delete khỏi movies_list
        if matching_movie_delete:
        # Hiển thị hộp thoại xác nhận
            confirm = QMessageBox.question(
                self,
                "Xác nhận xóa",
                f"Bạn có chắc chắn muốn xóa phim '{matching_movie_delete.get('title', 'N/A')}' không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirm == QMessageBox.StandardButton.Yes:
                # Gọi API để xóa phim
                try:
                    print(f"Xóa phim có id: {matching_movie_delete['id']}")
                    response = requests.delete(f"http://127.0.0.1:8000/api/movies/{matching_movie_delete["id"]}/delete_movie")
                    response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
                    if response.status_code == 200:
                        QMessageBox.information(self, "Thành công", "Xóa phim thành công!")
                        self.load_movies(self.get_movies())  # Tải lại danh sách phim
                    else:
                        QMessageBox.critical(self, "Lỗi", "Không thể xóa phim!")
                except requests.exceptions.RequestException as e:
                    QMessageBox.critical(self, "Lỗi", f"Không thể xóa phim: {e}")
    def clear_fileds(self):
        """Xóa nội dung các trường tìm kiếm"""
        self.ui.ad_trangchu_thanhtimkiem.clear()

    def show_movie_details(self):
        selected_row = self.ui.tableWidget.currentRow()
        print("Selected row:", selected_row)
        print(selected_row)
        if selected_row == -1:
            return
        rank = str(self.ui.tableWidget.item(selected_row, 0).text())
        title = str(self.ui.tableWidget.item(selected_row, 1).text())
        score = str(self.ui.tableWidget.item(selected_row, 2).text())
        episodes = str(self.ui.tableWidget.item(selected_row, 3).text())
        
        movies_list = self.get_movies()

        matching_movie = None
        for movie in movies_list:
            if (str(movie.get("rank", "")) == rank and
                str(movie.get("title", "")) == title and
                str(movie.get("score", "")) == score and
                str(movie.get("episodes", "")) == episodes):
                matching_movie= movie
                break
        
        self.new_window = AdminManagerFilm(matching_movie)
        self.new_window.show()
        self.close()

    def resfesh(self):
        """Làm mới giao diện"""
        self.ui.ad_trangchu_thanhtimkiem.clear()
        self.load_movies(self.get_movies())

    def open_admin_user(self):
        self.new_window = AdNguoiDung()
        self.new_window.show()
        self.close()

    def open_admin_phim(self):
        """Mở giao diện quản lý phim"""
        self.new_window = AdminPhim()  # Tạo instance của giao diện AdminPhim
        self.new_window.show()         # Hiển thị giao diện AdminPhim
        self.close()                   # Đóng giao diện hiện tại
        
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AdminTrangChu()
    window.show()
    sys.exit(app.exec())

