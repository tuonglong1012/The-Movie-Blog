from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

class Ui_ad_themphim(object):
    def setupUi(self, ad_themphim):
        ad_themphim.setObjectName("ad_themphim")
        ad_themphim.resize(1898, 1595)
        self.centralwidget = QtWidgets.QWidget(parent=ad_themphim)
        self.centralwidget.setObjectName("centralwidget")
        self.ad_themphim_thanhcc = QtWidgets.QWidget(parent=self.centralwidget)
        self.ad_themphim_thanhcc.setGeometry(QtCore.QRect(0, 0, 1981, 121))
        self.ad_themphim_thanhcc.setAutoFillBackground(False)
        self.ad_themphim_thanhcc.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.ad_themphim_thanhcc.setObjectName("ad_themphim_thanhcc")
        self.chublogphim = QtWidgets.QLabel(parent=self.ad_themphim_thanhcc)
        self.chublogphim.setGeometry(QtCore.QRect(40, 20, 431, 101))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(68)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.chublogphim.setFont(font)
        self.chublogphim.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.chublogphim.setObjectName("chublogphim")

        self.ad_themphim_back = QtWidgets.QPushButton(parent=self.ad_themphim_thanhcc)
        self.ad_themphim_back.setGeometry(QtCore.QRect(1340, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ad_themphim_back.setFont(font)
        self.ad_themphim_back.setAutoFillBackground(False)
        self.ad_themphim_back.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ad_themphim_back.setObjectName("ad_themphim_back")

        self.ad_themphim_luu = QtWidgets.QPushButton(parent=self.ad_themphim_thanhcc)
        self.ad_themphim_luu.setGeometry(QtCore.QRect(1340, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ad_themphim_luu.setFont(font)
        self.ad_themphim_luu.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ad_themphim_luu.setObjectName("ad_themphim_luu")
        
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 130, 381, 800))  # Chiều cao 800
        self.scrollArea.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(379, 1400))
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ad_themphim_motaphim = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.ad_themphim_motaphim.setGeometry(QtCore.QRect(10, 60, 321, 600))  # Điều chỉnh chiều cao
        self.ad_themphim_motaphim.setObjectName("ad_themphim_motaphim")
        self.ad_themphim_motaphim.setStyleSheet("""
            QTextBrowser {
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                font-size: 12px;
                font-family: Arial;
                border: 1px solid rgb(200, 200, 200);
                border-radius: 5px;
                padding: 5px;
            }
        """)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(380, 160, 1808, 1671))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(1806, 3200))  # Tăng để chứa bảng nhân vật
        self.ad_themphim_anhphim = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_anhphim.setGeometry(QtCore.QRect(70, 40, 381, 491))
        self.ad_themphim_anhphim.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad_themphim_anhphim.setObjectName("ad_themphim_anhphim")
        self.ad_trang_qlp_thongtin1 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp_thongtin1.setGeometry(QtCore.QRect(530, 160, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp_thongtin1.setFont(font)
        self.ad_trang_qlp_thongtin1.setObjectName("ad_trang_qlp_thongtin1")
        self.ad_trang_qlp_thongtin1_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp_thongtin1_2.setGeometry(QtCore.QRect(850, 160, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp_thongtin1_2.setFont(font)
        self.ad_trang_qlp_thongtin1_2.setObjectName("ad_trang_qlp_thongtin1_2")
        self.ad_trang_qlp_thongtin2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp_thongtin2.setGeometry(QtCore.QRect(530, 240, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp_thongtin2.setFont(font)
        self.ad_trang_qlp_thongtin2.setObjectName("ad_trang_qlp_thongtin2")
        self.ad_trang_qlp__thongtin3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp__thongtin3.setGeometry(QtCore.QRect(530, 330, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp__thongtin3.setFont(font)
        self.ad_trang_qlp__thongtin3.setObjectName("ad_trang_qlp__thongtin3")
        self.ad_trang_qlp_thongtin1_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp_thongtin1_4.setGeometry(QtCore.QRect(850, 330, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp_thongtin1_4.setFont(font)
        self.ad_trang_qlp_thongtin1_4.setObjectName("ad_trang_qlp_thongtin1_4")
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.scrollAreaWidgetContents_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(30, 640, 1101, 351))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(1099, 1000))
        self.ad_trang_qlp_tenphim_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp_tenphim_4.setGeometry(QtCore.QRect(-10, 342, 533, 551))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ad_trang_qlp_tenphim_4.setFont(font)
        self.ad_trang_qlp_tenphim_4.setObjectName("ad_trang_qlp_tenphim_4")
        self.ad_themphim_otaphim = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        self.ad_themphim_otaphim.setGeometry(QtCore.QRect(0, 0, 1061, 351))
        font = QtGui.QFont()
        font.setItalic(True)
        self.ad_themphim_otaphim.setFont(font)
        self.ad_themphim_otaphim.setObjectName("ad_themphim_otaphim")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        # ScrollArea cho bảng nhân vật
        self.scrollArea_nhanvat = QtWidgets.QScrollArea(parent=self.scrollAreaWidgetContents_2)
        self.scrollArea_nhanvat.setGeometry(QtCore.QRect(80, 1020, 1061, 150))  # Chiều cao ~5 dòng
        self.scrollArea_nhanvat.setWidgetResizable(True)
        self.scrollArea_nhanvat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_nhanvat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_nhanvat.setObjectName("scrollArea_nhanvat")
        self.scrollAreaWidgetContents_nhanvat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_nhanvat.setObjectName("scrollAreaWidgetContents_nhanvat")
        self.scrollAreaWidgetContents_nhanvat.setMinimumSize(QtCore.QSize(1059, 150))

        # Bảng nhân vật
        self.ad_themphim_bang_nhanvat = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_nhanvat)
        self.ad_themphim_bang_nhanvat.setGeometry(QtCore.QRect(0, 0, 1059, 150))  # Fit scroll area
        self.ad_themphim_bang_nhanvat.setObjectName("ad_themphim_bang_nhanvat")
        self.ad_themphim_bang_nhanvat.setColumnCount(4)
        self.ad_themphim_bang_nhanvat.setStyleSheet("""
            QTableWidget {
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                gridline-color: rgb(200, 200, 200);
            }
            QHeaderView::section {
                background-color: rgb(128,128,128);
                color: rgb(255, 255, 255);
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: rgb(192,192,192);
                color: white;
            }
        """)
        self.ad_themphim_bang_nhanvat.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("NHÂN VẬT"))
        self.ad_themphim_bang_nhanvat.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("VAI TRÒ"))
        self.ad_themphim_bang_nhanvat.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("DIỄN VIÊN LỒNG TIẾNG"))
        self.ad_themphim_bang_nhanvat.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("THÔNG TIN"))

        self.ad_themphim_bang_nhanvat.setColumnWidth(0, 200)
        self.ad_themphim_bang_nhanvat.setColumnWidth(1, 150)
        self.ad_themphim_bang_nhanvat.setColumnWidth(2, 200)
        self.ad_themphim_bang_nhanvat.setColumnWidth(3, 250)
        self.scrollArea_nhanvat.setWidget(self.scrollAreaWidgetContents_nhanvat)

        header = self.ad_themphim_bang_nhanvat.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)

        # Các nút THÊM, SỬA, XÓA
        self.ad_themphim_them_nhanvat = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_them_nhanvat.setGeometry(QtCore.QRect(30, 1020, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ad_themphim_them_nhanvat.setFont(font)
        self.ad_themphim_them_nhanvat.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ad_themphim_them_nhanvat.setText("THÊM")
        self.ad_themphim_them_nhanvat.setObjectName("ad_themphim_them_nhanvat")

        self.ad_themphim_sua_nhanvat = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_sua_nhanvat.setGeometry(QtCore.QRect(30, 1070, 41, 41))
        self.ad_themphim_sua_nhanvat.setFont(font)
        self.ad_themphim_sua_nhanvat.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ad_themphim_sua_nhanvat.setText("SỬA")
        self.ad_themphim_sua_nhanvat.setObjectName("ad_themphim_sua_nhanvat")

        self.ad_themphim_xoa_nhanvat = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_xoa_nhanvat.setGeometry(QtCore.QRect(30, 1120, 41, 41))
        self.ad_themphim_xoa_nhanvat.setFont(font)
        self.ad_themphim_xoa_nhanvat.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ad_themphim_xoa_nhanvat.setText("XÓA")
        self.ad_themphim_xoa_nhanvat.setObjectName("ad_themphim_xoa_nhanvat")

        self.ad_themphim_khubl = QtWidgets.QScrollArea(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_khubl.setGeometry(QtCore.QRect(30, 1280, 1111, 1000))  # Dịch xuống để nhường chỗ
        self.ad_themphim_khubl.setWidgetResizable(True)
        self.ad_themphim_khubl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ad_themphim_khubl.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ad_themphim_khubl.setObjectName("ad_themphim_khubl")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setMinimumSize(QtCore.QSize(1109, 1000))  # Match table height
        self.ad_themphim_bang_bl = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_4)
        self.ad_themphim_bang_bl.setGeometry(QtCore.QRect(10, 70, 1071, 920))  # Fit within scroll area
        self.ad_themphim_bang_bl.setObjectName("ad_themphim_bang_bl")
        self.ad_themphim_bang_bl.setColumnCount(5)
        # self.ad_themphim_bang_bl.setRowCount(44)
        self.ad_themphim_bang_bl.setStyleSheet("""
            QTableWidget {
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                gridline-color: rgb(200, 200, 200);
            }
            QHeaderView::section {
                background-color: rgb(128,128,128);
                color: rgb(255, 255, 255);
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: rgb(192,192,192);
                color: white;
            }
            QTableWidget::item {
                selection-background-color: rgb(200, 200, 255);
                selection-color: rgb(0, 0, 0);
            }
        """)
        
        for i in range(5):
            item = QtWidgets.QTableWidgetItem()
            self.ad_themphim_bang_bl.setHorizontalHeaderItem(i, item)

        header = self.ad_themphim_bang_bl.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ad_trang_qlp_thongtin1_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_4)
        self.ad_trang_qlp_thongtin1_5.setGeometry(QtCore.QRect(720, 430, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp_thongtin1_5.setFont(font)
        self.ad_trang_qlp_thongtin1_5.setObjectName("ad_trang_qlp_thongtin1_5")
        self.ad_trang_qlp_thongtin1_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_4)
        self.ad_trang_qlp_thongtin1_3.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.ad_trang_qlp_thongtin1_3.setFont(font)
        self.ad_trang_qlp_thongtin1_3.setObjectName("ad_trang_qlp_thongtin1_3")
        self.ad_themphim_khubl.setWidget(self.scrollAreaWidgetContents_4)
        self.ad_themphim_rank = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_rank.setGeometry(QtCore.QRect(590, 180, 251, 31))
        self.ad_themphim_rank.setAutoFillBackground(False)
        self.ad_themphim_rank.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ad_themphim_rank.setText("")
        self.ad_themphim_rank.setObjectName("ad_themphim_rank")
        self.ad_themphim_donoitieng = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_donoitieng.setGeometry(QtCore.QRect(650, 260, 451, 31))
        self.ad_themphim_donoitieng.setAutoFillBackground(False)
        self.ad_themphim_donoitieng.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ad_themphim_donoitieng.setText("")
        self.ad_themphim_donoitieng.setObjectName("ad_themphim_donoitieng")
        self.ad_themphim_diem = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_diem.setGeometry(QtCore.QRect(910, 180, 191, 31))
        self.ad_themphim_diem.setAutoFillBackground(False)
        self.ad_themphim_diem.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ad_themphim_diem.setText("")
        self.ad_themphim_diem.setObjectName("ad_themphim_diem")
        self.ad_themphim_nguoitheodoi = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_nguoitheodoi.setGeometry(QtCore.QRect(690, 350, 151, 31))
        self.ad_themphim_nguoitheodoi.setAutoFillBackground(False)
        self.ad_themphim_nguoitheodoi.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ad_themphim_nguoitheodoi.setText("")
        self.ad_themphim_nguoitheodoi.setObjectName("ad_themphim_nguoitheodoi")
        self.ad_themphim_yeuthich = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_yeuthich.setGeometry(QtCore.QRect(620, 440, 481, 31))
        self.ad_themphim_yeuthich.setAutoFillBackground(False)
        self.ad_themphim_yeuthich.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ad_themphim_yeuthich.setText("")
        self.ad_themphim_yeuthich.setObjectName("ad_themphim_yeuthich")
        self.ad_themphim_sotap = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_sotap.setGeometry(QtCore.QRect(920, 350, 181, 31))
        self.ad_themphim_sotap.setAutoFillBackground(False)
        self.ad_themphim_sotap.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ad_themphim_sotap.setText("")
        self.ad_themphim_sotap.setObjectName("ad_themphim_sotap")
        self.ad_trang_qlp_thongtin1_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.ad_trang_qlp_thongtin1_6.setGeometry(QtCore.QRect(530, 430, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ad_trang_qlp_thongtin1_6.setFont(font)
        self.ad_trang_qlp_thongtin1_6.setObjectName("ad_trang_qlp_thongtin1_6")
        self.ad_themphim_chonanh = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_chonanh.setGeometry(QtCore.QRect(180, 540, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ad_themphim_chonanh.setFont(font)
        self.ad_themphim_chonanh.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.ad_themphim_chonanh.setObjectName("ad_themphim_chonanh")
        self.ad_themphim_title = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents_2)
        self.ad_themphim_title.setGeometry(QtCore.QRect(500, 40, 600, 80))
        self.ad_themphim_title.setObjectName("ad_themphim_title")
        font = QtGui.QFont()
        font.setPointSize(14)  # Kích cỡ chữ (ví dụ: 14)
        font.setBold(True)  # Nếu muốn chữ in đậm
        self.ad_themphim_title.setFont(font)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        ad_themphim.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ad_themphim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1898, 26))
        self.menubar.setObjectName("menubar")
        ad_themphim.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ad_themphim)
        self.statusbar.setObjectName("statusbar")
        ad_themphim.setStatusBar(self.statusbar)

        widgets = [
            self.ad_themphim_title,
            self.ad_themphim_rank,
            self.ad_themphim_donoitieng,
            self.ad_themphim_diem,
            self.ad_themphim_nguoitheodoi,
            self.ad_themphim_yeuthich,
            self.ad_themphim_sotap
        ]

        for widget in widgets:
            widget.setStyleSheet("""
                background-color: rgb(144, 144, 144);
                color: rgb(255, 255, 255);
            """)

        self.retranslateUi(ad_themphim)
        QtCore.QMetaObject.connectSlotsByName(ad_themphim)

    def retranslateUi(self, ad_themphim):
        _translate = QtCore.QCoreApplication.translate
        ad_themphim.setWindowTitle(_translate("ad_themphim", "MainWindow"))
        self.chublogphim.setText(_translate("ad_themphim", "ADMIN"))
        self.ad_themphim_back.setText(_translate("ad_themphim", "TRANG CHỦ "))
        self.ad_themphim_luu.setText(_translate("ad_themphim", "LƯU"))
        self.label.setText(_translate("ad_themphim", "THÔNG TIN PHIM "))
        self.ad_themphim_anhphim.setText(_translate("ad_themphim", "POSTERPHIM"))
        self.ad_trang_qlp_thongtin1.setText(_translate("ad_themphim", "RANK:"))
        self.ad_trang_qlp_thongtin1_2.setText(_translate("ad_themphim", "ĐIỂM:"))
        self.ad_trang_qlp_thongtin2.setText(_translate("ad_themphim", "ĐỘ NỔI:"))
        self.ad_trang_qlp__thongtin3.setText(_translate("ad_themphim", "NGƯỜI THEO DÕI:"))
        self.ad_trang_qlp_thongtin1_4.setText(_translate("ad_themphim", "SỐ TẬP"))
        self.ad_themphim_otaphim.setHtml(_translate("ad_themphim", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MÔ TẢ PHIM NÈ: NBHJGSVGDVCGDHCVHDJCBSKHJBCHDJCVGDVCHDJBCVDCJ XND GCHBALEGVFYEOIJXKQWNHUBIOEJHNXHQBVEHGUDOLWQBDVFRHDKBX HJNS BHDGVBEDHUWBNXHSJBDHEBDJSNHJSDEVJDFEHUQNDJWS BEVDHEBSWNQHVHEDEJWD BGRHVFHEJBDH</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   MÔ TẢ NỮA NÈ HBSBGHKVXHSABXNKJvXKQWNHUBIOEJHNXHQBVEHGUDOLWQBDVFRHDKBX HJNS BHDGVBEDHUWBNXHSJBDHEBDJSNHJSDEVJDFEHUQNDJWS BEVDHEBSWNQHVHEDEJWD BGRHVFHEJBDHXKQWNHUBIOEJHNXHQBVEHGUDOLWQBDVFRHDKBX HJNS BHDGVBEDHUWBNXHSJBDHEBDJSNHJSDEVJDFEHUQNDJWS BEVDHEBSWNQHVHEDEJWD BGRHVFHEJBDHXKQWNHUBIOEJHNXHQBVEHGUDOLWQBDVFRHDKBX HJNS BHDGVBEDHUWBNXHSJBDHEBDJSNHJSDEVJDFEHUQNDJWS BEVDHEBSWNQHVHEDEJWD BGRHVFHEJBDH</p></body></html>"))
        self.ad_themphim_bang_bl.horizontalHeaderItem(0).setText(_translate("ad_themphim", "ID"))
        self.ad_themphim_bang_bl.horizontalHeaderItem(1).setText(_translate("ad_themphim", "MOVIE ID"))
        self.ad_themphim_bang_bl.horizontalHeaderItem(2).setText(_translate("ad_themphim", "USERNAME"))
        self.ad_themphim_bang_bl.horizontalHeaderItem(3).setText(_translate("ad_themphim", "NỘI DUNG"))
        self.ad_themphim_bang_bl.horizontalHeaderItem(4).setText(_translate("ad_themphim", "HÀNH ĐỘNG"))
        self.ad_trang_qlp_thongtin1_5.setText(_translate("ad_themphim", "RANK:"))
        self.ad_trang_qlp_thongtin1_3.setText(_translate("ad_themphim", "BÌNH LUẬN:"))
        self.ad_trang_qlp_thongtin1_6.setText(_translate("ad_themphim", "YÊU THÍCH:"))
        self.ad_themphim_chonanh.setText(_translate("ad_themphim", "CHỌN"))

    def change_to_add_mode(self):
        _translate = QtCore.QCoreApplication.translate
        self.ad_themphim_title.setPlaceholderText("Nhập tên phim")
        self.ad_themphim_rank.setPlaceholderText("Nhập thứ hạng phim")
        self.ad_themphim_diem.setPlaceholderText("Nhập điểm phim")
        self.ad_themphim_donoitieng.setPlaceholderText("Nhập độ nổi tiếng")
        self.ad_themphim_nguoitheodoi.setPlaceholderText("Nhập số người theo dõi")
        self.ad_themphim_sotap.setPlaceholderText("Nhập số tập phim")
        self.ad_themphim_yeuthich.setPlaceholderText("Nhập số lượt yêu thích")

        # Create a new QWidget to hold input fields
        self.motaphim_content = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.motaphim_content.setGeometry(QtCore.QRect(10, 60, 321, 1351))  # Chiều cao 740 để fit 800
        self.motaphim_content.setObjectName("motaphim_content")

        # Remove the existing QTextBrowser
        self.ad_themphim_motaphim.deleteLater()

        self.ad_themphim_otaphim = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.ad_themphim_otaphim.setGeometry(QtCore.QRect(0, 0, 1061, 351))
        self.ad_themphim_otaphim.setObjectName("ad_themphim_otaphim")
        self.ad_themphim_otaphim.setStyleSheet("""
                            QTextEdit {
                                background-color: rgb(255, 255, 255);
                                color: rgb(0, 0, 0);
                                font-size: 12px;
                                font-family: Arial;
                                border: 1px solid rgb(200, 200, 200);
                                border-radius: 5px;
                                padding: 5px;
                            }   
                        """)
        self.ad_themphim_otaphim.setPlaceholderText("Nhập mô tả phim")

        #Synonyms
        self.ad_themphim_motaphim_synonyms = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_synonyms.setGeometry(QtCore.QRect(10, 10, 321, 41))
        self.ad_themphim_motaphim_synonyms.setText(_translate("ad_themphim", "Synonyms:"))
        self.ad_themphim_motaphim_synonyms_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_synonyms_input.setGeometry(QtCore.QRect(10, 50, 280, 31))

        #Janpanese
        self.ad_themphim_motaphim_janpanese = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_janpanese.setGeometry(QtCore.QRect(10, 90, 321, 41))
        self.ad_themphim_motaphim_janpanese.setText(_translate("ad_themphim", "Janpanese:"))
        self.ad_themphim_motaphim_janpanese_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_janpanese_input.setGeometry(QtCore.QRect(10, 130, 280, 31))


        # Type
        self.ad_themphim_motaphim_type = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_type.setGeometry(QtCore.QRect(10, 170, 321, 41))
        self.ad_themphim_motaphim_type.setText(_translate("ad_themphim", "Type:"))
        self.ad_themphim_motaphim_type_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_type_input.setGeometry(QtCore.QRect(10, 210, 280, 31))

        # Status
        self.ad_themphim_motaphim_status = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_status.setGeometry(QtCore.QRect(10, 250, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_status.setText(_translate("ad_themphim", "Status:"))
        self.ad_themphim_motaphim_status_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_status_input.setGeometry(QtCore.QRect(10, 290, 280, 31))  # Cập nhật vị trí

        # Aired
        self.ad_themphim_motaphim_aired = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_aired.setGeometry(QtCore.QRect(10, 330, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_aired.setText(_translate("ad_themphim", "Aired:"))
        self.ad_themphim_motaphim_aired_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_aired_input.setGeometry(QtCore.QRect(10, 370, 280, 31))  # Cập nhật vị trí

        # Premiered
        self.ad_themphim_motaphim_premiered = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_premiered.setGeometry(QtCore.QRect(10, 410, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_premiered.setText(_translate("ad_themphim", "Premiered:"))
        self.ad_themphim_motaphim_premiered_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_premiered_input.setGeometry(QtCore.QRect(10, 450, 280, 31))  # Cập nhật vị trí

        # Broadcast
        self.ad_themphim_motaphim_broadcast = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_broadcast.setGeometry(QtCore.QRect(10, 490, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_broadcast.setText(_translate("ad_themphim", "Broadcast:"))
        self.ad_themphim_motaphim_broadcast_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_broadcast_input.setGeometry(QtCore.QRect(10, 530, 280, 31))  # Cập nhật vị trí

        # Producers
        self.ad_themphim_motaphim_producers = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_producers.setGeometry(QtCore.QRect(10, 570, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_producers.setText(_translate("ad_themphim", "Producers:"))
        self.ad_themphim_motaphim_producers_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_producers_input.setGeometry(QtCore.QRect(10, 610, 280, 31))  # Cập nhật vị trí

        # Licensors
        self.ad_themphim_motaphim_licensors = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_licensors.setGeometry(QtCore.QRect(10, 650, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_licensors.setText(_translate("ad_themphim", "Licensors:"))
        self.ad_themphim_motaphim_licensors_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_licensors_input.setGeometry(QtCore.QRect(10, 690, 280, 31))  # Cập nhật vị trí

        # Studios
        self.ad_themphim_motaphim_studios = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_studios.setGeometry(QtCore.QRect(10, 730, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_studios.setText(_translate("ad_themphim", "Studios:"))
        self.ad_themphim_motaphim_studios_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_studios_input.setGeometry(QtCore.QRect(10, 770, 280, 31))  # Cập nhật vị trí

        # Source
        self.ad_themphim_motaphim_source = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_source.setGeometry(QtCore.QRect(10, 810, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_source.setText(_translate("ad_themphim", "Source:"))
        self.ad_themphim_motaphim_source_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_source_input.setGeometry(QtCore.QRect(10, 850, 280, 31))  # Cập nhật vị trí

        # Genres
        self.ad_themphim_motaphim_genres = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_genres.setGeometry(QtCore.QRect(10, 890, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_genres.setText(_translate("ad_themphim", "Genres:"))
        self.ad_themphim_motaphim_genres_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_genres_input.setGeometry(QtCore.QRect(10, 930, 280, 31))  # Cập nhật vị trí

        # Demographic
        self.ad_themphim_motaphim_demographic = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_demographic.setGeometry(QtCore.QRect(10, 970, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_demographic.setText(_translate("ad_themphim", "Demographic:"))
        self.ad_themphim_motaphim_demographic_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_demographic_input.setGeometry(QtCore.QRect(10, 1010, 280, 31))  # Cập nhật vị trí

        # Duration
        self.ad_themphim_motaphim_duration = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_duration.setGeometry(QtCore.QRect(10, 1050, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_duration.setText(_translate("ad_themphim", "Duration:"))
        self.ad_themphim_motaphim_duration_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_duration_input.setGeometry(QtCore.QRect(10, 1090, 280, 31))  # Cập nhật vị trí

        # Rating
        self.ad_themphim_motaphim_rating = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_rating.setGeometry(QtCore.QRect(10, 1130, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_rating.setText(_translate("ad_themphim", "Rating:"))
        self.ad_themphim_motaphim_rating_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_rating_input.setGeometry(QtCore.QRect(10, 1170, 280, 31))  # Cập nhật vị trí

        # Link
        self.ad_themphim_motaphim_link = QtWidgets.QLabel(parent=self.motaphim_content)
        self.ad_themphim_motaphim_link.setGeometry(QtCore.QRect(10, 1210, 321, 41))  # Cập nhật vị trí
        self.ad_themphim_motaphim_link.setText(_translate("ad_themphim", "Link:"))
        self.ad_themphim_motaphim_link_input = QtWidgets.QLineEdit(parent=self.motaphim_content)
        self.ad_themphim_motaphim_link_input.setGeometry(QtCore.QRect(10, 1250, 280, 31))  # Cập nhật vị trí

        # Apply consistent styling to input fields
        input_widgets = [
            self.ad_themphim_motaphim_synonyms_input,
            self.ad_themphim_motaphim_janpanese_input,
            self.ad_themphim_motaphim_type_input,
            self.ad_themphim_motaphim_status_input,
            self.ad_themphim_motaphim_aired_input,
            self.ad_themphim_motaphim_premiered_input,
            self.ad_themphim_motaphim_broadcast_input,
            self.ad_themphim_motaphim_producers_input,
            self.ad_themphim_motaphim_licensors_input,
            self.ad_themphim_motaphim_studios_input,
            self.ad_themphim_motaphim_source_input,
            self.ad_themphim_motaphim_genres_input,
            self.ad_themphim_motaphim_demographic_input,
            self.ad_themphim_motaphim_duration_input,
            self.ad_themphim_motaphim_rating_input,
            self.ad_themphim_motaphim_link_input
        ]
        for widget in input_widgets:
            widget.setStyleSheet("""
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                font-size: 12px;
                font-family: Arial;
                border: 1px solid rgb(200, 200, 200);
                border-radius: 5px;
                padding: 5px;
            """)
            

    def change_to_edit_mode(self, film_data, characters_data):
        self.change_to_add_mode()

        self.ad_themphim_title.setText(film_data['title'])
        self.ad_themphim_rank.setText(str(film_data['rank']))  # Chuyển đổi thành chuỗi
        self.ad_themphim_diem.setText(str(film_data['score']))  # Chuyển đổi thành chuỗi
        self.ad_themphim_donoitieng.setText(str(film_data['popularity']))  # Chuyển đổi thành chuỗi
        self.ad_themphim_nguoitheodoi.setText(str(film_data['members']))  # Chuyển đổi thành chuỗi
        self.ad_themphim_sotap.setText(str(film_data['episodes']))  # Chuyển đổi thành chuỗi
        self.ad_themphim_yeuthich.setText(str(film_data['favorites']))  # Chuyển đổi thành chuỗi
        self.ad_themphim_otaphim.setHtml(film_data['synopsis'])
        self.ad_themphim_motaphim_synonyms_input.setText(film_data['synonyms'])
        self.ad_themphim_motaphim_janpanese_input.setText(film_data['japanese'])
        self.ad_themphim_motaphim_type_input.setText(film_data['type'])
        self.ad_themphim_motaphim_status_input.setText(film_data['status'])
        self.ad_themphim_motaphim_aired_input.setText(film_data['aired'])
        self.ad_themphim_motaphim_premiered_input.setText(film_data['premiered'])
        self.ad_themphim_motaphim_broadcast_input.setText(film_data['broadcast'])
        self.ad_themphim_motaphim_producers_input.setText(film_data['producers'])
        self.ad_themphim_motaphim_licensors_input.setText(film_data['licensors'])
        self.ad_themphim_motaphim_studios_input.setText(film_data['studios'])
        self.ad_themphim_motaphim_source_input.setText(film_data['source'])
        self.ad_themphim_motaphim_genres_input.setText(film_data['genres'])
        self.ad_themphim_motaphim_demographic_input.setText(film_data['demographic'])
        self.ad_themphim_motaphim_duration_input.setText(film_data['duration'])
        self.ad_themphim_motaphim_rating_input.setText(film_data['rating'])
        self.ad_themphim_motaphim_link_input.setText(film_data['link'])

        # Populate the character table with the loaded data
        self.ad_themphim_bang_nhanvat.setRowCount(len(characters_data))
        for row, char in enumerate(characters_data):
            name_link_character = QTableWidgetItem(char.get("name", "N/A"))
            font = name_link_character.font()
            font.setUnderline(True)
            name_link_character.setFont(font)
            name_link_character.setData(Qt.ItemDataRole.UserRole, char.get("link", "N/A"))

            role_character = QTableWidgetItem(char.get("role", "N/A"))

            name_link_actor = QTableWidgetItem(char.get("voice_actor", "N/A"))
            font = name_link_actor.font()
            font.setUnderline(True)
            name_link_actor.setFont(font)
            name_link_actor.setData(Qt.ItemDataRole.UserRole, char.get("voice_actor_link", "N/A"))

            country_actor = QTableWidgetItem(char.get("voice_actor_country", "N/A"))

            self.ad_themphim_bang_nhanvat.setItem(row, 0, name_link_character)
            self.ad_themphim_bang_nhanvat.setItem(row, 1, role_character)
            self.ad_themphim_bang_nhanvat.setItem(row, 2, name_link_actor)
            self.ad_themphim_bang_nhanvat.setItem(row, 3, country_actor)

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ad_themphim = QtWidgets.QMainWindow()
    ui = Ui_ad_themphim()
    ui.setupUi(ad_themphim)
    ui.change_to_add_mode()
    ad_themphim.show()
    sys.exit(app.exec())