from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView

class Ui_ad_tranguser(object):
    def setupUi(self, ad_tranguser):
        ad_tranguser.setObjectName("ad_tranguser")
        ad_tranguser.resize(1898, 1595)
        ad_tranguser.setStyleSheet("background-color: rgb(91, 91, 91);")

        self.centralwidget = QtWidgets.QWidget(parent=ad_tranguser)
        self.centralwidget.setObjectName("centralwidget")
        ad_tranguser.setCentralWidget(self.centralwidget)

        # Main layout for central widget
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Header (ad_tranguser_thanhcc)
        self.ad_tranguser_thanhcc = QtWidgets.QWidget()
        self.ad_tranguser_thanhcc.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.ad_tranguser_thanhcc.setFixedHeight(100)
        header_layout = QtWidgets.QHBoxLayout(self.ad_tranguser_thanhcc)

        self.ad_tranguser_homthu = QtWidgets.QListWidget()
        self.ad_tranguser_homthu.setFixedSize(100, 60)
        self.ad_tranguser_homthu.setStyleSheet("background-color: rgb(163, 163, 163);")
        self.ad_tranguser_homthu.addItem("Yêu cầu 1")
        self.ad_tranguser_homthu.addItem("Yêu cầu 2")
        header_layout.addWidget(self.ad_tranguser_homthu)

        self.chublogphim = QtWidgets.QLabel("ADMIN")
        font = QtGui.QFont("Colonna MT", 102, QtGui.QFont.Weight.Bold)
        font.setItalic(True)
        self.chublogphim.setFont(font)
        self.chublogphim.setStyleSheet("color: white;")
        header_layout.addWidget(self.chublogphim)

        header_layout.addStretch()

        self.ad_tranguser_thanhtimkiem = QtWidgets.QLineEdit()
        self.ad_tranguser_thanhtimkiem.setFixedWidth(300)
        self.ad_tranguser_thanhtimkiem.setStyleSheet("background-color: rgb(144, 144, 144); color: white;")
        header_layout.addWidget(self.ad_tranguser_thanhtimkiem)

        self.ad_tranguser_nuttimkiem = QtWidgets.QPushButton("TÌM KIẾM")
        self.ad_tranguser_nuttimkiem.setFixedWidth(100)
        self.ad_tranguser_nuttimkiem.setStyleSheet("background-color: rgb(24, 24, 24); color: rgb(230, 230, 230);")
        header_layout.addWidget(self.ad_tranguser_nuttimkiem)

        # Nút TRANG CHỦ và LƯU xếp dọc
        button_layout = QtWidgets.QVBoxLayout()
        self.ad_tranguser_back = QtWidgets.QPushButton("TRANG CHỦ")
        self.ad_tranguser_back.setFixedWidth(100)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ad_tranguser_back.setFont(font)
        self.ad_tranguser_back.setStyleSheet("background-color: rgb(223, 223, 223);")
        button_layout.addWidget(self.ad_tranguser_back)

        self.ad_tranguser_luu = QtWidgets.QPushButton("LƯU")
        self.ad_tranguser_luu.setFixedWidth(100)
        self.ad_tranguser_luu.setFont(font)
        self.ad_tranguser_luu.setStyleSheet("background-color: rgb(223, 223, 223);")
        button_layout.addWidget(self.ad_tranguser_luu)
        header_layout.addLayout(button_layout)

        main_layout.addWidget(self.ad_tranguser_thanhcc)

        # Main ScrollArea containing user info and user table
        self.main_scroll_area = QtWidgets.QScrollArea()
        self.main_scroll_area.setWidgetResizable(True)
        self.main_scroll_area.setStyleSheet("background-color: rgb(91, 91, 91);")
        main_scroll_content = QtWidgets.QWidget()
        self.main_scroll_area.setWidget(main_scroll_content)
        main_scroll_layout = QtWidgets.QHBoxLayout(main_scroll_content)
        main_scroll_layout.setContentsMargins(0, 0, 0, 0)
        main_scroll_layout.setSpacing(10)
        main_layout.addWidget(self.main_scroll_area)

        # ScrollArea for user info (widget)
        self.user_info_scroll_area = QtWidgets.QScrollArea()
        self.user_info_scroll_area.setWidgetResizable(True)
        self.user_info_scroll_area.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.user_info_scroll_area.setFixedWidth(480)  # 2/5 of 1200px
        self.widget = QtWidgets.QWidget()
        self.user_info_scroll_area.setWidget(self.widget)
        user_info_layout = QtWidgets.QVBoxLayout(self.widget)
        user_info_layout.setContentsMargins(10, 10, 10, 10)
        main_scroll_layout.addWidget(self.user_info_scroll_area)

        # Horizontal layout for avatar and info
        info_layout = QtWidgets.QHBoxLayout()

        # Avatar
        self.ad_tranguser_avt = QtWidgets.QLabel("AVATAR")
        self.ad_tranguser_avt.setFixedSize(160, 190)
        self.ad_tranguser_avt.setStyleSheet("background-color: rgb(255, 255, 255);")
        info_layout.addWidget(self.ad_tranguser_avt)

        # Vertical layout for info labels
        info_labels_layout = QtWidgets.QVBoxLayout()
        self.chublogphim_6 = QtWidgets.QLabel("THÔNG TIN CÁ NHÂN:")
        font = QtGui.QFont("MS Shell Dlg 2", 16, QtGui.QFont.Weight.Bold)
        self.chublogphim_6.setFont(font)
        self.chublogphim_6.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.chublogphim_6)

        self.chublogphim_2 = QtWidgets.QLabel("TÊN TÀI KHOẢN:")
        font = QtGui.QFont("MS Shell Dlg 2", 9)
        self.chublogphim_2.setFont(font)
        self.chublogphim_2.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.chublogphim_2)

        self.chublogphim_12 = QtWidgets.QLabel("")
        self.chublogphim_12.setFont(font)
        self.chublogphim_12.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_12)

        self.chublogphim_3 = QtWidgets.QLabel("NGÀY SINH")
        self.chublogphim_3.setFont(font)
        self.chublogphim_3.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.chublogphim_3)

        self.chublogphim_13 = QtWidgets.QLabel("")
        self.chublogphim_13.setFont(font)
        self.chublogphim_13.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_13)

        self.chublogphim_4 = QtWidgets.QLabel("VAI TRÒ:")
        self.chublogphim_4.setFont(font)
        self.chublogphim_4.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.chublogphim_4)

        self.chublogphim_14 = QtWidgets.QLabel("")
        self.chublogphim_14.setFont(font)
        self.chublogphim_14.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_14)

        self.chublogphim_5 = QtWidgets.QLabel("TRẠNG THÁI:")
        self.chublogphim_5.setFont(font)
        self.chublogphim_5.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.chublogphim_5)

        self.chublogphim_15 = QtWidgets.QLabel("")
        self.chublogphim_15.setFont(font)
        self.chublogphim_15.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_15)

        info_labels_layout.addStretch()
        info_layout.addLayout(info_labels_layout)
        user_info_layout.addLayout(info_layout)

        # Rest of user info content
        self.label_7 = QtWidgets.QLabel("HOẠT ĐỘNG:")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;")
        user_info_layout.addWidget(self.label_7)

        self.ad_tranguser_khuvuc_baiviet = QtWidgets.QScrollArea()
        self.ad_tranguser_khuvuc_baiviet.setWidgetResizable(True)
        self.ad_tranguser_khuvuc_baiviet.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        baiviet_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.ad_tranguser_khuvuc_baiviet.setWidget(self.scrollAreaWidgetContents_2)

        self.ad_nguoidung_baiviet = QtWidgets.QTableWidget()
        self.ad_nguoidung_baiviet.setRowCount(0)
        self.ad_nguoidung_baiviet.setColumnCount(3)
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("MOVIE ID"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("NỘI DUNG"))
        self.ad_nguoidung_baiviet.setStyleSheet("""
            QTableWidget {
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                gridline-color: rgb(200, 200, 200);
            }
            QHeaderView::section {
                background-color: rgb(128, 128, 128);
                color: rgb(255, 255, 255);
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: rgb(192, 192, 192);
                color: white;
            }
        """)
        self.ad_nguoidung_baiviet.setMinimumHeight(600)
        baiviet_layout.addWidget(self.ad_nguoidung_baiviet)
        baiviet_layout.addStretch()
        user_info_layout.addWidget(self.ad_tranguser_khuvuc_baiviet)

        
        header = self.ad_nguoidung_baiviet.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)    
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)           # Cột 1 co giãn
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        user_info_layout.addStretch()

        # ScrollArea for user table
        self.user_table_scroll_area = QtWidgets.QScrollArea()
        self.user_table_scroll_area.setWidgetResizable(True)
        self.user_table_scroll_area.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.user_table_scroll_area.setWidget(self.scrollAreaWidgetContents)
        user_table_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        user_table_layout.setContentsMargins(10, 10, 10, 10)
        main_scroll_layout.addWidget(self.user_table_scroll_area)

        # Vertical layout for buttons
        button_layout = QtWidgets.QVBoxLayout()
        self.ad_tranguser_them = QtWidgets.QPushButton("THÊM")
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.ad_tranguser_them.setFont(font)
        self.ad_tranguser_them.setStyleSheet("background-color: rgb(144, 144, 144);")
        button_layout.addWidget(self.ad_tranguser_them)

        self.ad_tranguser_sua = QtWidgets.QPushButton("SỬA")
        self.ad_tranguser_sua.setFont(font)
        self.ad_tranguser_sua.setStyleSheet("background-color: rgb(144, 144, 144);")
        button_layout.addWidget(self.ad_tranguser_sua)

        self.ad_tranguser_xoa = QtWidgets.QPushButton("XÓA")
        self.ad_tranguser_xoa.setFont(font)
        self.ad_tranguser_xoa.setStyleSheet("background-color: rgb(144, 144, 144);")
        button_layout.addWidget(self.ad_tranguser_xoa)

        button_layout.addStretch()
        user_table_layout.addLayout(button_layout)

        self.ad_tranguser_banguser = QtWidgets.QTableWidget()
        self.ad_tranguser_banguser.setRowCount(50)
        self.ad_tranguser_banguser.setColumnCount(6)
        self.ad_tranguser_banguser.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.ad_tranguser_banguser.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("USERNAME"))
        self.ad_tranguser_banguser.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("SINH NHẬT"))
        self.ad_tranguser_banguser.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("VAI TRÒ"))
        self.ad_tranguser_banguser.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("TRẠNG THÁI"))
        self.ad_tranguser_banguser.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("CHI TIẾT"))
        self.ad_tranguser_banguser.setStyleSheet("""
            QTableWidget {
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                gridline-color: rgb(200, 200, 200);
            }
            QHeaderView::section {
                background-color: rgb(128, 128, 128);
                color: rgb(255, 255, 255);
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: rgb(192, 192, 192);
                color: white;
            }
        """)
        self.ad_tranguser_banguser.setColumnWidth(0, 100)
        self.ad_tranguser_banguser.setColumnWidth(1, 200)
        self.ad_tranguser_banguser.setColumnWidth(2, 150)
        self.ad_tranguser_banguser.setColumnWidth(3, 150)
        self.ad_tranguser_banguser.setColumnWidth(4, 150)
        self.ad_tranguser_banguser.setMinimumHeight(800)
        for i in range(50):
            self.ad_tranguser_banguser.setItem(i, 0, QtWidgets.QTableWidgetItem(f"ID {i+1}"))
            self.ad_tranguser_banguser.setItem(i, 1, QtWidgets.QTableWidgetItem(f"user{i+1}@example.com"))
            self.ad_tranguser_banguser.setItem(i, 2, QtWidgets.QTableWidgetItem("Hoạt động"))
            self.ad_tranguser_banguser.setItem(i, 3, QtWidgets.QTableWidgetItem("Bình thường"))
            self.ad_tranguser_banguser.setItem(i, 4, QtWidgets.QTableWidgetItem("Chi tiết"))
        user_table_layout.addWidget(self.ad_tranguser_banguser)

        user_table_layout.addStretch()
        self.ad_tranguser_banguser.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ad_tranguser_banguser.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.centralwidget.mousePressEvent = self.clear_table_selection

        header = self.ad_tranguser_banguser.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)           # Cột 1 co giãn
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        # Menu and status bar
        self.menubar = QtWidgets.QMenuBar(parent=ad_tranguser)
        self.menubar.setObjectName("menubar")
        ad_tranguser.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=ad_tranguser)
        self.statusbar.setObjectName("statusbar")
        ad_tranguser.setStatusBar(self.statusbar)

        self.retranslateUi(ad_tranguser)
        QtCore.QMetaObject.connectSlotsByName(ad_tranguser)

    def retranslateUi(self, ad_tranguser):
        _translate = QtCore.QCoreApplication.translate
        ad_tranguser.setWindowTitle(_translate("ad_tranguser", "Quản Lý Người Dùng - Admin"))

    def clear_table_selection(self, event):
        """Tắt chọn dòng khi click ra ngoài bảng"""
        self.ad_tranguser_banguser.clearSelection()
        QtWidgets.QWidget.mousePressEvent(self.centralwidget, event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ad_tranguser = QtWidgets.QMainWindow()
    ui = Ui_ad_tranguser()
    ui.setupUi(ad_tranguser)
    ad_tranguser.show()
    sys.exit(app.exec())