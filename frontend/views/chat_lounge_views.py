import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton, QToolButton,
    QFrame, QSizePolicy, QFileDialog, QInputDialog, QScrollArea,
    QMessageBox, QLineEdit
)
from PyQt5.QtCore import Qt, QPoint, QSize, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QIcon, QPainter, QPainterPath, QRegion

import requests

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class AnimeWatchApp(QMainWindow):
    def __init__(self, user_info=None, avatar_pixmap=None):
        super().__init__()
        self.setWindowTitle("Anime Watch")
        self.setGeometry(100, 100, 1000, 600)
        self.user_info = {
            "Name": "Your Name",
            "Email": "you@example.com",
            "Birthday": "01-01-2000"
        }
        self.avatar_pixmap = None
        self.init_ui()

    def open_chibichat_window(self):
        from trangchu_views import AnimeListPage  
        self.anime_list_window = AnimeListPage(chat_window=self)
        self.anime_list_window.show()
        self.hide()

    def init_ui(self):
        main = QWidget(self)
        self.setCentralWidget(main)
        main_layout = QVBoxLayout(main)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        header = QWidget(main)
        header.setFixedHeight(70)
        header.setStyleSheet("background-color: #B0E0E6;")
        hdr_lay = QHBoxLayout(header)
        hdr_lay.setContentsMargins(20, 10, 20, 10)

        proj_lbl = ClickableLabel("ChibiChat", header)
        proj_lbl.setFont(QFont("Matura MT Script Capitals", 20, QFont.Bold))
        proj_lbl.setStyleSheet("color: #000; background-color: #D0F0F7; border-radius: 15px; margin-right: 2px")
        proj_lbl.clicked.connect(self.open_chibichat_window)
        hdr_lay.addWidget(proj_lbl, alignment=Qt.AlignLeft)

        left_spacer = QWidget(header)
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        hdr_lay.addWidget(left_spacer)

        blog_lbl = QLabel("Activities", header)
        blog_lbl.setFont(QFont("Matura MT Script Capitals", 16, QFont.Bold))
        blog_lbl.setStyleSheet("color: #000;")
        hdr_lay.addWidget(blog_lbl, alignment=Qt.AlignCenter)

        right_spacer = QWidget(header)
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        hdr_lay.addWidget(right_spacer)

        self.user_btn = QToolButton(header)
        self.user_btn.setFixedSize(50, 50)
        self.user_btn.setStyleSheet("""
            QToolButton { border: 2px solid #333; border-radius: 25px; background: white; border-color: white}
        """)

        avatar_path = "default_avatar.png"
        size = self.user_btn.width()
        pixmap = QPixmap(avatar_path)

        if pixmap.isNull():
            print("Failed to load default avatar:", avatar_path)
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
            self.avatar_pixmap = circular
            self.user_btn.setMask(circular.mask())

        self.user_btn.clicked.connect(self.toggle_dropdown)
        hdr_lay.addWidget(self.user_btn, alignment=Qt.AlignRight)

        main_layout.addWidget(header)

        body = QWidget(main)
        body.setStyleSheet("background-color: #F0F8FF;")
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        sidebar_scroll = QScrollArea(body)
        sidebar_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sidebar_scroll.setFixedWidth(300)
        sidebar_scroll.setWidgetResizable(True)
        sidebar_scroll.setStyleSheet("background-color: #0C5776;")
        sidebar_scroll.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical { background: transparent; width: 6px; margin: 0px; }
            QScrollBar::handle:vertical { background: #bdc3c7; min-height: 25px; border-radius: 3px; }
            QScrollBar::handle:vertical:hover { background: #ecf0f1; }
            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical { height: 0; }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical { background: none; }
        """)

        sidebar_container = QWidget()
        sb_lay = QVBoxLayout(sidebar_container)
        sb_lay.setContentsMargins(15, 15, 15, 15)
        sb_lay.setSpacing(20)

        title = QLabel("Top 10", sidebar_container)
        title.setFont(QFont("Times New Roman", 22, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignHCenter)
        sb_lay.addWidget(title)

        top_anime = [
            "Fullmetal Alchemist", "Attack on Titan", "Death Note",
            "Steins;Gate", "Hunter x Hunter", "My Hero Academia",
            "Naruto", "One Piece", "Demon Slayer", "Cowboy Bebop"
        ]

        self.chat_store = {}
        self.current_anime = None

        for idx, name in enumerate(top_anime, start=1):
            item_container = QWidget(sidebar_container)
            item_lay = QHBoxLayout(item_container)
            item_lay.setContentsMargins(0, 5, 0, 5)
            item_lay.setSpacing(10)
            item_lay.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            num_lbl = QLabel(str(idx), item_container)
            num_lbl.setFont(QFont("Times New Roman", 14))
            num_lbl.setStyleSheet("color: white;")
            num_lbl.setFixedWidth(15)
            num_lbl.setAlignment(Qt.AlignLeft)
            item_lay.addWidget(num_lbl)

            block = QWidget(item_container)
            block_lay = QVBoxLayout(block)
            block_lay.setContentsMargins(0, 0, 0, 0)
            block_lay.setSpacing(4)

            name_lbl = QLabel(name, block)
            name_lbl.setFont(QFont("Times New Roman", 12))
            name_lbl.setStyleSheet("color: white;")
            name_lbl.setAlignment(Qt.AlignLeft)
            block_lay.addWidget(name_lbl)

            thumb = QFrame(block)
            thumb.setFrameShape(QFrame.StyledPanel)
            thumb.setStyleSheet("border: 2px solid white; border-radius: 6px;")
            thumb.setFixedSize(200, 100)
            block_lay.addWidget(thumb)

            item_lay.addWidget(block)

            star_btn = QPushButton("☆", item_container)
            star_btn.setFont(QFont("Arial", 20))
            star_btn.setStyleSheet("color: yellow; background: none; border: none; margin-top: 50px")
            star_btn.setCheckable(True)

            def handle_star(checked, anime=name, btn=star_btn):
                if checked:
                    btn.setText("★")
                    self.current_anime = anime
                    self.load_messages(anime)
                else:
                    reply = QMessageBox.question(
                        self, "Confirm Unfavorite",
                        "Are you sure you want to unfavourite it?",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                    )
                    if reply == QMessageBox.Yes:
                        btn.setText("☆")
                        if self.current_anime == anime:
                            self.current_anime = None
                            self.load_messages(None)
                    else:
                        btn.setChecked(True)
                        btn.setText("★")

            star_btn.clicked.connect(handle_star)

            star_container = QWidget(item_container)
            star_vlay = QVBoxLayout(star_container)
            star_vlay.setContentsMargins(0, 0, 0, 0)
            star_vlay.setSpacing(0)
            star_vlay.addSpacing(8)
            star_vlay.addWidget(star_btn, alignment=Qt.AlignHCenter)
            star_vlay.addStretch()
            item_lay.addWidget(star_container)

            if idx < len(top_anime):
                sep = QFrame(sidebar_container)
                sep.setFrameShape(QFrame.HLine)
                sep.setStyleSheet("color: white;")
                sep.setFixedWidth(200)
                sb_lay.addWidget(sep, alignment=Qt.AlignHCenter)

            sb_lay.addWidget(item_container)

        sb_lay.addStretch()
        sidebar_scroll.setWidget(sidebar_container)
        body_layout.addWidget(sidebar_scroll)

        chat_container = QWidget(body)
        chat_container.setStyleSheet("background-color: white; margin-bottom: 20px;")
        chat_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        chat_layout = QVBoxLayout(chat_container)
        chat_layout.setContentsMargins(10, 10, 10, 10)
        chat_layout.setSpacing(8)

        self.msg_scroll = QScrollArea(chat_container)
        self.msg_scroll.setWidgetResizable(True)
        self.feed_widget = QWidget()
        self.feed_layout = QVBoxLayout(self.feed_widget)
        self.feed_layout.addStretch()
        self.msg_scroll.setWidget(self.feed_widget)

        self.input_line = QLineEdit(chat_container)
        self.input_line.setPlaceholderText("Write your caption…")
        self.input_line.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 12px;
                font-size: 20px;
                min-height: 36px;
            }
        """)
        send_btn = QPushButton("Send", chat_container)
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                border: none;
                border-radius: 6px;
                padding: 8px 20px;
                font-size: 16px;
                min-height: 36px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        send_btn.clicked.connect(self.send_message)

        input_row = QWidget(chat_container)
        row_lay = QHBoxLayout(input_row)
        row_lay.setContentsMargins(0, 0, 0, 0)
        row_lay.addWidget(self.input_line)
        row_lay.addWidget(send_btn)

        chat_layout.addWidget(self.msg_scroll)
        chat_layout.addWidget(input_row)
        body_layout.addWidget(chat_container, 1)
        main_layout.addWidget(body, 1)

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

    def create_post_widget_with_user(self, text):
        post_widget = QWidget()
        post_layout = QHBoxLayout(post_widget)
        post_layout.setContentsMargins(10, 5, 10, 5)
        post_layout.setSpacing(10)
        post_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        avatar_wrapper = QWidget()
        avatar_wrapper.setFixedSize(40, 40)
        avatar_wrapper.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        wrapper_layout = QVBoxLayout(avatar_wrapper)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(0)

        avatar_label = QLabel()
        avatar_label.setFixedSize(40, 40)
        avatar_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        if self.avatar_pixmap:
            original = self.avatar_pixmap
            side = min(original.width(), original.height())
            x = (original.width() - side) // 2
            y = (original.height() - side) // 2
            square = original.copy(x, y, side, side)

            scaled = square.scaled(40, 40, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            circular = QPixmap(40, 40)
            circular.fill(Qt.transparent)

            painter = QPainter(circular)
            painter.setRenderHint(QPainter.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, 40, 40)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, scaled)
            painter.end()

            avatar_label.setPixmap(circular)
            avatar_label.setMask(circular.mask())

        wrapper_layout.addWidget(avatar_label)

        # Right side: Username and message
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(4)

        name_label = QLabel(self.user_info.get("Name", "Anonymous"))
        name_label.setFont(QFont("Arial", 10, QFont.Bold))
        name_label.setStyleSheet("color: #2c3e50;")

        msg_label = QLabel(text)
        msg_label.setWordWrap(True)
        msg_label.setFont(QFont("Arial", 12))
        msg_label.setStyleSheet("""
            background-color: #F0F8FF;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
        """)

        right_layout.addWidget(name_label)
        right_layout.addWidget(msg_label)

        post_layout.addWidget(avatar_wrapper)
        post_layout.addWidget(right_container)

        return post_widget


    def send_message(self):
        text = self.input_line.text().strip()
        if not text or not self.current_anime:
            return
        self.chat_store.setdefault(self.current_anime, []).append(text)
        post = self.create_post_widget_with_user(text)
        self.feed_layout.insertWidget(self.feed_layout.count() - 1, post)
        self.input_line.clear()
        self.msg_scroll.verticalScrollBar().setValue(
            self.msg_scroll.verticalScrollBar().maximum()
        )

    def load_messages(self, anime_name):
        for i in reversed(range(self.feed_layout.count() - 1)):
            w = self.feed_layout.itemAt(i).widget()
            if w:
                w.deleteLater()
        if not anime_name or anime_name not in self.chat_store:
            return
        for msg in self.chat_store[anime_name]:
            post = self.create_post_widget_with_user(msg)
            self.feed_layout.insertWidget(self.feed_layout.count() - 1, post)

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

    def edit_info(self, field, button):
        current = self.user_info[field]
        prompt = f"Enter {field}" + (" (DD-MM-YYYY):" if field == "Birthday" else ":")
        text, ok = QInputDialog.getText(self, f"Edit {field}", prompt, text=current)
        if ok and text:
            self.user_info[field] = text
            button.setText(f"{field}: {text}")

    def on_logout(self):
        QApplication.quit()

    def fetch_top_anime_data(self):
        return []

    def set_thumbnail(self, frame: QFrame, url: str):
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            pix = QPixmap()
            pix.loadFromData(resp.content)
            lbl = QLabel(frame)
            lbl.setPixmap(
                pix.scaled(
                    frame.width(), frame.height(),
                    Qt.KeepAspectRatioByExpanding,
                    Qt.SmoothTransformation
                )
            )
            lbl.setGeometry(0, 0, frame.width(), frame.height())
            lbl.lower()
        except Exception as e:
            print(f"[Thumbnail ERROR] {e}")

    def update_thumbnails(self):
        data = self.fetch_top_anime_data()
        frames = [
            w for w in self.findChildren(QFrame)
            if w.frameShape() == QFrame.StyledPanel and w.size() == QSize(200, 100)
        ]
        for frame, item in zip(frames, data): 
            self.set_thumbnail(frame, item.get("thumbnail_url", ""))

if __name__ == "__main__":
    from trangchu_views import AnimeListPage  
    app = QApplication(sys.argv)
    chat_win = AnimeWatchApp()
    win = AnimeListPage(chat_window=chat_win)
    win.show()
    sys.exit(app.exec_())
