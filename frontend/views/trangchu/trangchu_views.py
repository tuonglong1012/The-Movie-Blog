from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QApplication,
    QHBoxLayout, QPushButton, QScrollArea, QSizePolicy,
    QDialog, QComboBox, QSpinBox
)
from PyQt5.QtGui import QFont, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, pyqtSignal
from base_window import BaseWindow
import sys
from ..chat_lounge_views import AnimeWatchApp
from ..movie_detail_views import AnimeDetailWindow
from controllers.trangchu_controller import get_all_movies


movies = get_all_movies()
if "error" in movies:
    print("Lỗi:", movies["error"])
else:
    for movie in movies:
        print(movie["title"], "-", movie["score"])
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class VerticalLine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(1)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(224, 224, 224), 1)
        painter.setPen(pen)
        painter.drawLine(0, 0, 0, self.height())


class AnimeTooltip(QWidget):
    def __init__(self, title, description, info, parent=None):
        super().__init__(parent, Qt.ToolTip)
        self.setWindowFlags(Qt.ToolTip)
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #999;
                border-radius: 6px;
                padding: 0px;
            }
            QLabel.title-bar {
                background-color: #4464b2;
                color: white;
                font-weight: bold;
                font-size: 10pt;
                padding: 6px 10px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QLabel.section {
                padding: 6px 10px;
                font-size: 9pt;
                color: #333;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel(title)
        title_label.setObjectName("title")
        title_label.setProperty("class", "title-bar")
        title_label.setStyleSheet("background-color: #4464b2; color: white; font-weight: bold; font-size: 10pt; padding: 6px 10px; border-top-left-radius: 6px; border-top-right-radius: 6px;")

        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_label.setProperty("class", "section")
        desc_label.setStyleSheet("padding: 6px 10px; font-size: 9pt; color: #333;")

        info_label = QLabel(info)
        info_label.setWordWrap(True)
        info_label.setProperty("class", "section")
        info_label.setStyleSheet("padding: 6px 10px; font-size: 9pt; color: #333;")

        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addWidget(info_label)


class AddAnimeDialog(QDialog):
    def __init__(self, anime_title, total_eps, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Anime to My List")
        self.setMinimumSize(500, 320)
        self.setStyleSheet("""
            QLabel { font-size: 11pt; }
            QComboBox, QSpinBox { font-size: 11pt; min-height: 28px; }
            QPushButton { min-width: 90px; padding: 6px 14px; font-size: 10.5pt; }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 20)
        layout.setSpacing(22)

        title_label = QLabel(f"<b>Anime Title:</b> <span style='color:#1c3f94'>{anime_title}</span>")
        title_label.setTextFormat(Qt.RichText)
        layout.addWidget(title_label)

        status_row = QHBoxLayout()
        status_label = QLabel("Status")
        status_label.setFixedWidth(130)
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Watching", "Completed", "On-Hold", "Dropped", "Plan to Watch"])
        status_row.addWidget(status_label)
        status_row.addWidget(self.status_combo)
        layout.addLayout(status_row)

        eps_row = QHBoxLayout()
        eps_label = QLabel("Episodes Watched")
        eps_label.setFixedWidth(130)
        self.eps_spinbox = QSpinBox()
        self.eps_spinbox.setRange(0, total_eps)
        eps_total = QLabel(f"/ {total_eps}")
        eps_row.addWidget(eps_label)
        eps_row.addWidget(self.eps_spinbox)
        eps_row.addWidget(eps_total)
        eps_row.addStretch(1)
        layout.addLayout(eps_row)

        score_row = QHBoxLayout()
        score_label = QLabel("Your Score")
        score_label.setFixedWidth(130)
        self.score_combo = QComboBox()
        self.score_combo.addItem("Select score")
        scores = [
            "(10) Masterpiece", "(9) Great", "(8) Very Good", "(7) Good", "(6) Fine",
            "(5) Average", "(4) Bad", "(3) Very Bad", "(2) Horrible", "(1) Appalling"
        ]
        self.score_combo.addItems(scores)
        score_row.addWidget(score_label)
        score_row.addWidget(self.score_combo)
        layout.addLayout(score_row)

        button_row = QHBoxLayout()
        button_row.addStretch()
        self.submit_btn = QPushButton("Submit")
        self.cancel_btn = QPushButton("Cancel")
        self.submit_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        button_row.addWidget(self.submit_btn)
        button_row.addWidget(self.cancel_btn)
        layout.addLayout(button_row)

    def get_data(self):
        return {
            "status": self.status_combo.currentText(),
            "episodes": self.eps_spinbox.value(),
            "score": self.score_combo.currentText() if self.score_combo.currentIndex() != 0 else None
        }

class AnimeListPage(BaseWindow):
    def __init__(self, chat_window=None):
        super().__init__(
            user_info=chat_window.user_info if chat_window else None,
            avatar_pixmap=chat_window.avatar_pixmap if chat_window else None
        )
        self.chat_window = chat_window
        self.setWindowTitle("Anime List")
        self.showMaximized()

        for widget in self.findChildren(QLabel):
            if widget.text() == "ChibiChat":
                clickable = ClickableLabel("ChibiChat")
                clickable.setFont(widget.font())
                clickable.setStyleSheet(widget.styleSheet())
                clickable.setAlignment(widget.alignment())
                clickable.setCursor(Qt.PointingHandCursor)
                clickable.clicked.connect(self.return_to_chat)

                parent = widget.parentWidget()
                layout = parent.layout()
                index = layout.indexOf(widget)
                layout.removeWidget(widget)
                widget.deleteLater()
                layout.insertWidget(index, clickable)
                break

        content_widget = QWidget()
        content_widget.setFixedWidth(1000)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 80, 20, 20)
        content_layout.setSpacing(2)

        heading = QLabel("Top Anime List")
        heading.setFont(QFont("Arial", 18, QFont.Bold))
        heading.setAlignment(Qt.AlignCenter)

        content_layout.addWidget(heading)
        content_layout.addWidget(self.create_anime_list_widget())

        centered_layout = QHBoxLayout()
        centered_layout.addStretch(1)
        centered_layout.addWidget(content_widget, 6)
        centered_layout.addStretch(1)
        self.main_layout.addLayout(centered_layout)

    def create_vertical_line(self):
        return VerticalLine()

    def create_anime_list_widget(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                background: transparent;
                width: 6px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #bdc3c7;
                min-height: 25px;
                border-radius: 3px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #ecf0f1;
            }
            QScrollBar::sub-line:vertical,
            QScrollBar::add-line:vertical {
                height: 0;
            }
            QScrollBar::sub-page:vertical,
            QScrollBar::add-page:vertical {
                background: none;
            }
        """)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.create_header_row())

        anime_data = [
            {
                "rank": i + 1,
                "title": f"Anime Title {i + 1}",
                "info": f"TV ({12 + i % 5} eps)\n2022 - 2023\n{1_000_000 + i * 12345} members",
                "score": f"{9.5 - (i * 0.1):.2f}"
            } for i in range(20)
        ]

        for i, anime in enumerate(anime_data):
            layout.addWidget(self.create_data_row(anime, i))

        scroll_area.setWidget(container)
        return scroll_area

    def create_header_row(self):
        row = QWidget()
        row.setFixedHeight(30)
        row.setStyleSheet("background-color: #4464b2;")
        row_layout = QHBoxLayout(row)
        row_layout.setContentsMargins(5, 4, 5, 4)
        row_layout.setSpacing(0)

        headers = ["Rank", "Title", "Score", "Your Score", "Status"]
        stretches = [1, 6, 2, 2, 2]

        for i, (text, stretch) in enumerate(zip(headers, stretches)):
            lbl = QLabel(text)
            lbl.setFont(QFont("Arial", 8))
            lbl.setStyleSheet("color: white; padding: 0px;")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            lbl.setFixedHeight(20)
            row_layout.addWidget(lbl, stretch)
            if i < len(headers) - 1:
                row_layout.addWidget(self.create_vertical_line())

        return row

    def create_data_row(self, anime, index):
        row = QWidget()
        row.setMinimumHeight(100)
        bg_color = "#ffffff" if index % 2 == 0 else "#f7f7f7"
        row.setStyleSheet(f"background-color: {bg_color};")
        row_layout = QHBoxLayout(row)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(0)

        rank = QLabel(str(anime['rank']))
        rank.setFont(QFont("Arial", 12, QFont.Bold))
        rank.setAlignment(Qt.AlignCenter)
        rank.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        row_layout.addWidget(rank, 1)
        row_layout.addWidget(self.create_vertical_line())

        title_widget = QWidget()
        title_layout = QHBoxLayout(title_widget)
        title_layout.setContentsMargins(20, 0, 0, 0)
        title_layout.setSpacing(10)
        title_layout.setAlignment(Qt.AlignVCenter)

        thumb = QLabel()
        thumb.setObjectName("animeThumbnail")
        thumb.setFixedSize(70, 80)
        thumb.setStyleSheet("""
            QLabel#animeThumbnail {
                border: 1px solid #ccc;
                background-color: #f0f0f0;
                image: url(default_avatar.png);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)

        text_container = QWidget()
        text_layout = QVBoxLayout(text_container)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(2)

        title_label = QLabel(f"<b>{anime['title']}</b>")
        title_label.setFont(QFont("Arial", 11, QFont.Bold))
        title_label.setStyleSheet("color: #1c3f94; margin: 0; padding: 0;")
        title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title_label.setWordWrap(True)
        title_label.setCursor(Qt.PointingHandCursor)

        # Tooltip logic
        tooltip_info = f"""<b>Genres:</b> Adventure, Drama<br>
        <b>Status:</b> Finished Airing<br>
        <b>Type:</b> TV<br>
        <b>Episodes:</b> 28<br>
        <b>Score:</b> {anime['score']}<br>
        <b>Members:</b> 1,112,242"""

        tooltip = AnimeTooltip(anime['title'], "During their decade-long quest to defeat the Demon King, the members of the hero’s party forge bonds through battles.", tooltip_info)

        title_label.installEventFilter(self)
        title_label._tooltip_widget = tooltip

        # OPEN DETAIL WINDOW ON CLICK
        self.detail_windows = getattr(self, 'detail_windows', [])

        def show_detail_window():
            anime_data = {
                "title": anime['title'],
                "type": "TV",
                "episodes": 28,
                "status": "Finished Airing",
                "score": anime['score'],
                "members": "1,112,242",
                "synopsis": "During their decade-long quest to defeat the Demon King, the members of the hero’s party forge bonds through battles."
            }
            detail_win = AnimeDetailWindow(anime_data, parent=self) 
            self.detail_windows.append(detail_win)
            detail_win.show()

        title_label.mousePressEvent = lambda event: show_detail_window()

        tooltip_info = f"""<b>Genres:</b> Adventure, Drama<br>
    <b>Status:</b> Finished Airing<br>
    <b>Type:</b> TV<br>
    <b>Episodes:</b> 28<br>
    <b>Score:</b> {anime['score']}<br>
    <b>Members:</b> 1,112,242"""

        tooltip = AnimeTooltip(anime['title'], "During their decade-long quest to defeat the Demon King, the members of the hero’s party forge bonds through battles.", tooltip_info)
        title_label.installEventFilter(self)
        title_label._tooltip_widget = tooltip

        text_layout.addWidget(title_label)
        text_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        title_layout.addWidget(thumb)
        title_layout.addWidget(text_container)
        title_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        row_layout.addWidget(title_widget, 6, Qt.AlignVCenter)
        row_layout.addWidget(self.create_vertical_line())

        score = QLabel(f"★ {anime['score']}")
        score.setFont(QFont("Arial", 11, QFont.Bold))
        score.setStyleSheet("color: #e3b400;")
        score.setAlignment(Qt.AlignCenter)
        score.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        row_layout.addWidget(score, 2)
        row_layout.addWidget(self.create_vertical_line())

        your_score = QLabel("☆ N/A")
        your_score.setFont(QFont("Arial", 10))
        your_score.setStyleSheet("color: #aaa;")
        your_score.setAlignment(Qt.AlignCenter)
        your_score.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        row_layout.addWidget(your_score, 2)
        row_layout.addWidget(self.create_vertical_line())

        status_widget = QWidget()
        status_layout = QHBoxLayout(status_widget)
        status_layout.setContentsMargins(0, 0, 0, 0)
        status_layout.setAlignment(Qt.AlignCenter)

        status_button = QPushButton("Add to List")
        status_button.setCursor(Qt.PointingHandCursor)
        status_button.setFixedSize(100, 30)
        status_button.setStyleSheet("""
            QPushButton {
                background-color: #2e51a2;
                color: white;
                border: none;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #1d3a85;
            }
        """)

        status_toggle = QPushButton("")
        status_toggle.setFont(QFont("Arial", 10))
        status_toggle.setCursor(Qt.PointingHandCursor)
        status_toggle.setStyleSheet("""
            QPushButton {
                color: #28a745;
                border: 1px solid #28a745;
                padding: 3px 10px;
                border-radius: 4px;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #e6f4ea;
            }
        """)
        status_toggle.hide()

        status_layout.addWidget(status_button)
        status_layout.addWidget(status_toggle)
        row_layout.addWidget(status_widget, 2, alignment=Qt.AlignCenter)

        def open_add_dialog():
            dialog = AddAnimeDialog(anime['title'], total_eps=28, parent=self)
            if dialog.exec_() == QDialog.Accepted:
                data = dialog.get_data()
                if data['score']:
                    score_val = data['score'].split(')')[0].strip('(')
                    your_score.setText(f"★ {score_val}")
                    your_score.setStyleSheet("color: #e3b400; font-weight: bold;")
                else:
                    your_score.setText("☆ N/A")
                    your_score.setStyleSheet("color: #aaa;")

                if data['status']:
                    status_toggle.setText(data['status'])
                    status_toggle.show()
                    status_button.hide()

        def reopen_dialog():
            dialog = AddAnimeDialog(anime['title'], total_eps=28, parent=self)
            if dialog.exec_() == QDialog.Accepted:
                data = dialog.get_data()
                if data['score']:
                    score_val = data['score'].split(')')[0].strip('(')
                    your_score.setText(f"★ {score_val}")
                    your_score.setStyleSheet("color: #e3b400; font-weight: bold;")
                else:
                    your_score.setText("☆ N/A")
                    your_score.setStyleSheet("color: #aaa;")

                if data['status']:
                    status_toggle.setText(data['status'])
                else:
                    status_toggle.hide()
                    status_button.show()

        status_button.clicked.connect(open_add_dialog)
        status_toggle.clicked.connect(reopen_dialog)

        return row


    def eventFilter(self, source, event):
        if isinstance(source, QLabel) and hasattr(source, '_tooltip_widget'):
            if event.type() == event.Enter:
                pos = source.mapToGlobal(source.rect().bottomLeft())
                source._tooltip_widget.move(pos)
                source._tooltip_widget.show()
            elif event.type() == event.Leave:
                source._tooltip_widget.hide()
        return super().eventFilter(source, event)

    def return_to_chat(self):
        if self.chat_window:
            self.chat_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_win = AnimeWatchApp()
    win = AnimeListPage(chat_window=chat_win)
    win.show()

    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    win.setGeometry(rect)

    sys.exit(app.exec_())