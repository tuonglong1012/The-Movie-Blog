from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QInputDialog,
    QPushButton, QFileDialog, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPainter, QPainterPath
from PyQt5.QtCore import Qt, QPoint, QSize

class BaseWindow(QMainWindow):
    def __init__(self, user_info=None, avatar_pixmap=None):
        super().__init__()
        self.user_info = user_info if user_info else {
            "Name": "Your Name",
            "Email": "you@example.com",
            "Birthday": "01-01-2000"
        }
        self.avatar_pixmap = avatar_pixmap
        self.init_ui()

    def init_ui(self):
        main = QWidget(self)
        self.setCentralWidget(main)
        self.main_layout = QVBoxLayout(main)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        header = QWidget()
        header.setFixedHeight(70)
        header.setStyleSheet("background-color: #D0F0F7;")
        hdr_lay = QHBoxLayout(header)
        hdr_lay.setContentsMargins(20, 10, 20, 10)

        proj_lbl = QLabel("ChibiChat")
        proj_lbl.setFont(QFont("Matura MT Script Capitals", 20, QFont.Bold))
        proj_lbl.setStyleSheet("color: #000; background-color:  #B0E0E6; border-radius: 15px; margin-right: 2px")
        hdr_lay.addWidget(proj_lbl, alignment=Qt.AlignLeft)

        spacer_left = QWidget()
        spacer_left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        hdr_lay.addWidget(spacer_left)

        blog_lbl = QLabel("Anime List")
        blog_lbl.setFont(QFont("Matura MT Script Capitals", 16, QFont.Bold))
        blog_lbl.setStyleSheet("color: #000;")
        hdr_lay.addWidget(blog_lbl, alignment=Qt.AlignCenter)

        spacer_right = QWidget()
        spacer_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        hdr_lay.addWidget(spacer_right)

        self.user_btn = QToolButton()
        self.user_btn.setFixedSize(50, 50)
        self.user_btn.setStyleSheet("QToolButton { border: 2px solid #333; border-radius: 25px; background: white; border-color: white }")
        self.user_btn.clicked.connect(self.toggle_dropdown)

        size = self.user_btn.width()
        if self.avatar_pixmap:
            original = self.avatar_pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        else:
            avatar_path = "default_avatar.png"
            pixmap = QPixmap(avatar_path)
            if pixmap.isNull():
                original = QPixmap(size, size)
                original.fill(Qt.white)
            else:
                original = pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        circular = QPixmap(size, size)
        circular.fill(Qt.transparent)
        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        x = (size - original.width()) // 2
        y = (size - original.height()) // 2
        painter.drawPixmap(x, y, original)
        painter.end()

        self.user_btn.setIcon(QIcon(circular))
        self.user_btn.setIconSize(QSize(size, size))
        self.user_btn.setMask(circular.mask())
        self.avatar_pixmap = circular

        hdr_lay.addWidget(self.user_btn, alignment=Qt.AlignRight)
        self.main_layout.addWidget(header)

        self.dropdown = QWidget(self)
        self.dropdown.setStyleSheet("""
            background-color: #fff;
            border: 1px solid white;
            border-radius: 10px;
        """)
        dd_lay = QVBoxLayout(self.dropdown)
        dd_lay.setContentsMargins(10, 10, 10, 10)
        for field, val in self.user_info.items():
            btn = QToolButton(self.dropdown)
            btn.setText(f"{field}: {val}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("color: #000; text-align: left; padding: 2px 0;")
            btn.clicked.connect(lambda _, f=field, b=btn: self.edit_info(f, b))
            dd_lay.addWidget(btn)
        dd_lay.addSpacing(8)
        change_avatar_btn = QPushButton("Change Avatar", self.dropdown)
        change_avatar_btn.setStyleSheet("color: #000; background: none; border: none; text-align: left; padding: 4px 0;")
        change_avatar_btn.clicked.connect(self.change_avatar)
        dd_lay.addWidget(change_avatar_btn)
        dd_lay.addSpacing(8)
        logout_btn = QPushButton("Log Out", self.dropdown)
        logout_btn.setStyleSheet("color: red; background: none; border: none; text-align: left; padding: 4px 0;")
        logout_btn.clicked.connect(self.on_logout)
        dd_lay.addWidget(logout_btn)
        self.dropdown.setFixedWidth(200)
        self.dropdown.hide()

    def toggle_dropdown(self):
        if self.dropdown.isVisible():
            self.dropdown.hide()
            return
        btn = self.user_btn
        pt_global = btn.mapToGlobal(QPoint(0, btn.height()))
        pt_window = self.mapFromGlobal(pt_global)
        x = pt_window.x() + btn.width() - self.dropdown.width()
        y = pt_window.y() + 8
        self.dropdown.adjustSize()
        self.dropdown.move(x, y)
        self.dropdown.show()
        self.dropdown.raise_()

    def edit_info(self, field, button):
        current = self.user_info[field]
        prompt = f"Enter {field}" + (" (DD-MM-YYYY):" if field == "Birthday" else ":")
        text, ok = QInputDialog.getText(self, f"Edit {field}", prompt, text=current)
        if ok and text:
            self.user_info[field] = text
            button.setText(f"{field}: {text}")

    def change_avatar(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Avatar", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if path:
            size = self.user_btn.width()
            original = QPixmap(path).scaled(
                size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )

            mask = QPixmap(size, size)
            mask.fill(Qt.transparent)
            painter = QPainter(mask)
            painter.setRenderHint(QPainter.Antialiasing)
            circle = QPainterPath()
            circle.addEllipse(0, 0, size, size)
            painter.setClipPath(circle)
            painter.drawPixmap(0, 0, original)
            painter.end()

            self.user_btn.setIcon(QIcon(mask))
            self.user_btn.setIconSize(mask.size())
            self.user_btn.setMask(mask.mask())
            self.avatar_pixmap = mask

            if hasattr(self, "chat_window") and self.chat_window:
                self.chat_window.avatar_pixmap = mask
                self.chat_window.user_btn.setIcon(QIcon(mask))
                self.chat_window.user_btn.setIconSize(mask.size())
                self.chat_window.user_btn.setMask(mask.mask())

    def on_logout(self):
        self.close()