import datetime
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QDate
from requests import get
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from frontend.views.admin.ad_nguoidung import Ui_ad_tranguser

class AdNguoiDung(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ad_tranguser()
        self.ui.setupUi(self)
        
        

        # Set up the UI components
    
        self.ui.ad_tranguser_back.clicked.connect(self.back_to_main)
        self.ui.ad_tranguser_luu.clicked.connect(self.update_user)
        self.ui.ad_tranguser_xoa.clicked.connect(self.delete_user)
        self.ui.ad_tranguser_them.clicked.connect(self.add_user)
        self.ui.ad_tranguser_sua.clicked.connect(self.edit_user)
        self.ui.ad_tranguser_nuttimkiem.clicked.connect(self.tim_kiem_user)
        self.ui.ad_tranguser_banguser.cellClicked.connect(self.load_reviews)

        self.load_user(self.get_user())

    def get_user(self):
        try:
            response = requests.get("http://127.0.0.1:8000/api/user/user-list")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            return data
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch data: {e}")
            return []
        
    def get_reviews_by_userID(self, user_id):
        try:
            response = requests.get("http://127.0.0.1:8000/api/user/user-list")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            return data
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch data: {e}")
            return []
        
        
    def load_user(self, user_data):
        user_data = sorted(user_data, key=lambda x: x.get("id", 0))
        self.ui.ad_tranguser_banguser.setRowCount(len(user_data))
        
        for row, user in enumerate(user_data):
            # Tạo widget chứa 2 nút


            detail_button = QPushButton("Xem chi tiết")
            detail_button.setStyleSheet("background-color: rgb(105 105 105); color: rgb(245 245 245); font-weight: bold;")
            detail_button.clicked.connect(self.show_details)

            self.ui.ad_tranguser_banguser.setItem(row, 0, QTableWidgetItem(str(user.get("id", ""))))
            self.ui.ad_tranguser_banguser.setItem(row, 1, QTableWidgetItem(user.get("username", "")))
            self.ui.ad_tranguser_banguser.setItem(row, 2, QTableWidgetItem(user.get("date_of_birth", "")))
            self.ui.ad_tranguser_banguser.setItem(row, 3, QTableWidgetItem(self.check_role(int(user.get("role", "")))))
            self.ui.ad_tranguser_banguser.setItem(row, 4, QTableWidgetItem(self.check_status(user.get("status", "false"))))
            self.ui.ad_tranguser_banguser.setCellWidget(row, 5, detail_button)

    def load_reviews(self):
        
        """
        Tải các bài review của user dựa trên user_id và hiển thị lên bảng ad_nguoidung_baiviet.
        """
        selected_row = self.ui.ad_tranguser_banguser.currentRow()

        self.ui.chublogphim_12.setText(self.ui.ad_tranguser_banguser.item(selected_row, 1).text())
        self.ui.chublogphim_13.setText(self.ui.ad_tranguser_banguser.item(selected_row, 2).text())
        self.ui.chublogphim_14.setText(self.ui.ad_tranguser_banguser.item(selected_row, 3).text())
        self.ui.chublogphim_15.setText(self.ui.ad_tranguser_banguser.item(selected_row, 4).text())
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để xem chi tiết!")
            return
        
        user_id = int(self.ui.ad_tranguser_banguser.item(selected_row, 0).text())

        try:
            # Gửi yêu cầu GET đến API để lấy danh sách review của user
            response = requests.get(f"http://localhost:8000/api/review/{user_id}/review-by-user")
            response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP

            # Lấy dữ liệu JSON từ phản hồi
            reviews = response.json()

            # Xóa dữ liệu cũ trên bảng
            self.ui.ad_nguoidung_baiviet.setColumnCount(3)
            self.ui.ad_nguoidung_baiviet.setRowCount(0)

            # Duyệt qua danh sách review và thêm vào bảng
            for row, review in enumerate(reviews):
                self.ui.ad_nguoidung_baiviet.setRowCount(len(reviews))

                id = QTableWidgetItem(str(review.get("id", "N/A")))
                id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                
                
                movie_id = QTableWidgetItem(str(review.get("movie_detail_id", "N/A")))
                movie_id.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                

                # Thêm nội dung review
                content_item = QTableWidgetItem(review.get("show_reviews", "N/A"))
                content_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                

                self.ui.ad_nguoidung_baiviet.setItem(row, 0, id)
                self.ui.ad_nguoidung_baiviet.setItem(row, 1, movie_id)
                self.ui.ad_nguoidung_baiviet.setItem(row, 2, content_item)


        except requests.exceptions.RequestException as e:
            # Hiển thị thông báo lỗi nếu không thể tải dữ liệu
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách review: {e}")

    def tim_kiem_user(self):
        search_text = self.ui.ad_tranguser_thanhtimkiem.text()
        if search_text:
            filtered_data = [user for user in self.get_user() if search_text.lower() in user.get("username", "").lower() or search_text.lower() in str(user.get("id", ""))]
            self.load_user(filtered_data)
            self.clear_fileds()
        else:
            self.load_user(self.get_user())
            self.clear_fileds()

    def check_status(self, status):
        if status:
            return "Đang hoạt động"
        else:
            return "Đã khóa"
            
    def check_role(self, role):
        if role == 0:
            return "Người dùng"
        elif role == 1:
            return "Quản trị viên"
        else:
            return "Khách hàng"
        
    def clear_fileds(self):
        """Xóa nội dung các trường tìm kiếm"""
        self.ui.ad_tranguser_thanhtimkiem.clear()

    def back_to_main(self):
        """Quay lại trang chính"""
        from frontend.views.admin.ad_trangchu_logic import AdminTrangChu
        self.close()
        self.main_window = AdminTrangChu()
        self.main_window.show() 
    
    def update_user(self):
        print("Update user information")
        
    def delete_user(self):
        # Lấy dòng được chọn
        selected_row = self.ui.ad_tranguser_banguser.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để xóa!")
            return

        # Lấy thông tin ID của người dùng từ dòng được chọn
        user_id = self.ui.ad_tranguser_banguser.item(selected_row, 0).text()

        # Hiển thị hộp thoại xác nhận
        confirm = QMessageBox.question(
            self,
            "Xác nhận xóa",
            "Bạn có chắc chắn muốn xóa người dùng này không? User sẽ bị xóa khỏi cơ sở dữ liệu!",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                # Gửi yêu cầu xóa đến API
                response = requests.delete(f"http://127.0.0.1:8000/api/user/{user_id}")
                response.raise_for_status()

                # Xóa dòng khỏi bảng
                self.ui.ad_tranguser_banguser.removeRow(selected_row)

                QMessageBox.information(self, "Thành công", "Người dùng đã được xóa!")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể xóa người dùng: {e}")

    def add_user(self):
        class AddUserDialog(QDialog):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Thêm người dùng")
                self.setFixedSize(400, 300)
                
                # Biến tạm để lưu dữ liệu
                self.user_data = {}
                
                # Thiết lập giao diện
                self.setup_ui()
                
            def setup_ui(self):
                layout = QVBoxLayout()
                
                # Tên tài khoản
                self.username_label = QLabel("Tên tài khoản (*):")
                self.username_input = QLineEdit()
                layout.addWidget(self.username_label)
                layout.addWidget(self.username_input)
                
                # Mật khẩu
                self.password_label = QLabel("Mật khẩu (*):")
                self.password_input = QLineEdit()
                self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
                layout.addWidget(self.password_label)
                layout.addWidget(self.password_input)
                
                # Ngày sinh
                self.dob_label = QLabel("Ngày sinh (dd/MM/yyyy):")
                self.dob_input = QDateEdit()
                self.dob_input.setDisplayFormat("dd/MM/yyyy")
                self.dob_input.setDate(QDate.currentDate())
                self.dob_input.setCalendarPopup(True)
                layout.addWidget(self.dob_label)
                layout.addWidget(self.dob_input)
                
                # Vai trò
                self.role_label = QLabel("Vai trò (*):")
                self.role_input = QComboBox()
                self.role_input.addItems(["Người dùng", "Quản trị viên"])
                layout.addWidget(self.role_label)
                layout.addWidget(self.role_input)
                
                # Nút Hủy và Lưu
                button_layout = QHBoxLayout()
                self.cancel_button = QPushButton("Hủy")
                self.save_button = QPushButton("Lưu")
                button_layout.addWidget(self.cancel_button)
                button_layout.addWidget(self.save_button)
                layout.addLayout(button_layout)
                
                self.setLayout(layout)
                
                # Kết nối sự kiện
                self.cancel_button.clicked.connect(self.reject)
                self.save_button.clicked.connect(self.save_data)
                
            def save_data(self):
                username = self.username_input.text().strip()
                password = self.password_input.text().strip()
                dob = self.dob_input.date().toString("dd-MM-yyyy")
                role = 0 if self.role_input.currentText() == "Người dùng" else 1
                
                # Kiểm tra dữ liệu bắt buộc
                if not username:
                    QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên tài khoản!")
                    return
                if not password:
                    QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mật khẩu!")
                    return
                
                # Lưu dữ liệu vào user_data
                self.user_data = {
                    "username": username,
                    "password": password,
                    "date_of_birth": dob,
                    "role": role,
                    "status": True  # Mặc định trạng thái là "Đang hoạt động"
                }
                self.accept()

        # Hiển thị hộp thoại thêm người dùng
        dialog = AddUserDialog(self)
        if dialog.exec():
            new_user = dialog.user_data
            print("Dữ liệu thêm:", new_user)

            # Gửi yêu cầu thêm người dùng đến API
            try:
                response = requests.post("http://127.0.0.1:8000/api/signup", json=new_user)
                response.raise_for_status()

                QMessageBox.information(self, "Thành công", "Người dùng đã được thêm thành công!")
                self.load_user(self.get_user())  # Tải lại danh sách người dùng
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể thêm người dùng: {e}")
        
    def edit_user(self):
        selected_row = self.ui.ad_tranguser_banguser.currentRow()
        if selected_row == -1:
           QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để sửa!")
           return

        # Lấy thông tin từ dòng đã chọn
        user_id = self.ui.ad_tranguser_banguser.item(selected_row, 0).text()
        username = self.ui.ad_tranguser_banguser.item(selected_row, 1).text()
        date_of_birth = self.ui.ad_tranguser_banguser.item(selected_row, 2).text()
        role = self.ui.ad_tranguser_banguser.item(selected_row, 3).text()
        status = self.ui.ad_tranguser_banguser.item(selected_row, 4).text()

        # Chuyển đổi vai trò và trạng thái
        role_index = 0 if role == "Người dùng" else 1
        status_index = 0 if status == "Đã khóa" else 1


       # Tạo cửa sổ chỉnh sửa
        class EditUserDialog(QDialog):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle("Sửa thông tin người dùng")
                self.setFixedSize(400, 300)

                 # Biến tạm để lưu dữ liệu
                self.user_data = {}

                 # Thiết lập giao diện
                self.setup_ui()
            def setup_ui(self):
                layout = QVBoxLayout()

                # ID (không chỉnh sửa)
                self.id_label = QLabel("ID:")
                self.id_display = QLabel(user_id)
                layout.addWidget(self.id_label)
                layout.addWidget(self.id_display)

                # Tên tài khoản
                self.username_label = QLabel("Tên tài khoản (*):")
                self.username_input = QLineEdit(username)
                self.username_input.setEnabled(False)
                layout.addWidget(self.username_label)
                layout.addWidget(self.username_input)

                # Ngày sinh
                self.dob_label = QLabel("Ngày sinh (dd/MM/yyyy):")
                self.dob_input = QDateEdit()
                self.dob_input.setDisplayFormat("dd/MM/yyyy")
                self.dob_input.setDate(QDate.fromString(date_of_birth, "dd/MM/yyyy"))
                self.dob_input.setCalendarPopup(True)
                layout.addWidget(self.dob_label)
                layout.addWidget(self.dob_input)

                # Vai trò
                self.role_label = QLabel("Vai trò (*):")
                self.role_input = QComboBox()
                self.role_input.addItems(["Người dùng", "Quản trị viên"])
                self.role_input.setCurrentIndex(role_index)
                layout.addWidget(self.role_label)
                layout.addWidget(self.role_input)

                # Trạng thái
                self.status_label = QLabel("Trạng thái:")
                self.status_input = QComboBox()
                self.status_input.addItems(["Đã khóa", "Đang hoạt động"])
                self.status_input.setCurrentIndex(status_index)
                layout.addWidget(self.status_label)
                layout.addWidget(self.status_input)

                # Nút Hủy và Lưu
                button_layout = QHBoxLayout()
                self.cancel_button = QPushButton("Hủy")
                self.save_button = QPushButton("Lưu")
                button_layout.addWidget(self.cancel_button)
                button_layout.addWidget(self.save_button)
                layout.addLayout(button_layout)

                self.setLayout(layout)

                # Kết nối sự kiện
                self.cancel_button.clicked.connect(self.reject)
                self.save_button.clicked.connect(self.save_data)

            def save_data(self):
                username = self.username_input.text().strip()
                dob = self.dob_input.date().toString("dd-MM-yyyy")
                role = 0 if self.role_input.currentText() == "Người dùng" else 1
                status = self.status_input.currentText() == "Đang hoạt động"

                # Kiểm tra dữ liệu bắt buộc
                if not username:
                    QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên tài khoản!")
                    return

                # Lưu dữ liệu vào user_data
                self.user_data = {
                    "id": int(user_id),
                    "username": username,
                    "date_of_birth": dob,
                    "status": status,
                    "role": role
            }

                QMessageBox.information(self, "Thành công", "Dữ liệu đã được cập nhật!")
                self.accept()

        # Hiển thị hộp thoại chỉnh sửa
        dialog = EditUserDialog(self)
        if dialog.exec():
            updated_user = dialog.user_data
        

            print("Dữ liệu đã chỉnh sửa:", updated_user)

            # Gửi dữ liệu cập nhật về server
            try:
                response = requests.put(
                    f"http://127.0.0.1:8000/api/user/{user_id}/update",
                    json=updated_user
                )
                response.raise_for_status()
                QMessageBox.information(self, "Thành công", "Thông tin người dùng đã được cập nhật!")
                self.load_user(self.get_user())  # Tải lại danh sách người dùng
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể cập nhật thông tin: {e}")

    def show_details(self):
        # Lấy dòng được chọn
        selected_row = self.ui.ad_tranguser_banguser.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để xem chi tiết!")
            return

        # Lấy thông tin từ dòng đã chọn
        user_id = self.ui.ad_tranguser_banguser.item(selected_row, 0).text()
        username = self.ui.ad_tranguser_banguser.item(selected_row, 1).text()
        date_of_birth = self.ui.ad_tranguser_banguser.item(selected_row, 2).text()
        role = self.ui.ad_tranguser_banguser.item(selected_row, 3).text()
        status = self.ui.ad_tranguser_banguser.item(selected_row, 4).text()

        # Đóng gói thông tin thành một dictionary kiểu user
        user = {
            "id": user_id,
            "username": username,
            "date_of_birth": date_of_birth,
            "role": role,
            "status": 1 if status == "Đang hoạt động" else 0
        }

        # Mở giao diện trang cá nhân với tham số user
        from frontend.views.admin.ad_trangcanhan_logic import AdminTrangcanhanFilm
        
        self.personal_page = AdminTrangcanhanFilm(user=user)
        self.personal_page.set_up_details()  # Thiết lập thông tin chi tiết
        self.personal_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdNguoiDung()
    window.show()
    sys.exit(app.exec())