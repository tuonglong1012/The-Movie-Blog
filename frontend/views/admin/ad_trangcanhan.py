from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView

class Ui_ad_trangcanhan(object):
    def setupUi(self, ad_trangcanhan):
        ad_trangcanhan.setObjectName("ad_trangcanhan")
        ad_trangcanhan.resize(1523, 1262)
        ad_trangcanhan.setStyleSheet("background-color: rgb(203, 203, 203);")

        self.centralwidget = QtWidgets.QWidget(parent=ad_trangcanhan)
        self.centralwidget.setObjectName("centralwidget")
        ad_trangcanhan.setCentralWidget(self.centralwidget)

        # Main layout for central widget
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Header
        self.header_widget = QtWidgets.QWidget()
        self.header_widget.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.header_widget.setFixedHeight(100)
        header_layout = QtWidgets.QHBoxLayout(self.header_widget)

        self.ad_tranguser_homthu = QtWidgets.QListWidget()
        self.ad_tranguser_homthu.setFixedSize(100, 60)
        self.ad_tranguser_homthu.setStyleSheet("background-color: rgb(163, 163, 163);")
        self.ad_tranguser_homthu.addItem("Yêu cầu 1")
        self.ad_tranguser_homthu.addItem("Yêu cầu 2")
        header_layout.addWidget(self.ad_tranguser_homthu)

        self.chublogphim = QtWidgets.QLabel("ADMIN")
        font = QtGui.QFont("Colonna MT", 54, QtGui.QFont.Weight.Bold)
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

        main_layout.addWidget(self.header_widget)

        # Main ScrollArea containing user info and activity
        self.main_scroll_area = QtWidgets.QScrollArea()
        self.main_scroll_area.setWidgetResizable(True)
        self.main_scroll_area.setStyleSheet("background-color: rgb(203, 203, 203);")
        main_scroll_content = QtWidgets.QWidget()
        self.main_scroll_area.setWidget(main_scroll_content)
        main_scroll_layout = QtWidgets.QHBoxLayout(main_scroll_content)
        main_scroll_layout.setContentsMargins(0, 0, 0, 0)
        main_scroll_layout.setSpacing(10)
        main_layout.addWidget(self.main_scroll_area)

        # ScrollArea for user info
        self.user_info_scroll_area = QtWidgets.QScrollArea()
        self.user_info_scroll_area.setWidgetResizable(True)
        self.user_info_scroll_area.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.user_info_scroll_area.setFixedWidth(480)  # 2/5 of 1200px
        self.user_info_widget = QtWidgets.QWidget()
        self.user_info_scroll_area.setWidget(self.user_info_widget)
        user_info_layout = QtWidgets.QVBoxLayout(self.user_info_widget)
        user_info_layout.setContentsMargins(10, 10, 10, 10)
        main_scroll_layout.addWidget(self.user_info_scroll_area)

        # Horizontal layout for avatar and info
        info_layout = QtWidgets.QHBoxLayout()

        # Avatar
        self.ad_tranguser_avt = QtWidgets.QLabel("AVATAR")
        self.ad_tranguser_avt.setFixedSize(260, 350)
        self.ad_tranguser_avt.setStyleSheet("background-color: rgb(255, 255, 255);")
        info_layout.addWidget(self.ad_tranguser_avt)

        # Vertical layout for info labels
        info_labels_layout = QtWidgets.QVBoxLayout()
        self.chublogphim_6 = QtWidgets.QLabel("THÔNG TIN CÁ NHÂN:")
        font = QtGui.QFont("MS Shell Dlg 2", 16, QtGui.QFont.Weight.Bold)
        self.chublogphim_6.setFont(font)
        self.chublogphim_6.setStyleSheet("color: black;")
        info_labels_layout.addWidget(self.chublogphim_6)

        self.chublogphim_2 = QtWidgets.QLabel("TÊN TÀI KHOẢN:")
        font = QtGui.QFont("MS Shell Dlg 2", 13)
        self.chublogphim_2.setFont(font)
        self.chublogphim_2.setStyleSheet("color: black;")
        info_labels_layout.addWidget(self.chublogphim_2)

        self.chublogphim_12 = QtWidgets.QLabel("NGUYỄN BÙNG BINH")
        font = QtGui.QFont("Arial Black", 14, QtGui.QFont.Weight.Bold)
        self.chublogphim_12.setFont(font)
        self.chublogphim_12.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_12)

        self.chublogphim_3 = QtWidgets.QLabel("ID:")
        font = QtGui.QFont("MS Shell Dlg 2", 12)
        self.chublogphim_3.setFont(font)
        self.chublogphim_3.setStyleSheet("color: black;")
        info_labels_layout.addWidget(self.chublogphim_3)

        self.chublogphim_13 = QtWidgets.QLabel("BUNGBINH@GMAI.COM")
        self.chublogphim_13.setFont(font)
        self.chublogphim_13.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_13)

        self.chublogphim_4 = QtWidgets.QLabel("NGÀY SINH:")
        self.chublogphim_4.setFont(font)
        self.chublogphim_4.setStyleSheet("color: black;")
        info_labels_layout.addWidget(self.chublogphim_4)

        self.chublogphim_14 = QtWidgets.QLabel("19001008")
        self.chublogphim_14.setFont(font)
        self.chublogphim_14.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_14)

        self.chublogphim_5 = QtWidgets.QLabel("VAI TRÒ:")
        self.chublogphim_5.setFont(font)
        self.chublogphim_5.setStyleSheet("color: black;")
        info_labels_layout.addWidget(self.chublogphim_5)

        self.chublogphim_15 = QtWidgets.QLabel("BIA ĐIA")
        self.chublogphim_15.setFont(font)
        self.chublogphim_15.setStyleSheet("background-color: rgb(0, 0, 0);")
        info_labels_layout.addWidget(self.chublogphim_15)

        info_labels_layout.addStretch()
        info_layout.addLayout(info_labels_layout)
        user_info_layout.addLayout(info_layout)

        # XÓA TÀI KHOẢN button
        button_layout = QtWidgets.QVBoxLayout()
        self.ad_trangcanhan_baned = QtWidgets.QPushButton("BANED")
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.ad_trangcanhan_baned.setFont(font)
        self.ad_trangcanhan_baned.setStyleSheet("background-color: rgb(192,192,192);")
        self.ad_trangcanhan_baned.setFixedWidth(180)
        button_layout.addWidget(self.ad_trangcanhan_baned)
        button_layout.addStretch()
        user_info_layout.addLayout(button_layout)

        # YÊU THÍCH table
        self.label_8 = QtWidgets.QLabel("YÊU THÍCH:")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: black;")
        user_info_layout.addWidget(self.label_8)

        self.ad_trangchu_bangphim = QtWidgets.QTableWidget()
        self.ad_trangchu_bangphim.setRowCount(50)
        self.ad_trangchu_bangphim.setColumnCount(3)
        self.ad_trangchu_bangphim.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("TOP"))
        self.ad_trangchu_bangphim.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("TIÊU ĐỀ"))
        self.ad_trangchu_bangphim.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("HÀNH ĐỘNG"))

        self.ad_trangchu_bangphim.setStyleSheet("""
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
        self.ad_trangchu_bangphim.setColumnWidth(0, 100)
        self.ad_trangchu_bangphim.setColumnWidth(1, 200)
        self.ad_trangchu_bangphim.setColumnWidth(2, 150)
        self.ad_trangchu_bangphim.setMinimumHeight(600)
        for i in range(50):
            self.ad_trangchu_bangphim.setItem(i, 0, QtWidgets.QTableWidgetItem(f"Top {i+1}"))
            self.ad_trangchu_bangphim.setItem(i, 1, QtWidgets.QTableWidgetItem(f"Phim {i+1}"))
            self.ad_trangchu_bangphim.setItem(i, 2, QtWidgets.QTableWidgetItem("Hành động"))
        user_info_layout.addWidget(self.ad_trangchu_bangphim)

        user_info_layout.addStretch()

        # ScrollArea for activity
        self.activity_scroll_area = QtWidgets.QScrollArea()
        self.activity_scroll_area.setWidgetResizable(True)
        self.activity_scroll_area.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.activity_widget = QtWidgets.QWidget()
        self.activity_scroll_area.setWidget(self.activity_widget)
        activity_layout = QtWidgets.QVBoxLayout(self.activity_widget)
        activity_layout.setContentsMargins(10, 10, 10, 10)
        main_scroll_layout.addWidget(self.activity_scroll_area)

        # HOẠT ĐỘNG table
        self.label_7 = QtWidgets.QLabel("HOẠT ĐỘNG:")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: black;")
        activity_layout.addWidget(self.label_7)

        self.ad_nguoidung_baiviet = QtWidgets.QTableWidget()
        self.ad_nguoidung_baiviet.setRowCount(50)
        self.ad_nguoidung_baiviet.setColumnCount(4)
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("MOVIE ID"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("NỘI DUNG"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("HÀNH ĐỘNG"))
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
        self.ad_nguoidung_baiviet.setColumnWidth(0, 200)
        self.ad_nguoidung_baiviet.setColumnWidth(1, 300)
        self.ad_nguoidung_baiviet.setColumnWidth(2, 150)
        self.ad_nguoidung_baiviet.setMinimumHeight(800)
        for i in range(50):
            self.ad_nguoidung_baiviet.setItem(i, 0, QtWidgets.QTableWidgetItem(f"Thời gian {i}"))
            self.ad_nguoidung_baiviet.setItem(i, 1, QtWidgets.QTableWidgetItem(f"Nội dung {i}"))
            self.ad_nguoidung_baiviet.setItem(i, 2, QtWidgets.QTableWidgetItem("Hành động"))
        activity_layout.addWidget(self.ad_nguoidung_baiviet)

        activity_layout.addStretch()

        header = self.ad_nguoidung_baiviet.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Cột 0 tự động vừa nội dung
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)           # Cột 1 co giãn
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        # Menu and status bar
        self.menubar = QtWidgets.QMenuBar(parent=ad_trangcanhan)
        self.menubar.setObjectName("menubar")
        ad_trangcanhan.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=ad_trangcanhan)
        self.statusbar.setObjectName("statusbar")
        ad_trangcanhan.setStatusBar(self.statusbar)

        self.retranslateUi(ad_trangcanhan)
        QtCore.QMetaObject.connectSlotsByName(ad_trangcanhan)

    def retranslateUi(self, ad_trangcanhan):
        _translate = QtCore.QCoreApplication.translate
        ad_trangcanhan.setWindowTitle(_translate("ad_trangcanhan", "Trang Cá Nhân - Admin"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ad_trangcanhan = QtWidgets.QMainWindow()
    ui = Ui_ad_trangcanhan()
    ui.setupUi(ad_trangcanhan)
    ad_trangcanhan.show()
    sys.exit(app.exec())