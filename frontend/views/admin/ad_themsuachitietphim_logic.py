import uuid
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QColor, QDesktopServices
from pydantic import ValidationError
from requests import get
import requests
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from backend.app.schemas.movie_schemas import MovieIn
from frontend.views.admin.ad_themsuachitietphim import Ui_ad_themphim



class AdminManagerFilm(QMainWindow):
    def __init__(self, movie=None, edit=False):
        """
        Khởi tạo giao diện quản lý phim.
        Nếu `movie` được truyền, vào chế độ xem chi tiết.
        Nếu không, vào chế độ thêm mới phim.
        """
        super().__init__()
        self.ui = Ui_ad_themphim()
        self.ui.setupUi(self)

         # Kiểm tra chế độ (xem chi tiết hoặc thêm mới)
        self.movie = movie
        if self.movie:
            if edit:
                self.setup_edit_mode()
                self.ui.ad_themphim_them_nhanvat.clicked.connect(self.add_character)
                self.ui.ad_themphim_sua_nhanvat.clicked.connect(self.edit_character)
                self.ui.ad_themphim_xoa_nhanvat.clicked.connect(self.delete_character)
            else:
                self.setup_detail_mode()
                self.load_character()
                
        else:
            self.setup_add_mode()
            self.ui.ad_themphim_chonanh.clicked.connect(self.load_picture)
            self.ui.ad_themphim_them_nhanvat.clicked.connect(self.add_character)
            self.ui.ad_themphim_sua_nhanvat.clicked.connect(self.edit_character)
            self.ui.ad_themphim_xoa_nhanvat.clicked.connect(self.delete_character)
            

        # Kết nối các nút với hàm xử lý
        self.ui.ad_themphim_bang_nhanvat.itemClicked.connect(self.open_link)
        self.ui.ad_themphim_back.clicked.connect(self.back_to_main)

    def get_character(self, movie_detail_id: int):
        """
        Lấy thông tin nhân vật từ API.
        """
        try:
            response = requests.get(f"http://127.0.0.1:8000/api/movie/{movie_detail_id}/character")
            response.raise_for_status()
            character_data = response.json()

            return character_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching character data: {e}")
            return []
        
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
        
    def open_link(self, item):
    # Lấy link từ item theo UserRole
        url = item.data(Qt.ItemDataRole.UserRole)
        if url and url != "N/A":
            QDesktopServices.openUrl(QUrl(url))

    def load_character(self):
        """
        Tải thông tin nhân vật từ API và hiển thị lên giao diện.
        
        """
        movie_detail = self.get_movie_detail(self.movie["id"])
        character_data = self.get_character(movie_detail["id"])
        if character_data:
            # Xử lý dữ liệu nhân vật và hiển thị lên giao diện
            for character in character_data:
                # Ví dụ: in ra tên nhân vật
                print(character.get("name", "N/A"))
        else:
            print("Không có dữ liệu nhân vật.")
        
        self.ui.ad_themphim_bang_nhanvat.setRowCount(len(character_data))

        for row, char in enumerate(character_data):

            #Tên nhân vật và link
            name_link_character = QTableWidgetItem(char.get("name", "N/A"))
            # name_link_character.setForeground(QColor("blue"))
            font = name_link_character.font()
            font.setUnderline(True)
            name_link_character.setFont(font)
            name_link_character.setData(Qt.ItemDataRole.UserRole, char.get("link", "N/A"))

            #Vai trò nhân vật
            role_character = QTableWidgetItem(char.get("role", "N/A"))

            #Tên diễn viên lồng tiếng và link
            name_link_actor = QTableWidgetItem(char.get("voice_actor", "N/A"))
            # name_link_actor.setForeground(QColor("blue"))
            font = name_link_actor.font()
            font.setUnderline(True)
            name_link_actor.setFont(font)
            name_link_actor.setData(Qt.ItemDataRole.UserRole, char.get("voice_actor_link", "N/A"))

            #Quốc tịch diễn viên lồng tiếng
            country_actor = QTableWidgetItem(char.get("voice_actor_country", "N/A"))


            #Thêm các item vào hàng
            self.ui.ad_themphim_bang_nhanvat.setItem(row, 0, name_link_character)
            self.ui.ad_themphim_bang_nhanvat.setItem(row, 1, role_character)
            self.ui.ad_themphim_bang_nhanvat.setItem(row, 2, name_link_actor)
            self.ui.ad_themphim_bang_nhanvat.setItem(row, 3, country_actor)
   
    def setup_detail_mode(self):
        """
        Thiết lập chế độ xem chi tiết phim.
        """
        response = requests.get(f"http://127.0.0.1:8000/api/movies/{self.movie["id"]}/movie-detail")
        response.raise_for_status()
        movie_detail = response.json()
        self.ui.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(379, 1400))

        self.setWindowTitle("Xem chi tiết phim")
        self.ui.ad_themphim_title.setText(self.movie.get("title", "N/A"))
        self.ui.ad_themphim_title.setEnabled(False)

        self.ui.ad_themphim_rank.setText(str(self.movie.get("rank", "N/A")))
        self.ui.ad_themphim_rank.setEnabled(False)

        self.ui.ad_themphim_diem.setText(str(self.movie.get("score", "N/A")))
        self.ui.ad_themphim_diem.setEnabled(False)

        self.ui.ad_themphim_donoitieng.setText(str(movie_detail.get("popularity", "N/A")))
        self.ui.ad_themphim_donoitieng.setEnabled(False)

        self.ui.ad_themphim_nguoitheodoi.setText(str(movie_detail.get("members", "N/A")))
        self.ui.ad_themphim_nguoitheodoi.setEnabled(False)

        self.ui.ad_themphim_sotap.setText(str(self.movie.get("episodes", "N/A")))
        self.ui.ad_themphim_sotap.setEnabled(False)

        self.ui.ad_themphim_yeuthich.setText(str(movie_detail.get("favorites", "N/A")))
        self.ui.ad_themphim_yeuthich.setEnabled(False)

        image_path = r"C:\Users\khoat\Pictures\Save Picture\cropped-SGU-LOGO.png"
        pixmap = QPixmap(image_path)
        self.ui.ad_themphim_anhphim.setPixmap(pixmap)
        self.ui.ad_themphim_anhphim.setScaledContents(True)

        html_content = self.format_movie_detail(movie_detail)


        self.ui.ad_themphim_motaphim.setHtml(html_content)
        self.ui.ad_themphim_motaphim.setEnabled(False)

        self.ui.ad_themphim_otaphim.setHtml(f"""
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html>
            <head>
                <meta name="qrichtext" content="1" />
                <style type="text/css">
                    p, li {{ white-space: pre-wrap; }}
                </style>
            </head>
            <body style="font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:italic;">
                <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                    {movie_detail.get('synopsis', 'N/A')}
                </p>
            </body>
            </html>
            """)
        
        rewiews = self.get_reviews(movie_detail["id"])
        print(rewiews)
        self.load_reviews(rewiews)
        
    def load_reviews(self, reviews, edit = False):
        """
        Tải các bài review của user dựa trên user_id và hiển thị lên bảng ad_themphim_bang_bl.
        """

        # Xóa dữ liệu cũ trên bảng
        self.ui.ad_themphim_bang_bl.setRowCount(len(reviews))


        for row, review in enumerate(reviews):
            
            id = QTableWidgetItem(str(review.get("id", "N/A")))
            id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.ad_themphim_bang_bl.setItem(row, 0, id)
                
            movie_id = QTableWidgetItem(str(review.get("movie_detail_id", "N/A")))
            movie_id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.ad_themphim_bang_bl.setItem(row, 1, movie_id)

            username = QTableWidgetItem(review.get("username", "N/A"))
            movie_id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.ad_themphim_bang_bl.setItem(row, 2, username)

            content = QTableWidgetItem(review.get("show_reviews", "N/A"))
            movie_id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.ui.ad_themphim_bang_bl.setItem(row, 3, content)

        # Tạo nút "Thêm" cho mỗi bài review
            add_button = QPushButton("Thêm")
            add_button.setStyleSheet("background-color: rgb(105, 105, 105); color: rgb(245, 245, 245); font-weight: bold;")
            if edit:
                add_button.setText("Xóa")
                add_button.clicked.connect(self.delete_review)
            else:
                add_button.setText("Xóa")
                add_button.clicked.connect(lambda: QMessageBox.warning(self, "Chế độ chỉnh sửa", "Hãy chuyển qua chế độ chỉnh sửa để thực hiện thao tác này."))
            self.ui.ad_themphim_bang_bl.setCellWidget(row, 4, add_button)
        

    def delete_review(self):
        """
        Xóa bài review của user dựa trên review_id.
        """
        # Lấy dòng hiện tại trong bảng bình luận
        current_row = self.ui.ad_themphim_bang_bl.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một bài review để xóa!")
            return

        # Lấy ID của bài review từ cột đầu tiên
        review_id_item = self.ui.ad_themphim_bang_bl.item(current_row, 0)
        review_id = int(review_id_item.text())
        if not review_id:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy ID của bài review!")
            return

        # Xác nhận xóa
        confirm = QMessageBox.question(
            self,
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa bài review này?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                # Gửi yêu cầu DELETE đến API
                response = requests.delete(f"http://localhost:8000/api/review/{review_id}/delete-review")
                if response.status_code == 200:
                    QMessageBox.information(self, "Thành công", "Xóa bài review thành công!")
                    # Tải lại danh sách review sau khi xóa
                    rewiews = self.get_reviews(self.movie["id"])
                    self.load_reviews(rewiews, edit=True)
                else:
                    QMessageBox.critical(self, "Lỗi", f"Xóa bài review thất bại: {response.json().get('detail', 'Không rõ lỗi')}")
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi xóa bài review: {str(e)}")


    def setup_edit_mode(self):
        # lấy movie detail từ API bằng id 
        
        movie_detail = self.get_movie_detail(self.movie["id"])
        print(movie_detail)
        
        self.ui.change_to_edit_mode(movie_detail, self.get_character(movie_detail["id"]))

        self.ui.ad_themphim_luu.clicked.connect(self.update_movie)

        rewiews = self.get_reviews(movie_detail["id"])
        self.load_reviews(rewiews, edit = True)

    def update_movie(self):
        """
        Lấy dữ liệu từ các trường nhập liệu, kiểm tra và cập nhật thông tin phim.
        """
        # Lấy dữ liệu từ các trường nhập liệu
        movie_detail = self.get_input_movie_detail_edit()
        characters_update = self.get_characters_from_table()
        movie_detail_id = self.get_movie_detail(self.movie["id"])
        if not movie_detail:
            # Nếu dữ liệu không hợp lệ, dừng lại
            return

        # Gửi yêu cầu PUT để cập nhật phim
        try:
            response = requests.put(
                f"http://127.0.0.1:8000/api/movies/{self.movie['id']}/update_movie",
                json=movie_detail.model_dump()
            )
            if response.status_code == 200:
                
                list_char = []
                for name, char in characters_update.items():
                    char["name"] = name
                    list_char.append(char)
                all_characters_added = True
                char_response = requests.put(f"http://localhost:8000/api/movies/{movie_detail_id["id"]}/update-characters", json=list_char)
                if char_response.status_code == 200:
                    print(f"Cập nhật nhân vật cho {self.movie["title"]}")
                else:
                    all_characters_added = False
                    print(f"Cập nhật nhân vật phim {self.movie["title"]} thất bại: {char_response.json()}")

                # Kiểm tra nếu tất cả nhân vật được thêm thành công
                if all_characters_added:
                    QMessageBox.information(self, "Thành công", "Sửa phim và tất cả nhân vật thành công!")
                else:
                    QMessageBox.warning(self, "Cảnh báo", "Sửa phim thành công nhưng một số nhân vật không được thêm.")
                    
            else:
                    QMessageBox.critical(self, "Lỗi", f"Cập nhật phim thất bại: {response.json().get('detail', 'Không rõ lỗi')}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi cập nhật phim: {str(e)}")

    def format_movie_detail(self, movie_detail):
        """
        Định dạng chi tiết phim thành HTML.
        """


        def clean_datatext(data_text):
            """
            Xử lý chuỗi genres để loại bỏ trùng lặp và định dạng lại.
            """
            # Tách chuỗi thành danh sách các phần tử
            data_text_list = data_text.split(",")
            
            # Loại bỏ trùng lặp trong từng phần tử và định dạng lại
            cleaned_data_texts = []
            for data_text in data_text_list:
                # Tách từ, loại bỏ trùng lặp và ghép lại
                unique_words = " ".join(set(data_text.split()))
                cleaned_data_texts.append(unique_words.strip())
            
            # Loại bỏ trùng lặp toàn bộ danh sách và giữ thứ tự
            unique_data_texts = list(dict.fromkeys(cleaned_data_texts))
            
            # Kết hợp lại thành chuỗi
            return ", ".join(unique_data_texts)
        

        formatted_details = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                        line-height: 1.6;
                    }}
                    .detail {{
                        margin-bottom: 10px;
                    }}
                    .label {{
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                <div class="detail"><span class="label">Synonyms:</span> {clean_datatext(movie_detail.get('synonyms', 'N/A'))}</div>
                <div class="detail"><span class="label">Japanese Title:</span> {movie_detail.get('japanese', 'N/A')}</div>
                <div class="detail"><span class="label">Episodes:</span> {movie_detail.get('episodes', 'N/A')}</div>
                <div class="detail"><span class="label">Type:</span> {movie_detail.get('type', 'N/A')}</div>
                <div class="detail"><span class="label">Status:</span> {movie_detail.get('status', 'N/A')}</div>
                <div class="detail"><span class="label">Aired:</span> {movie_detail.get('aired', 'N/A')}</div>
                <div class="detail"><span class="label">Premiered:</span> {movie_detail.get('premiered', 'N/A')}</div>
                <div class="detail"><span class="label">Broadcast:</span> {movie_detail.get('broadcast', 'N/A')}</div>
                <div class="detail"><span class="label">Producers:</span> {movie_detail.get('producers', 'N/A')}</div>
                <div class="detail"><span class="label">Licensors:</span> {movie_detail.get('licensors', 'N/A')}</div>
                <div class="detail"><span class="label">Studios:</span> {movie_detail.get('studios', 'N/A')}</div>
                <div class="detail"><span class="label">Source:</span> {movie_detail.get('source', 'N/A')}</div>
                <div class="detail"><span class="label">Genres:</span> {clean_datatext(movie_detail.get('genres', 'N/A'))}</div>
                <div class="detail"><span class="label">Demographic:</span> {clean_datatext(movie_detail.get('demographic', 'N/A'))}</div>
                <div class="detail"><span class="label">Duration:</span> {movie_detail.get('duration', 'N/A')}</div>
                <div class="detail"><span class="label">Rating:</span> {movie_detail.get('rating', 'N/A')}</div>
            </body>
            </html>
            """
        return formatted_details

    def setup_add_mode(self):
        """
        Thiết lập chế độ thêm mới phim.
        """
        self.ui.change_to_add_mode()
        self.ui.ad_themphim_luu.clicked.connect(self.save_movie)

    def save_movie(self):
        # Lấy thông tin phim từ giao diện
        movie_detail = self.get_input_movie_detail_add()
        characters = self.get_characters_from_table()

        movie_detail_dict = movie_detail.model_dump()
        
        # Gửi yêu cầu POST để thêm phim
        print("Dữ liệu gửi đi:", movie_detail_dict)
        response = requests.post("http://localhost:8000/api/movies/add_movie", json=movie_detail_dict)
        if response.status_code == 200:
            movie_id = response.json().get("id")
            print(f"Thêm phim thành công với ID: {movie_id}")

            # Gửi yêu cầu POST để thêm từng nhân vật
            all_characters_added = True
            for name, character in characters.items():
                character["movie_detail_id"] = movie_id  # Gắn movie_detail_id vào nhân vật
                character["name"] = name  # Thêm trường 'name' vào dữ liệu
                char_response = requests.post(f"http://localhost:8000/api/movies/{movie_id}/add-character", json=character)
                if char_response.status_code == 200:
                    print(f"Thêm nhân vật '{name}' thành công.")
                else:
                    all_characters_added = False
                    print(f"Thêm nhân vật '{name}' thất bại: {char_response.json()}")

            # Kiểm tra nếu tất cả nhân vật được thêm thành công
            if all_characters_added:
                QMessageBox.information(self, "Thành công", "Thêm phim và tất cả nhân vật thành công!")
            else:
                QMessageBox.warning(self, "Cảnh báo", "Thêm phim thành công nhưng một số nhân vật không được thêm.")

            # Xóa dữ liệu trong các trường nhập liệu
            self.clear_fields()

        else:
            print("Thêm phim thất bại")
            print(response.json())
            QMessageBox.critical(self, "Lỗi", "Thêm phim thất bại. Vui lòng kiểm tra lại dữ liệu!")

    def clear_fields(self):
        """
        Xóa dữ liệu trong các trường nhập liệu để chuẩn bị cho lần nhập tiếp theo.
        """
        # Xóa dữ liệu các trường thông tin phim
        self.ui.ad_themphim_title.clear()
        self.ui.ad_themphim_diem.clear()
        self.ui.ad_themphim_rank.clear()
        self.ui.ad_themphim_motaphim_status_input.clear()
        self.ui.ad_themphim_sotap.clear()
        self.ui.ad_themphim_otaphim.clear()
        self.ui.ad_themphim_motaphim_link_input.clear()
        self.ui.ad_themphim_motaphim_synonyms_input.clear()
        self.ui.ad_themphim_motaphim_janpanese_input.clear()
        self.ui.ad_themphim_motaphim_type_input.clear()
        self.ui.ad_themphim_motaphim_aired_input.clear()
        self.ui.ad_themphim_motaphim_premiered_input.clear()
        self.ui.ad_themphim_motaphim_broadcast_input.clear()
        self.ui.ad_themphim_motaphim_producers_input.clear()
        self.ui.ad_themphim_motaphim_licensors_input.clear()
        self.ui.ad_themphim_motaphim_studios_input.clear()
        self.ui.ad_themphim_motaphim_source_input.clear()
        self.ui.ad_themphim_motaphim_genres_input.clear()
        self.ui.ad_themphim_motaphim_demographic_input.clear()
        self.ui.ad_themphim_motaphim_duration_input.clear()
        self.ui.ad_themphim_motaphim_rating_input.clear()
        self.ui.ad_themphim_donoitieng.clear()
        self.ui.ad_themphim_nguoitheodoi.clear()
        self.ui.ad_themphim_yeuthich.clear()

        # Xóa dữ liệu bảng nhân vật
        self.ui.ad_themphim_bang_nhanvat.setRowCount(0)

    def get_input_movie_detail_add(self):
        try:
            # Lấy dữ liệu từ giao diện
            movie_detail = {
                "title": self.ui.ad_themphim_title.text(),
                "score": float(self.ui.ad_themphim_diem.text()) if self.ui.ad_themphim_diem.text() else None,
                "rank": int(self.ui.ad_themphim_rank.text()) if self.ui.ad_themphim_rank.text() else None,
                "status":  self.ui.ad_themphim_motaphim_status_input.text(),
                "episodes": int(self.ui.ad_themphim_sotap.text()) if self.ui.ad_themphim_sotap.text() else None,
                "synopsis": self.ui.ad_themphim_otaphim.toPlainText(),
                "link": self.ui.ad_themphim_motaphim_link_input.text(),
                "synonyms": self.ui.ad_themphim_motaphim_synonyms_input.text(),
                "japanese": self.ui.ad_themphim_motaphim_janpanese_input.text(),
                "type": self.ui.ad_themphim_motaphim_type_input.text(),
                "aired": self.ui.ad_themphim_motaphim_aired_input.text(),
                "premiered": self.ui.ad_themphim_motaphim_premiered_input.text(),
                "broadcast": self.ui.ad_themphim_motaphim_broadcast_input.text(),
                "producers": self.ui.ad_themphim_motaphim_producers_input.text(),
                "licensors": self.ui.ad_themphim_motaphim_licensors_input.text(),
                "studios": self.ui.ad_themphim_motaphim_studios_input.text(),
                "source": self.ui.ad_themphim_motaphim_source_input.text(),
                "genres": self.ui.ad_themphim_motaphim_genres_input.text(),
                "demographic": self.ui.ad_themphim_motaphim_demographic_input.text(),
                "duration": self.ui.ad_themphim_motaphim_duration_input.text(),
                "rating": self.ui.ad_themphim_motaphim_rating_input.text(),
                "popularity": self.ui.ad_themphim_donoitieng.text(),
                "members": self.ui.ad_themphim_nguoitheodoi.text(),
                "favorites": self.ui.ad_themphim_yeuthich.text(),
                "external_id": self.generate_unique_external_id()
            }

            # Kiểm tra dữ liệu với schema MovieIn
            validated_movie = MovieIn(**movie_detail)
            return validated_movie

        except ValidationError as e:
            # Hiển thị thông báo lỗi cho người dùng
            error_messages = "\n".join([f"{err['loc'][0]}: {err['msg']}" for err in e.errors()])
            QMessageBox.warning(self, "Lỗi nhập liệu", f"Dữ liệu không hợp lệ:\n{error_messages}")
            return None
        except ValueError as e:
            # Xử lý lỗi chuyển đổi kiểu dữ liệu (nếu có)
            QMessageBox.warning(self, "Lỗi nhập liệu", f"Lỗi chuyển đổi dữ liệu: {str(e)}")
            return None
        
    def get_input_movie_detail_edit(self):
        try:
            
            # Lấy dữ liệu từ giao diện
            movie_detail = {
                "title": self.ui.ad_themphim_title.text(),
                "score": float(self.ui.ad_themphim_diem.text()) if self.ui.ad_themphim_diem.text() else None,
                "rank": int(self.ui.ad_themphim_rank.text()) if self.ui.ad_themphim_rank.text() else None,
                "status":  self.ui.ad_themphim_motaphim_status_input.text(),
                "episodes": int(self.ui.ad_themphim_sotap.text()) if self.ui.ad_themphim_sotap.text() else None,
                "synopsis": self.ui.ad_themphim_otaphim.toPlainText(),
                "link": self.ui.ad_themphim_motaphim_link_input.text(),
                "synonyms": self.ui.ad_themphim_motaphim_synonyms_input.text(),
                "japanese": self.ui.ad_themphim_motaphim_janpanese_input.text(),
                "type": self.ui.ad_themphim_motaphim_type_input.text(),
                "aired": self.ui.ad_themphim_motaphim_aired_input.text(),
                "premiered": self.ui.ad_themphim_motaphim_premiered_input.text(),
                "broadcast": self.ui.ad_themphim_motaphim_broadcast_input.text(),
                "producers": self.ui.ad_themphim_motaphim_producers_input.text(),
                "licensors": self.ui.ad_themphim_motaphim_licensors_input.text(),
                "studios": self.ui.ad_themphim_motaphim_studios_input.text(),
                "source": self.ui.ad_themphim_motaphim_source_input.text(),
                "genres": self.ui.ad_themphim_motaphim_genres_input.text(),
                "demographic": self.ui.ad_themphim_motaphim_demographic_input.text(),
                "duration": self.ui.ad_themphim_motaphim_duration_input.text(),
                "rating": self.ui.ad_themphim_motaphim_rating_input.text(),
                "popularity": self.ui.ad_themphim_donoitieng.text(),
                "members": self.ui.ad_themphim_nguoitheodoi.text(),
                "favorites": self.ui.ad_themphim_yeuthich.text(),
                "external_id": self.movie["external_id"]
            }

            # Kiểm tra dữ liệu với schema MovieIn
            validated_movie = MovieIn(**movie_detail)
            return validated_movie

        except ValidationError as e:
            # Hiển thị thông báo lỗi cho người dùng
            error_messages = "\n".join([f"{err['loc'][0]}: {err['msg']}" for err in e.errors()])
            QMessageBox.warning(self, "Lỗi nhập liệu", f"Dữ liệu không hợp lệ:\n{error_messages}")
            return None
        except ValueError as e:
            # Xử lý lỗi chuyển đổi kiểu dữ liệu (nếu có)
            QMessageBox.warning(self, "Lỗi nhập liệu", f"Lỗi chuyển đổi dữ liệu: {str(e)}")
            return None
        
    # Hàm generate ra external_id
    def generate_unique_external_id(self):
        """
        Tạo một external_id duy nhất (kiểu int) không trùng với bất kỳ movie nào trong cơ sở dữ liệu.
        """
        # Lấy danh sách tất cả các phim
        movies = self.get_movies()

        # Trích xuất tất cả các external_id từ danh sách phim
        existing_external_ids = [movie.get("external_id") for movie in movies if "external_id" in movie]

        # Tìm external_id lớn nhất hiện có
        max_external_id = max(existing_external_ids, default=0)

        # Sinh external_id mới (lớn hơn giá trị lớn nhất hiện có)
        return max_external_id + 1

    def get_characters_from_table(self):
        """
        Lấy dữ liệu từ bảng ad_themphim_bang_nhanvat và trả về một dictionary các đối tượng character.
        """
        characters = {}

        # Duyệt qua từng dòng trong bảng
        row_count = self.ui.ad_themphim_bang_nhanvat.rowCount()
        for row in range(row_count):
            # Lấy dữ liệu từ từng cột
            name_item = self.ui.ad_themphim_bang_nhanvat.item(row, 0)
            role_item = self.ui.ad_themphim_bang_nhanvat.item(row, 1)
            voice_actor_item = self.ui.ad_themphim_bang_nhanvat.item(row, 2)
            voice_actor_country_item = self.ui.ad_themphim_bang_nhanvat.item(row, 3)

            # Lấy text và link từ cột name
            name = name_item.text() if name_item else "N/A"
            link = name_item.data(Qt.ItemDataRole.UserRole)[0] if name_item and name_item.data(Qt.ItemDataRole.UserRole) else "N/A"

            # Lấy text từ cột role
            role = role_item.text() if role_item else "N/A"

            # Lấy text và link từ cột voice_actor
            voice_actor = voice_actor_item.text() if voice_actor_item else "N/A"
            voice_actor_link = voice_actor_item.data(Qt.ItemDataRole.UserRole)[0] if voice_actor_item and voice_actor_item.data(Qt.ItemDataRole.UserRole) else "N/A"

            # Lấy text từ cột voice_actor_country
            voice_actor_country = voice_actor_country_item.text() if voice_actor_country_item else "N/A"

            # Tạo đối tượng character
            character = {
                "role": role,
                "link": link,
                "voice_actor": voice_actor,
                "voice_actor_link": voice_actor_link,
                "voice_actor_country": voice_actor_country
            }

            # Thêm vào dictionary với key là tên nhân vật
            characters[name] = character

        return characters

    def add_character(self):
        # Tạo cửa sổ nhập thông tin nhân vật
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Thêm Nhân Vật")
        dialog.setFixedSize(400, 400)

        layout = QtWidgets.QVBoxLayout(dialog)

        # Các trường nhập liệu
        name_label = QtWidgets.QLabel("Tên nhân vật:")
        name_input = QtWidgets.QLineEdit()
        role_label = QtWidgets.QLabel("Vai trò:")
        role_input = QtWidgets.QLineEdit()
        link_label = QtWidgets.QLabel("Link:")
        link_input = QtWidgets.QLineEdit()
        voice_actor_label = QtWidgets.QLabel("Diễn viên lồng tiếng:")
        voice_actor_input = QtWidgets.QLineEdit()
        voice_actor_link_label = QtWidgets.QLabel("Link diễn viên:")
        voice_actor_link_input = QtWidgets.QLineEdit()
        voice_actor_country_label = QtWidgets.QLabel("Quốc tịch diễn viên:")
        voice_actor_country_input = QtWidgets.QLineEdit()

        # Nút Lưu và Hủy
        save_button = QtWidgets.QPushButton("Lưu")
        cancel_button = QtWidgets.QPushButton("Hủy")

        # Thêm các widget vào layout
        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(role_label)
        layout.addWidget(role_input)
        layout.addWidget(link_label)
        layout.addWidget(link_input)
        layout.addWidget(voice_actor_label)
        layout.addWidget(voice_actor_input)
        layout.addWidget(voice_actor_link_label)
        layout.addWidget(voice_actor_link_input)
        layout.addWidget(voice_actor_country_label)
        layout.addWidget(voice_actor_country_input)
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)

        # Xử lý sự kiện nút Hủy
        cancel_button.clicked.connect(dialog.reject)

        # Xử lý sự kiện nút Lưu
        def save_character():
            # Lấy dữ liệu từ các trường nhập liệu
            name = name_input.text().strip()
            role = role_input.text().strip()
            link = link_input.text().strip()
            voice_actor = voice_actor_input.text().strip()
            voice_actor_link = voice_actor_link_input.text().strip()
            voice_actor_country = voice_actor_country_input.text().strip()

            # Kiểm tra dữ liệu
            if not name or not role or not link or not voice_actor or not voice_actor_link or not voice_actor_country:
                QtWidgets.QMessageBox.warning(dialog, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                return
            
            print("name:" + name)
            print("role:" + role)
            print("link:" + link)
            print("voice_actor:" + voice_actor)
            print("voice_actor_link:" + voice_actor_link)
            print("voice_actor_country:" + voice_actor_country)

            name_link_character = QTableWidgetItem(name)
            font = name_link_character.font()
            font.setUnderline(True)
            name_link_character.setFont(font)
            name_link_character.setData(Qt.ItemDataRole.UserRole, (link, "N/A"))

            name_link_actor = QTableWidgetItem(voice_actor)
            font = name_link_actor.font()
            font.setUnderline(True)
            name_link_actor.setFont(font)
            name_link_actor.setData(Qt.ItemDataRole.UserRole, (voice_actor_link, "N/A"))

            # Thêm dữ liệu vào bảng
            row_position = self.ui.ad_themphim_bang_nhanvat.rowCount()

            

            self.ui.ad_themphim_bang_nhanvat.insertRow(row_position)
            self.ui.ad_themphim_bang_nhanvat.setItem(row_position, 0, name_link_character)
            self.ui.ad_themphim_bang_nhanvat.setItem(row_position, 1, QtWidgets.QTableWidgetItem(role))
            self.ui.ad_themphim_bang_nhanvat.setItem(row_position, 2, name_link_actor)
            self.ui.ad_themphim_bang_nhanvat.setItem(row_position, 3, QtWidgets.QTableWidgetItem(voice_actor_country))

            dialog.accept()

        save_button.clicked.connect(save_character)

        # Hiển thị cửa sổ
        dialog.exec()

    def edit_character(self):
        # Lấy dòng được chọn
        selected_row = self.ui.ad_themphim_bang_nhanvat.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Vui lòng chọn một nhân vật để sửa!")
            return

        # Tạo cửa sổ chỉnh sửa
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Sửa Nhân Vật")
        dialog.setFixedSize(400, 400)

        layout = QtWidgets.QVBoxLayout(dialog)

        # Các trường nhập liệu
        name_item = self.ui.ad_themphim_bang_nhanvat.item(selected_row, 0)
        name_label = QtWidgets.QLabel("Tên nhân vật:")
        name_input = QtWidgets.QLineEdit(name_item.text())
        role_label = QtWidgets.QLabel("Vai trò:")
        role_input = QtWidgets.QLineEdit(self.ui.ad_themphim_bang_nhanvat.item(selected_row, 1).text())
        link_label = QtWidgets.QLabel("Link:")
        link_data = name_item.data(Qt.ItemDataRole.UserRole)
        if isinstance(link_data, tuple):
            link_data = link_data[0]
        link_input = QtWidgets.QLineEdit(link_data)

        voice_actor_item = self.ui.ad_themphim_bang_nhanvat.item(selected_row, 2)
        voice_actor_label = QtWidgets.QLabel("Diễn viên lồng tiếng:")
        voice_actor_input = QtWidgets.QLineEdit(voice_actor_item.text())
        voice_actor_link_label = QtWidgets.QLabel("Link diễn viên:")
        voice_actor_link_data = voice_actor_item.data(Qt.ItemDataRole.UserRole)
        if isinstance(voice_actor_link_data, tuple):
            voice_actor_link_data = voice_actor_link_data[0]
        voice_actor_link_input = QtWidgets.QLineEdit(voice_actor_link_data)
        voice_actor_country_label = QtWidgets.QLabel("Quốc tịch diễn viên:")
        voice_actor_country_input = QtWidgets.QLineEdit(self.ui.ad_themphim_bang_nhanvat.item(selected_row, 3).text())

        # Nút Lưu và Hủy
        save_button = QtWidgets.QPushButton("Lưu")
        cancel_button = QtWidgets.QPushButton("Hủy")

        # Thêm các widget vào layout
        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(role_label)
        layout.addWidget(role_input)
        layout.addWidget(link_label)
        layout.addWidget(link_input)
        layout.addWidget(voice_actor_label)
        layout.addWidget(voice_actor_input)
        layout.addWidget(voice_actor_link_label)
        layout.addWidget(voice_actor_link_input)
        layout.addWidget(voice_actor_country_label)
        layout.addWidget(voice_actor_country_input)
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)

        # Xử lý sự kiện nút Hủy
        cancel_button.clicked.connect(dialog.reject)

        # Xử lý sự kiện nút Lưu
        def save_character():
            # Lấy dữ liệu từ các trường nhập liệu
            name = name_input.text().strip()
            role = role_input.text().strip()
            link = link_input.text().strip()
            voice_actor = voice_actor_input.text().strip()
            voice_actor_link = voice_actor_link_input.text().strip()
            voice_actor_country = voice_actor_country_input.text().strip()

            # Kiểm tra dữ liệu
            if not name or not role or not link or not voice_actor or not voice_actor_link or not voice_actor_country:
                QtWidgets.QMessageBox.warning(dialog, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                return
            
            name_link_character = QTableWidgetItem(name)
            font = name_link_character.font()
            font.setUnderline(True)
            name_link_character.setFont(font)
            name_link_character.setData(Qt.ItemDataRole.UserRole, (link, "N/A"))

            name_link_actor = QTableWidgetItem(voice_actor)
            font = name_link_actor.font()
            font.setUnderline(True)
            name_link_actor.setFont(font)
            name_link_actor.setData(Qt.ItemDataRole.UserRole, (voice_actor_link, "N/A"))

            # Cập nhật dữ liệu trong bảng
            self.ui.ad_themphim_bang_nhanvat.setItem(selected_row, 0, QtWidgets.QTableWidgetItem(name_link_character))
            self.ui.ad_themphim_bang_nhanvat.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(role))
            self.ui.ad_themphim_bang_nhanvat.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(name_link_actor))
            self.ui.ad_themphim_bang_nhanvat.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(link))

            dialog.accept()

        save_button.clicked.connect(save_character)

        # Hiển thị cửa sổ
        dialog.exec()

    def delete_character(self):
    # Lấy dòng được chọn
        selected_row = self.ui.ad_themphim_bang_nhanvat.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Vui lòng chọn một nhân vật để xóa!")
            return

        # Xác nhận xóa
        confirm = QtWidgets.QMessageBox.question(
            None, "Xác nhận", "Bạn có chắc chắn muốn xóa nhân vật này?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            self.ui.ad_themphim_bang_nhanvat.removeRow(selected_row)

    def load_picture(self):
        """
        Tải hình ảnh từ máy tính và hiển thị lên giao diện.
        """
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                pixmap = QPixmap(image_path)
                self.ui.ad_themphim_anhphim.setPixmap(pixmap)
                self.ui.ad_themphim_anhphim.setScaledContents(True)
        
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
    window = AdminManagerFilm()
    window.show()
    sys.exit(app.exec())