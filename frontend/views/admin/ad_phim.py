from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui

class Ui_ad_trang_ql_phim(object):
    def setupUi(self, ad_trang_ql_phim):
        ad_trang_ql_phim.setObjectName("ad_trang_ql_phim")
        ad_trang_ql_phim.resize(1523, 1262)
        ad_trang_ql_phim.setStyleSheet("background-color: rgb(91, 91, 91);")

        self.centralwidget = QWidget(parent=ad_trang_ql_phim)
        self.centralwidget.setObjectName("centralwidget")
        ad_trang_ql_phim.setCentralWidget(self.centralwidget)

        # Main layout for central widget
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Header (ad_trang_qlp_thanhcc)
        self.ad_trang_qlp_thanhcc = QWidget()
        self.ad_trang_qlp_thanhcc.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.ad_trang_qlp_thanhcc.setFixedHeight(100)
        header_layout = QHBoxLayout(self.ad_trang_qlp_thanhcc)

        self.chublogphim = QLabel("ADMIN")
        font = QtGui.QFont("Colonna MT", 102, QtGui.QFont.Weight.Bold)
        font.setItalic(True)
        self.chublogphim.setFont(font)
        self.chublogphim.setStyleSheet("color: white;")
        header_layout.addWidget(self.chublogphim)

        header_layout.addStretch()

        self.ad_trang_qlp_thanhtimkiem = QLineEdit()
        self.ad_trang_qlp_thanhtimkiem.setFixedWidth(300)
        self.ad_trang_qlp_thanhtimkiem.setStyleSheet("background-color: rgb(144, 144, 144); color: white;")
        header_layout.addWidget(self.ad_trang_qlp_thanhtimkiem)

        self.ad_trang_qlp_timkiem = QPushButton("TÌM KIẾM")
        self.ad_trang_qlp_timkiem.setFixedWidth(100)
        self.ad_trang_qlp_timkiem.setStyleSheet("background-color: rgb(24, 24, 24); color: rgb(230, 230, 230);")
        header_layout.addWidget(self.ad_trang_qlp_timkiem)

        # Nút TRANG CHỦ và LƯU xếp dọc
        button_layout = QVBoxLayout()
        self.ad_trang_qlp_back = QPushButton("TRANG CHỦ")
        self.ad_trang_qlp_back.setFixedWidth(100)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ad_trang_qlp_back.setFont(font)
        self.ad_trang_qlp_back.setStyleSheet("background-color: rgb(223, 223, 223);")
        button_layout.addWidget(self.ad_trang_qlp_back)

        self.ad_trang_qlp_luu = QPushButton("LƯU")
        self.ad_trang_qlp_luu.setFixedWidth(100)
        self.ad_trang_qlp_luu.setFont(font)
        self.ad_trang_qlp_luu.setStyleSheet("background-color: rgb(223, 223, 237);")
        button_layout.addWidget(self.ad_trang_qlp_luu)
        header_layout.addLayout(button_layout)

        main_layout.addWidget(self.ad_trang_qlp_thanhcc)

        # Main ScrollArea containing thanhcc2 and khubangphim
        self.main_scroll_area = QScrollArea()
        self.main_scroll_area.setWidgetResizable(True)
        self.main_scroll_area.setStyleSheet("background-color: rgb(91, 91, 91);")
        main_scroll_content = QWidget()
        self.main_scroll_area.setWidget(main_scroll_content)
        main_scroll_layout = QHBoxLayout(main_scroll_content)
        main_scroll_layout.setContentsMargins(0, 0, 0, 0)
        main_scroll_layout.setSpacing(10)
        main_layout.addWidget(self.main_scroll_area)

        # ScrollArea for ad_trang_qlp_thanhcc2
        self.thanhcc2_scroll_area = QScrollArea()
        self.thanhcc2_scroll_area.setWidgetResizable(True)
        self.thanhcc2_scroll_area.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.thanhcc2_scroll_area.setFixedWidth(480)  # 2/5 of 1200px
        self.ad_trang_qlp_thanhcc2 = QWidget()
        self.thanhcc2_scroll_area.setWidget(self.ad_trang_qlp_thanhcc2)
        thanhcc2_layout = QVBoxLayout(self.ad_trang_qlp_thanhcc2)
        thanhcc2_layout.setContentsMargins(10, 10, 10, 10)

        # Horizontal layout for anhphim and info
        info_layout = QHBoxLayout()

        # Anh phim
        self.ad_trang_qlp_anhphim = QLabel("POSTERPHIM")
        self.ad_trang_qlp_anhphim.setFixedSize(200, 300)
        self.ad_trang_qlp_anhphim.setStyleSheet("background-color: rgb(255, 255, 255);")
        info_layout.addWidget(self.ad_trang_qlp_anhphim)

        # Vertical layout for info labels
        info_labels_layout = QVBoxLayout()
        self.ad_trang_qlp_tenphim = QLabel("TÊN BỘ PHIM")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.ad_trang_qlp_tenphim.setFont(font)
        self.ad_trang_qlp_tenphim.setStyleSheet("color: white;")
        self.ad_trang_qlp_tenphim.setWordWrap(True)
        info_labels_layout.addWidget(self.ad_trang_qlp_tenphim)

        self.ad_trang_qlp_thongtin1 = QLabel("RANK:")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ad_trang_qlp_thongtin1.setFont(font)
        self.ad_trang_qlp_thongtin1.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.ad_trang_qlp_thongtin1)

        self.ad_trang_qlp_rank = QLabel("số 1")
        self.ad_trang_qlp_rank.setFont(font)
        self.ad_trang_qlp_rank.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.ad_trang_qlp_rank)

        self.ad_trang_qlp_thongtin2 = QLabel("TRẠNG THÁI:")
        self.ad_trang_qlp_thongtin2.setFont(font)
        self.ad_trang_qlp_thongtin2.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.ad_trang_qlp_thongtin2)

        self.ad_trang_qlp_trangthai = QLabel("ĐANG RA")
        self.ad_trang_qlp_trangthai.setFont(font)
        self.ad_trang_qlp_trangthai.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.ad_trang_qlp_trangthai)

        self.ad_trang_qlp__thongtin3 = QLabel("NĂM PHÁT HÀNH:")
        self.ad_trang_qlp__thongtin3.setFont(font)
        self.ad_trang_qlp__thongtin3.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.ad_trang_qlp__thongtin3)

        self.ad_trang_qlp_nam = QLabel("2020")
        self.ad_trang_qlp_nam.setFont(font)
        self.ad_trang_qlp_nam.setStyleSheet("color: white;")
        info_labels_layout.addWidget(self.ad_trang_qlp_nam)

        info_labels_layout.addStretch()
        info_layout.addLayout(info_labels_layout)
        thanhcc2_layout.addLayout(info_layout)

        # Rest of thanhcc2 content
        self.ad_trang_qlp_motaphim = QTextBrowser()
        self.ad_trang_qlp_motaphim.setMinimumHeight(200)
        self.ad_trang_qlp_motaphim.setStyleSheet("""
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                font-size: 12px;
                font-family: Arial;
                border: 1px solid rgb(200, 200, 200);
                border-radius: 5px;
                padding: 5px;
            """)
        self.ad_trang_qlp_motaphim.setHtml("""
            <p>MÔ TẢ PHIM: Nội dung mô tả phim ở đây...</p>
            <p>MÔ TẢ NỮA: Thêm thông tin chi tiết về phim...</p>
        """)
        thanhcc2_layout.addWidget(self.ad_trang_qlp_motaphim)

        self.ad_trang_qlp_comment = QLabel("BÌNH LUẬN:")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        self.ad_trang_qlp_comment.setFont(font)
        self.ad_trang_qlp_comment.setStyleSheet("color: white;")
        thanhcc2_layout.addWidget(self.ad_trang_qlp_comment)

        self.ad_nguoidung_baiviet = QTableWidget()
        self.ad_nguoidung_baiviet.setRowCount(50)
        self.ad_nguoidung_baiviet.setColumnCount(3)
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(1, QTableWidgetItem("MOVIE ID"))
        self.ad_nguoidung_baiviet.setHorizontalHeaderItem(2, QTableWidgetItem("NỘI DUNG"))
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

        header = self.ad_nguoidung_baiviet.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Cột 0 tự động vừa nội dung
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)           
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ad_nguoidung_baiviet.setMinimumHeight(600)
        thanhcc2_layout.addWidget(self.ad_nguoidung_baiviet)

        thanhcc2_layout.addStretch()
        main_scroll_layout.addWidget(self.thanhcc2_scroll_area)

        # ScrollArea for ad_trang_qlp_khubangphim
        self.khubangphim_scroll_area = QScrollArea()
        self.khubangphim_scroll_area.setWidgetResizable(True)
        self.khubangphim_scroll_area.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.ad_trang_qlp_khubangphim = QWidget()
        self.khubangphim_scroll_area.setWidget(self.ad_trang_qlp_khubangphim)
        khubangphim_layout = QVBoxLayout(self.ad_trang_qlp_khubangphim)
        khubangphim_layout.setContentsMargins(10, 10, 10, 10)

        # Vertical layout for buttons
        button_layout = QVBoxLayout()
        self.ad_trang_qlp_them = QPushButton("THÊM")
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.ad_trang_qlp_them.setFont(font)
        self.ad_trang_qlp_them.setStyleSheet("background-color: rgb(144, 144, 144);")
        button_layout.addWidget(self.ad_trang_qlp_them)

        self.ad_trang_qlp_sua = QPushButton("SỬA")
        self.ad_trang_qlp_sua.setFont(font)
        self.ad_trang_qlp_sua.setStyleSheet("background-color: rgb(144, 144, 144);")
        button_layout.addWidget(self.ad_trang_qlp_sua)

        self.ad_trang_qlp_xoa = QPushButton("XÓA")
        self.ad_trang_qlp_xoa.setFont(font)
        self.ad_trang_qlp_xoa.setStyleSheet("background-color: rgb(144, 144, 144);")
        button_layout.addWidget(self.ad_trang_qlp_xoa)

        button_layout.addStretch()
        khubangphim_layout.addLayout(button_layout)

        self.ad_trang_qlp_bangphim = QTableWidget()
        self.ad_trang_qlp_bangphim.setRowCount(50)
        self.ad_trang_qlp_bangphim.setColumnCount(5)
        self.ad_trang_qlp_bangphim.setHorizontalHeaderItem(0, QTableWidgetItem("TOP"))
        self.ad_trang_qlp_bangphim.setHorizontalHeaderItem(1, QTableWidgetItem("TIÊU ĐỀ"))
        self.ad_trang_qlp_bangphim.setHorizontalHeaderItem(2, QTableWidgetItem("ĐIỂM"))
        self.ad_trang_qlp_bangphim.setHorizontalHeaderItem(3, QTableWidgetItem("ĐÁNH GIÁ"))
        self.ad_trang_qlp_bangphim.setHorizontalHeaderItem(4, QTableWidgetItem("CHI TIẾT"))
        self.ad_trang_qlp_bangphim.setStyleSheet("""
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
        self.ad_trang_qlp_bangphim.setColumnWidth(0, 100)
        self.ad_trang_qlp_bangphim.setColumnWidth(1, 450)
        self.ad_trang_qlp_bangphim.setColumnWidth(2, 100)
        self.ad_trang_qlp_bangphim.setColumnWidth(3, 100)
        self.ad_trang_qlp_bangphim.setColumnWidth(4, 190)
        self.ad_trang_qlp_bangphim.setMinimumHeight(800)

        self.ad_trang_qlp_bangphim.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ad_trang_qlp_bangphim.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.centralwidget.mousePressEvent = self.clear_table_selection

        header = self.ad_trang_qlp_bangphim.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Cột 0 tự động vừa nội dung
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)           # Cột 1 co giãn
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Cột 2 tự động vừa nội dung
        # header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)           # Cột 3 co giãn
        # header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)           # Cột 4 co giãn


        for i in range(50):
            self.ad_trang_qlp_bangphim.setItem(i, 0, QTableWidgetItem(f"Top {i+1}"))
            self.ad_trang_qlp_bangphim.setItem(i, 1, QTableWidgetItem(f"Phim {i+1}"))
            self.ad_trang_qlp_bangphim.setItem(i, 2, QTableWidgetItem("8.0"))
            self.ad_trang_qlp_bangphim.setItem(i, 3, QTableWidgetItem("Tốt"))
            self.ad_trang_qlp_bangphim.setItem(i, 4, QTableWidgetItem("Chi tiết"))
        khubangphim_layout.addWidget(self.ad_trang_qlp_bangphim)

        khubangphim_layout.addStretch()
        main_scroll_layout.addWidget(self.khubangphim_scroll_area)

        # Menu and status bar
        self.menubar = QMenuBar(parent=ad_trang_ql_phim)
        self.menubar.setObjectName("menubar")
        ad_trang_ql_phim.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(parent=ad_trang_ql_phim)
        self.statusbar.setObjectName("statusbar")
        ad_trang_ql_phim.setStatusBar(self.statusbar)

        self.retranslateUi(ad_trang_ql_phim)
        QtCore.QMetaObject.connectSlotsByName(ad_trang_ql_phim)

    def retranslateUi(self, ad_trang_ql_phim):
        _translate = QtCore.QCoreApplication.translate
        ad_trang_ql_phim.setWindowTitle(_translate("ad_trang_ql_phim", "Quản Lý Phim - Admin"))

    def clear_table_selection(self, event):
        self.ad_trang_qlp_bangphim.clearSelection()
        QWidget.mousePressEvent(self.centralwidget, event)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ad_trang_ql_phim = QMainWindow()
    ui = Ui_ad_trang_ql_phim()
    ui.setupUi(ad_trang_ql_phim)
    ad_trang_ql_phim.show()
    sys.exit(app.exec())