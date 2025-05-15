from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from requests import get
import requests
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from frontend.views.admin.ad_phim import Ui_ad_trang_ql_phim
from frontend.views.admin.ad_themsuachitietphim_logic import AdminManagerFilm

class AdminPhim(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ad_trang_ql_phim()
        self.ui.setupUi(self)

        # Kết nối các nút với hàm xử lý
        self.ui.ad_trang_qlp_bangphim.cellClicked.connect(self.on_table_row_clicked)
        self.ui.ad_trang_qlp_bangphim.cellDoubleClicked.connect(self.show_movie_details)
        self.ui.ad_trang_qlp_back.clicked.connect(self.back_to_main)
        self.ui.ad_trang_qlp_timkiem.clicked.connect(self.tim_kiem_phim)
        self.ui.ad_trang_qlp_them.clicked.connect(self.them_phim)
        self.ui.ad_trang_qlp_sua.clicked.connect(self.sua_phim)
        self.ui.ad_trang_qlp_xoa.clicked.connect(self.xoa_phim)

        # Tải danh sách phim khi khởi động
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
        
    def get_movie_detail(self, movie_id):
        try:
            print(f"Fetching movie detail for ID: {movie_id}")
            response = requests.get(f"http://127.0.0.1:8000/api/movies/{movie_id}/movie-detail")
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
            response.raise_for_status()
            movie_detail = response.json()
            return movie_detail
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải chi tiết phim: {e}")
            return []
        
    def get_reviews(self, movie_id):
        try:
            # Gửi yêu cầu GET đến API để lấy danh sách review của user
            response = requests.get(f"http://localhost:8000/api/review/{movie_id}/review-by-movie")
            response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP

            # Lấy dữ liệu JSON từ phản hồi
            reviews = response.json()
            return reviews
          
        except requests.exceptions.RequestException as e:
            # Hiển thị thông báo lỗi nếu không thể tải dữ liệu
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách review: {e}")
            return []
    
    def load_movies(self, movies):
            movies = sorted(movies, key=lambda movie: movie.get("rank", float('inf')))
            self.ui.ad_trang_qlp_bangphim.setColumnCount(5)
            self.ui.ad_trang_qlp_bangphim.setRowCount(len(movies))  # Đặt số hàng cho bảng

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
                    self.ui.ad_trang_qlp_bangphim.setItem(row, 0, rank_item)
                    self.ui.ad_trang_qlp_bangphim.setItem(row, 1, title_item)
                    self.ui.ad_trang_qlp_bangphim.setItem(row, 2, score_item)
                    self.ui.ad_trang_qlp_bangphim.setItem(row, 3, episodes_item)
                    self.ui.ad_trang_qlp_bangphim.setCellWidget(row, 4, detail_button)

                self.ui.ad_trang_qlp_bangphim.viewport().update()
            except KeyError as e:
                print(f"Missing key {e} in movie data: {movie}")

    def tim_kiem_phim(self):
        """Tìm kiếm phim theo từ khóa"""
        print("Searching for movies...")
        keyword = self.ui.ad_trang_qlp_thanhtimkiem.text().strip()
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
        selected_row = self.ui.ad_trang_qlp_bangphim.currentRow()
        print("Selected row:", selected_row)
        print(selected_row)
        if selected_row == -1:
            return
        rank = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 0).text())
        title = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 1).text())
        score = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 2).text())
        episodes = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 3).text())
        
        movies_list = self.get_movies()

        matching_movie = None
        for movie in movies_list:
            if (str(movie.get("rank", "")) == rank and
                str(movie.get("title", "")) == title and
                str(movie.get("score", "")) == score and
                str(movie.get("episodes", "")) == episodes):
                matching_movie= movie
                break
        
        self.new_window = AdminManagerFilm(matching_movie, edit=True)
        self.new_window.show()
        self.close()

    def xoa_phim(self):
        """Xử lý xóa phim"""
        selected_row = self.ui.ad_trang_qlp_bangphim.currentRow()
        print(selected_row)
        if selected_row == -1:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một phim để xóa!")
            return
        rank = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 0).text())
        title = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 1).text())
        score = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 2).text())
        episodes = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 3).text())
        
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
        self.ui.ad_trang_qlp_thanhtimkiem.clear()

    def show_movie_details(self):
        selected_row = self.ui.ad_trang_qlp_bangphim.currentRow()
        print("Selected row:", selected_row)
        print(selected_row)
        if selected_row == -1:
            return
        rank = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 0).text())
        title = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 1).text())
        score = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 2).text())
        episodes = str(self.ui.ad_trang_qlp_bangphim.item(selected_row, 3).text())
        
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

    def on_table_row_clicked(self, row, column):
        """
        Xử lý khi người dùng nhấp vào một hàng trong bảng.
        """
        # Lấy thông tin phim từ hàng đã chọn
        rank = str(self.ui.ad_trang_qlp_bangphim.item(row, 0).text())
        title = str(self.ui.ad_trang_qlp_bangphim.item(row, 1).text())
        score = str(self.ui.ad_trang_qlp_bangphim.item(row, 2).text())
        episodes = str(self.ui.ad_trang_qlp_bangphim.item(row, 3).text())

        movies_list = self.get_movies()

        matching_movie = None
        for movie in movies_list:
            if (str(movie.get("rank", "")) == rank and
                str(movie.get("title", "")) == title and
                str(movie.get("score", "")) == score and
                str(movie.get("episodes", "")) == episodes):
                matching_movie = movie
                break

        if not matching_movie:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy phim trong danh sách!")
            return

        movie_detail = self.get_movie_detail(matching_movie["id"])
        if not movie_detail:
            QMessageBox.warning(self, "Lỗi", "Không thể tải chi tiết phim!")
            return

        image_path = r"C:\Users\khoat\Pictures\Save Picture\cropped-SGU-LOGO.png"
        pixmap = QPixmap(image_path)
        self.ui.ad_trang_qlp_anhphim.setPixmap(pixmap)
        self.ui.ad_trang_qlp_anhphim.setScaledContents(True)

        self.ui.ad_trang_qlp_tenphim.setText(str(matching_movie.get("title", "N/A")))
        self.ui.ad_trang_qlp_rank.setText(rank)
        self.ui.ad_trang_qlp_trangthai.setText(str(movie_detail.get("status", "N/A")))  # Ví dụ: trạng thái có thể lấy từ API
        self.ui.ad_trang_qlp_nam.setText(str(movie_detail.get("aired", "N/A")))

        self.ui.ad_trang_qlp_motaphim.setHtml(f"""
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html>
            <head>
                <meta name="qrichtext" content="1" />
                <style type="text/css">
                    p, li {{ white-space: pre-wrap; }}
                </style>
            </head>
            <body style="font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:italic;">
                <h3 style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                                                Mô tả phim
                </h3>
                <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                    {movie_detail.get('synopsis', 'N/A')}
                </p>
            </body>
            </html>
            """)
        
        rewiews = self.get_reviews(movie_detail["id"])
        print(rewiews)
        self.load_reviews(rewiews)
        
    def load_reviews(self, reviews):
        """
        Tải các bài review của user dựa trên user_id và hiển thị lên bảng ad_nguoidung_baiviet.
        """

        # Xóa dữ liệu cũ trên bảng
        self.ui.ad_nguoidung_baiviet.setColumnCount(3)
        self.ui.ad_nguoidung_baiviet.setRowCount(len(reviews))

        # Duyệt qua danh sách review và thêm vào bảng
        # Duyệt qua danh sách review và thêm vào bảng
        for row, review in enumerate(reviews):
            
            id = QTableWidgetItem(str(review.get("id", "N/A")))
            id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.ad_nguoidung_baiviet.setItem(row, 0, id)
                
            movie_id = QTableWidgetItem(str(review.get("movie_detail_id", "N/A")))
            movie_id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.ad_nguoidung_baiviet.setItem(row, 1, movie_id)

            # Thêm nội dung review
            content_item = QTableWidgetItem(review.get("show_reviews", "N/A"))
            content_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            self.ui.ad_nguoidung_baiviet.setItem(row, 2, content_item)
    def back_to_main(self):
        """
        Quay lại giao diện chính.
        """
        from frontend.views.admin.ad_trangchu_logic import AdminTrangChu
        self.close()
        self.main_window = AdminTrangChu()
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPhim()
    window.show()
    sys.exit(app.exec())