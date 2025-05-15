from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from requests import get
import requests
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from frontend.views.admin.ad_trangcanhan import Ui_ad_trangcanhan



class AdminTrangcanhanFilm(QMainWindow):
    def __init__(self, user=None):
        super().__init__()
        self.user = user
        self.ui = Ui_ad_trangcanhan()
        self.ui.setupUi(self)
        

        self.ui.ad_tranguser_nuttimkiem.clicked.connect(self.search)
        self.ui.ad_trangcanhan_baned.clicked.connect(self.baned_and_unclock)
        self.ui.ad_tranguser_back.clicked.connect(self.back_to_main)
        self.ui.ad_tranguser_luu.clicked.connect(self.save)
  
    def get_movies(self):
        try:
            response = requests.get("http://127.0.0.1:8000/api/movies")
            response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
            movies = response.json()
            
            return movies
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách phim: {e}")
            return []
        
    def get_reviews(self, user_id):
        try:
            # Gửi yêu cầu GET đến API để lấy danh sách review của user
            response = requests.get(f"http://localhost:8000/api/review/{user_id}/review-by-user")
            response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP

            # Lấy dữ liệu JSON từ phản hồi
            reviews = response.json()
            return reviews
          
        except requests.exceptions.RequestException as e:
            # Hiển thị thông báo lỗi nếu không thể tải dữ liệu
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách review: {e}")
            return []
        
    def get_favorites(self, user_id):
        try:
            response = requests.get(f"http://127.0.0.1:8000/api/movies/user/{user_id}/favorites-movies")
            response.raise_for_status()  # Kiểm tra lỗi HTTP
            favorite_movies = response.json()  # Lấy dữ liệu JSON từ API

            return favorite_movies
          
        except requests.exceptions.RequestException as e:
            # Hiển thị thông báo lỗi nếu không thể tải dữ liệu
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách review: {e}")
            return []

    def set_up_details(self):
    
        """Thiết lập thông tin chi tiết người dùng"""
        print(self.user)
        self.ui.chublogphim_12.setText(self.user["username"])
        self.ui.chublogphim_13.setText(self.user["id"])
        self.ui.chublogphim_14.setText(self.user["date_of_birth"])
        self.ui.chublogphim_15.setText(self.user["role"])

        print(self.user["status"])

        if self.user["status"] == 1:
            self.ui.ad_trangcanhan_baned.setText("BANED")
        else:
            self.ui.ad_trangcanhan_baned.setText("UNCLOCK")

        favorite_movies = self.get_favorites(self.user["id"])
        self.load_favorite_movies(favorite_movies)
        reviews = self.get_reviews(self.user["id"])
        self.load_reviews(reviews)

    def load_favorite_movies(self, favorites_movies):
        """
        Tải danh sách phim yêu thích của user và hiển thị lên bảng.
        """      

            # Lọc các phim yêu thích từ danh sách phim
            # favorite_movie_ids = {int(fav["movie_id"]) for fav in favorite_movies}
        self.ui.ad_trangchu_bangphim.setRowCount(len(favorites_movies))
        self.ui.ad_trangchu_bangphim.setColumnCount(3)
        self.ui.ad_trangchu_bangphim.setHorizontalHeaderLabels(["ID", "MOVIE ID", "HÀNH ĐỘNG"])

        for row, movie in enumerate(favorites_movies):
                
            print(movie)
                # Tạo các QTableWidgetItem
            id_item = QTableWidgetItem(str(movie.get("id", "N/A")))
            movieid_item = QTableWidgetItem(str(movie.get("movie_id", "N/A")))

                # Tạo nút "Xem chi tiết"
            detail_button = QPushButton("Xóa")
            detail_button.setStyleSheet("background-color: rgb(255, 69, 58); color: white; font-weight: bold;")
            detail_button.clicked.connect(self.delete_favorite)

                # Thêm thông tin vào bảng
            self.ui.ad_trangchu_bangphim.setItem(row, 0, id_item)
            self.ui.ad_trangchu_bangphim.setItem(row, 1, movieid_item)
            self.ui.ad_trangchu_bangphim.setCellWidget(row, 2, detail_button)

        self.ui.ad_trangchu_bangphim.viewport().update()


    def load_reviews(self, reviews):
        """
        Tải các bài review của user dựa trên user_id và hiển thị lên bảng ad_nguoidung_baiviet.
        """

        # Xóa dữ liệu cũ trên bảng
        self.ui.ad_nguoidung_baiviet.setColumnCount(4)
        self.ui.ad_nguoidung_baiviet.setRowCount(len(reviews))

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

            # Thêm hành động (ví dụ: Xóa review)
            action_button = QPushButton("Xóa")
            action_button.setStyleSheet("background-color: rgb(255, 69, 58); color: white; font-weight: bold;")
            action_button.clicked.connect(self.delete_review)
            self.ui.ad_nguoidung_baiviet.setCellWidget(row, 3, action_button)

    def back_to_main(self):
        """Quay lại trang chính"""
        from frontend.views.admin.ad_trangchu_logic import AdminTrangChu
        self.close()
        self.main_window = AdminTrangChu()
        self.main_window.show() 


    def search(self):
        search_text = self.ui.ad_tranguser_thanhtimkiem.text()

        # Lấy dữ liệu JSON từ phản hồi
        reviews = self.get_reviews(self.user["id"])

        if search_text:
            filtered_data = [re for re in reviews if search_text.lower() in str(re.get("id", "")).lower() or search_text.lower() in str(re.get("movie_id", "")) or search_text.lower() in re.get("show_reviews", "").lower() ]
            self.load_reviews(filtered_data)
            self.clear_fileds()
        else:
            self.load_reviews(self.get_reviews(self.user["id"]))
            self.clear_fileds()
    
        
    def baned_and_unclock(self):
        """
        Ban hoặc unclock user dựa trên trạng thái hiện tại.
        """
        user_id = self.user["id"]
        current_status = self.user["status"]  # Lấy trạng thái hiện tại của user
        action = self.ui.ad_trangcanhan_baned.text()  # Lấy text của nút để xác định hành động

        # Xác định API endpoint và thông báo dựa trên hành động
        if action == "BANED":
            api_endpoint = f"http://127.0.0.1:8000/api/user/banned/{user_id}"
            success_message = "Người dùng đã bị khóa thành công!"
            error_message = "Không thể khóa người dùng!"
            new_status = 0  # Trạng thái sau khi bị ban
        elif action == "UNCLOCK":
            api_endpoint = f"http://127.0.0.1:8000/api/user/unlock/{user_id}"
            success_message = "Người dùng đã được mở khóa thành công!"
            error_message = "Không thể mở khóa người dùng!"
            new_status = 1  # Trạng thái sau khi được mở khóa
        else:
            QMessageBox.warning(self, "Lỗi", "Hành động không hợp lệ!")
            return

        # Gửi yêu cầu đến API
        try:
            response = requests.post(api_endpoint)
            response.raise_for_status()  # Kiểm tra lỗi HTTP

            # Cập nhật trạng thái người dùng trên giao diện
            self.user["status"] = new_status
            if new_status == 1:
                self.ui.ad_trangcanhan_baned.setText("BANED")
            else:
                self.ui.ad_trangcanhan_baned.setText("UNCLOCK")

            # Hiển thị thông báo thành công
            QMessageBox.information(self, "Thành công", success_message)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"{error_message}\nChi tiết lỗi: {e}")



    def save(self):
        """Lưu thông tin người dùng"""
        print("Lưu thông tin người dùng")

    def clear_fileds(self):
        self.ui.ad_tranguser_thanhtimkiem.clear()

    def delete_favorite(self):
        """
        Xóa một bộ phim yêu thích của user.
        """
        # Lấy dòng được chọn trong bảng
        selected_row = self.ui.ad_trangchu_bangphim.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để xóa!")
            return

        # Lấy thông tin movie_id từ dòng được chọn
        movie_id_item = self.ui.ad_trangchu_bangphim.item(selected_row, 1)
        if not movie_id_item:
            QMessageBox.warning(self, "Lỗi", "Không thể lấy thông tin movie_id!")
            return

        movie_id = int(movie_id_item.text())
        user_id = self.user["id"]

        # Hiển thị hộp thoại xác nhận
        confirm = QMessageBox.question(
            self,
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa phim yêu thích với ID {movie_id} không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                # Gửi yêu cầu DELETE đến API
                response = requests.delete(
                    "http://127.0.0.1:8000/api/movies/remove-favorites-movies",
                    params={"user_id": user_id, "movie_id": movie_id},
                )
                response.raise_for_status()  # Kiểm tra lỗi HTTP

                # Xóa dòng khỏi bảng
                self.ui.ad_trangchu_bangphim.removeRow(selected_row)

                # Hiển thị thông báo thành công
                QMessageBox.information(self, "Thành công", "Xóa phim yêu thích thành công!")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể xóa phim yêu thích: {e}")["id"]

    def delete_review(self):
        """
        Xóa một bài review của user.
        """
        # Lấy dòng được chọn trong bảng
        selected_row = self.ui.ad_nguoidung_baiviet.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để xóa!")
            return

        # Lấy thông tin review_id từ dòng được chọn
        review_id_item = self.ui.ad_nguoidung_baiviet.item(selected_row, 0)
        if not review_id_item:
            QMessageBox.warning(self, "Lỗi", "Không thể lấy thông tin review_id!")
            return

        try:
            review_id = int(review_id_item.text())
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "ID bài review không hợp lệ!")
            return

        # Hiển thị hộp thoại xác nhận
        confirm = QMessageBox.question(
            self,
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa bài review với ID {review_id} không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                # Gửi yêu cầu DELETE đến API
                response = requests.delete(f"http://127.0.0.1:8000/api/review/{review_id}/delete-review")
                response.raise_for_status()  # Kiểm tra lỗi HTTP

                # Xóa dòng khỏi bảng
                self.ui.ad_nguoidung_baiviet.removeRow(selected_row)

                # Hiển thị thông báo thành công
                QMessageBox.information(self, "Thành công", "Xóa bài review thành công!")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể xóa bài review: {e}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminTrangcanhanFilm()
    window.show()
    sys.exit(app.exec())