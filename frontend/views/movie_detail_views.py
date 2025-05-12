from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QSpinBox, QPushButton, QSizePolicy, QApplication, QScrollArea, QGridLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from base_window import BaseWindow
import sys

def load_anime_data(anime_id):
    return {
        "title": "Sousou no Frieren",
        "subtitle": "Beyond Journey's End",
        "type": "TV",
        "episodes": 28,
        "status": "Finished Airing",
        "score": "9.1",
        "members": "1,500,000",
        "rank": "#5",
        "popularity": "#15",
        "season": "Fall 2023",
        "studio": "Madhouse",
        "synopsis": (
            "After the defeat of the Demon King, Frieren the elf mage continues her journey "
            "to understand humanity. As her long-lived race outlasts her companions, she reflects "
            "on the bonds they formed and seeks to create new ones in a changing world."
        ),
        "characters": [
            {
                "name": "Frieren", "role": "Main", "image": "frieren.png",
                "voice": {"name": "Tanezaki, Atsumi", "lang": "Japanese", "image": "atsumi.png"}
            },
            {
                "name": "Fern", "role": "Main", "image": "fern.png",
                "voice": {"name": "Ichinose, Kana", "lang": "Japanese", "image": "kana.png"}
            }
        ]
    }


class AnimeDetailWindow(BaseWindow):

    def build_character_voice_grid(self, characters):
        grid = QGridLayout()
        grid.setSpacing(20)
        grid.setContentsMargins(0, 10, 0, 10)

        def create_profile_cell(image_path, name, subtitle):
            layout = QVBoxLayout()
            layout.setSpacing(4)

            image = QLabel()
            pixmap = QPixmap(image_path)
            image.setPixmap(pixmap.scaled(64, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image.setFixedSize(64, 90)

            name_label = QLabel(f"<b>{name}</b>")
            subtitle_label = QLabel(subtitle)
            name_label.setAlignment(Qt.AlignCenter)
            subtitle_label.setAlignment(Qt.AlignCenter)
            name_label.setStyleSheet("font-size: 9pt;")
            subtitle_label.setStyleSheet("font-size: 8pt; color: #555;")

            layout.addWidget(image)
            layout.addWidget(name_label)
            layout.addWidget(subtitle_label)

            container = QFrame()
            container.setLayout(layout)
            container.setStyleSheet("""
                QFrame {
                    background-color: #fdfdfd;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                    padding: 6px;
                }
            """)
            return container

        for i, char in enumerate(characters):
            char_cell = create_profile_cell(char["image"], char["name"], char["role"])
            va = char.get("voice", {})
            va_cell = create_profile_cell(va.get("image", ""), va.get("name", "N/A"), va.get("lang", "Unknown"))

            grid.addWidget(char_cell, i, 0)
            grid.addWidget(va_cell, i, 1)

        return grid

    def build_review_list(self, reviews):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        for review in reviews:
            container = QFrame()
            container.setStyleSheet("""
                QFrame {
                    background-color: #fcfcfc;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 10px;
                }
            """)
            container_layout = QVBoxLayout(container)
            container_layout.setSpacing(8)

            header = QHBoxLayout()
            avatar = QLabel()
            avatar.setFixedSize(40, 40)
            avatar.setPixmap(QPixmap(review["avatar"]).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            username = QLabel(f"<b>{review['username']}</b>")
            date = QLabel(review["date"])
            date.setStyleSheet("color: #888; font-size: 8pt;")
            header.addWidget(avatar)
            header.addWidget(username)
            header.addStretch(1)
            header.addWidget(date)

            tag_line = QHBoxLayout()
            for tag in review.get("tags", []):
                tag_label = QLabel(tag)
                tag_label.setStyleSheet("""
                    QLabel {
                        background-color: #e0e0e0;
                        border-radius: 4px;
                        padding: 2px 6px;
                        font-size: 8pt;
                        color: #444;
                    }
                """)
                tag_line.addWidget(tag_label)
            tag_line.addStretch(1)

            content = QLabel(review["content"])
            content.setWordWrap(True)
            content.setStyleSheet("font-size: 9pt; color: #333;")

            container_layout.addLayout(header)
            container_layout.addLayout(tag_line)
            container_layout.addWidget(content)
            layout.addWidget(container)

        return layout
    

    def __init__(self, anime_data, parent=None):
        super().__init__(
            user_info=parent.user_info if parent else None,
            avatar_pixmap=parent.avatar_pixmap if parent else None
        )

        if parent:
            parent.close()

        self.setWindowTitle(anime_data.get("title", "Anime Details"))
        self.showMaximized()

        return_button_layout = QHBoxLayout()
        return_button_layout.setContentsMargins(20, 10, 0, 0)
        return_button = QPushButton("⟵ Return to List")
        return_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 10pt; padding: 6px 12px; border: none;")
        return_button.setFixedWidth(150)
        return_button.clicked.connect(self.return_to_list)
        return_button_layout.addWidget(return_button, alignment=Qt.AlignLeft)
        header_wrapper = QWidget()
        header_wrapper.setStyleSheet("background: transparent; border: none;")
        header_wrapper.setLayout(return_button_layout)
        self.main_layout.addWidget(header_wrapper)
        return_button_layout.setSpacing(0)
        return_button_layout.setContentsMargins(20, 10, 0, 0)

        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(30, 30, 30, 30)
        content_layout.setSpacing(30)

        poster_layout = QVBoxLayout()
        poster_layout.setSpacing(2)
        poster_label = QLabel()
        poster_label.setFixedSize(200, 280)
        poster_label.setStyleSheet("border: 1px solid #ccc; background-color: #eee;")
        pixmap = QPixmap("default_avatar.png")
        if not pixmap.isNull():
            poster_label.setPixmap(pixmap.scaled(200, 280, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        poster_layout.addWidget(poster_label)

        watch_button = QPushButton("Watch Episodes")
        watch_button.setStyleSheet("background-color: #2e51a2; color: white; font-size: 10pt; padding: 6px 12px;")
        poster_layout.addWidget(watch_button)

        info_header = QLabel("Information")
        info_header.setFont(QFont("Arial", 10, QFont.Bold))
        info_header.setStyleSheet("margin-top: 15px; margin-bottom: 5px; border-bottom: 1px solid #ccc;")
        poster_layout.addWidget(info_header)

        def add_info_row(label_text, value_text):
            row = QLabel(f"<b>{label_text}</b>: {value_text}")
            row.setWordWrap(True)
            row.setStyleSheet("font-size: 9pt; margin-bottom: 2px;")
            poster_layout.addWidget(row)

        add_info_row("Type", anime_data.get("type", "N/A"))
        add_info_row("Episodes", str(anime_data.get("episodes", "N/A")))
        add_info_row("Status", anime_data.get("status", "N/A"))
        add_info_row("Aired", "Sep 29, 2023 to Mar 22, 2024")
        add_info_row("Premiered", anime_data.get("season", "Fall 2023"))
        add_info_row("Broadcast", "Fridays at 23:00 (JST)")
        add_info_row("Producers", "Aniplex, Dentsu, Shogakukan, TOHO animation")
        add_info_row("Licensors", "Crunchyroll")
        add_info_row("Studios", anime_data.get("studio", "Madhouse"))
        add_info_row("Source", "Manga")
        add_info_row("Genres", "Adventure, Drama, Fantasy")
        add_info_row("Demographic", "Shounen")
        add_info_row("Duration", "24 min. per ep.")
        add_info_row("Rating", "PG-13 - Teens 13 or older")

        poster_layout.addStretch(1)

        right_layout = QVBoxLayout()
        right_layout.setSpacing(4)

        title = QLabel(anime_data.get("title", "Title Unknown"))
        title.setFont(QFont("Arial", 30, QFont.Bold))
        title.setFixedHeight(40)

        subtitle = QLabel(anime_data.get("subtitle", ""))
        subtitle.setFont(QFont("Arial", 10, QFont.StyleItalic))
        subtitle.setStyleSheet("color: #555;")
        subtitle.setContentsMargins(0, 0, 0, 0)

        title_subtitle_wrapper = QWidget()
        title_subtitle_layout = QVBoxLayout(title_subtitle_wrapper)
        title_subtitle_layout.setContentsMargins(0, 0, 0, 0)
        title_subtitle_layout.setSpacing(0)
        title_subtitle_layout.addWidget(title)
        title_subtitle_layout.addWidget(subtitle)

        right_layout.addWidget(title_subtitle_wrapper)

        info_grid = QVBoxLayout()

        def make_label(text, bold=True):
            label = QLabel(text)
            label.setFont(QFont("Arial", 10, QFont.Bold if bold else QFont.Normal))
            label.setStyleSheet("color: #333;")
            return label

        info_grid.addWidget(make_label(f"Score: {anime_data.get('score', 'N/A')}", True))
        info_grid.addWidget(make_label(f"Ranked: {anime_data.get('rank', '#?')}", False))
        info_grid.addWidget(make_label(f"Popularity: {anime_data.get('popularity', '#?')}", False))
        info_grid.addWidget(make_label(f"Members: {anime_data.get('members', '???')}", False))

        right_layout.addLayout(info_grid)

        line_info = QLabel()
        line_info.setFixedHeight(1)
        line_info.setStyleSheet("background-color: #ccc;")
        right_layout.addWidget(line_info)

                # Container for toggleable add-to-list section
        list_controls = QHBoxLayout()
        list_controls.setSpacing(10)

        # Toggle button
        add_button = QPushButton("+ Add to List")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #2e51a2;
                color: white;
                padding: 6px 12px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3e61b2;
            }
        """)
        add_button.setCursor(Qt.PointingHandCursor)

        # Inline widget container
        self.inline_controls = QWidget()
        inline_layout = QHBoxLayout(self.inline_controls)
        inline_layout.setSpacing(10)
        inline_layout.setContentsMargins(10, 10, 10, 10)
        self.inline_controls.setStyleSheet("""
            QWidget {
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
        """)

        status_select = QComboBox()
        status_select.addItems(["Watching", "Completed", "On-Hold", "Dropped", "Plan to Watch"])
        status_select.setStyleSheet("""
        QComboBox {
            border: 1px solid #28a745;
            border-radius: 6px;
            padding: 6px 10px;
            background: white;
            color: #28a745;
            min-width: 110px;
        }

        QComboBox::drop-down {
            border-left: 1px solid #28a745;
            width: 20px;
        }

        QComboBox::down-arrow {
            image: url(:/qt-project.org/styles/commonstyle/images/arrowdown.png);
        }

        QComboBox QAbstractItemView {
            border: 1px solid #28a745;
            background: rgba(255, 255, 255, 0.95);
            outline: none;
            selection-background-color: #e0f9ec;
            selection-color: #000;
            padding: 4px;
            font-size: 10pt;
        }

        QScrollBar:vertical {
            border: none;
            background: transparent;
            width: 8px;
            margin: 0px;
        }

        QScrollBar::handle:vertical {
            background: #bbb;
            border-radius: 4px;
            min-height: 20px;
        }

        QScrollBar::handle:vertical:hover {
            background: #888;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            height: 0;
            background: none;
        }

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {
            background: none;
        }
        """)


        score_select = QComboBox()
        score_select.addItem("⭐ Select")
        score_labels = [
            "⭐ (10) Masterpiece", "⭐ (9) Great", "⭐ (8) Very Good", "⭐ (7) Good", "⭐ (6) Fine",
            "⭐ (5) Average", "⭐ (4) Bad", "⭐ (3) Very Bad", "⭐ (2) Horrible", "⭐ (1) Appalling"
        ]
        for label in score_labels:
            score_select.addItem(label)
        score_select.setStyleSheet("""
        QComboBox {
            border: 1px solid #aaa;
            border-radius: 6px;
            padding: 6px 10px;
            background: white;
            min-width: 150px;
        }

        QComboBox::drop-down {
            width: 20px;
            border-left: 1px solid #aaa;
        }

        QComboBox::down-arrow {
            image: url(:/qt-project.org/styles/commonstyle/images/arrowdown.png);
            width: 10px;
            height: 10px;
        }

        QComboBox QAbstractItemView {
            border: 1px solid #ccc;
            background: rgba(255, 255, 255, 0.95);
            outline: none;
            selection-background-color: #e0f0ff;
            selection-color: #000;
            padding: 4px;
            font-size: 10pt;
            alternate-background-color: transparent;
        }

        QScrollBar:vertical {
            border: none;
            background: transparent;
            width: 8px;
            margin: 0px;
        }

        QScrollBar::handle:vertical {
            background: #bbb;
            border-radius: 4px;
            min-height: 20px;
        }

        QScrollBar::handle:vertical:hover {
            background: #888;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            height: 0;
            background: none;
        }

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {
            background: none;
        }
        """)

        episode_spin = QSpinBox()
        episode_spin.setRange(0, anime_data.get("episodes", 0))
        episode_spin.setStyleSheet("""
            QSpinBox {
                border: 1px solid #aaa;
                border-radius: 6px;
                padding: 6px 10px;
                background: white;
                min-width: 60px;
            }
        """)
        total_label = QLabel(f"/ {anime_data.get('episodes', 0)}")
        total_label.setStyleSheet("color: #555; padding-left: 5px; font-size: 10pt;")

        inline_layout.addWidget(status_select)
        inline_layout.addWidget(score_select)
        inline_layout.addWidget(QLabel("Episodes:"))
        inline_layout.addWidget(episode_spin)
        inline_layout.addWidget(total_label)
        self.inline_controls.hide()

        def toggle_controls():
            add_button.hide()
            self.inline_controls.show()

        add_button.clicked.connect(toggle_controls)

        list_controls.addWidget(add_button)
        list_controls.addWidget(self.inline_controls)
        list_controls.addStretch(1)

        right_layout.addLayout(list_controls)

        line_controls = QLabel()
        line_controls.setFixedHeight(1)
        line_controls.setStyleSheet("background-color: #ccc;")
        right_layout.addWidget(line_controls)

        synopsis_title = QLabel("Synopsis")
        synopsis_title.setFont(QFont("Arial", 11, QFont.Bold))

        synopsis = QLabel(anime_data.get("synopsis", "No synopsis available."))
        synopsis.setWordWrap(True)
        synopsis.setStyleSheet("color: #444;")
        synopsis.setFont(QFont("Arial", 10))

        right_layout.addSpacing(10)
        right_layout.addWidget(synopsis_title)
        right_layout.addWidget(synopsis)

        line1 = QLabel()
        line1.setFixedHeight(1)
        line1.setStyleSheet("background-color: #ccc;")
        right_layout.addWidget(line1)

        char_header = QLabel("Characters & Voice Actors")
        char_header.setFont(QFont("Arial", 11, QFont.Bold))
        right_layout.addSpacing(10)
        right_layout.addWidget(char_header)

        line2 = QLabel()
        line2.setFixedHeight(1)
        line2.setStyleSheet("background-color: #ccc;")
        right_layout.addWidget(line2)

        char_grid = self.build_character_voice_grid(anime_data.get("characters", []))
        right_layout.addLayout(char_grid)

        # Review Section
        reviews = anime_data.get("reviews", [])
        review_layout = self.build_review_list(reviews)
        right_layout.addSpacing(10)
        right_layout.addWidget(QLabel("Reviews"))
        right_layout.addLayout(review_layout)

        for char in anime_data.get("characters", []):
            row = QHBoxLayout()

            char_img = QLabel()
            pix = QPixmap(char["image"])
            char_img.setPixmap(pix.scaled(60, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            char_img.setFixedSize(60, 80)
            row.addWidget(char_img)

            char_info = QLabel(f"<b>{char['name']}</b><br>{char['role']}")
            char_info.setStyleSheet("font-size: 9pt;")
            char_info.setFixedWidth(100)
            row.addWidget(char_info)

            va_img = QLabel()
            pix = QPixmap(char['voice']['image'])
            va_img.setPixmap(pix.scaled(60, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            va_img.setFixedSize(60, 80)
            row.addWidget(va_img)

            va_info = QLabel(f"{char['voice']['name']}<br><i>{char['voice']['lang']}</i>")
            va_info.setStyleSheet("font-size: 9pt;")
            row.addWidget(va_info)

            row.setSpacing(15)
            right_layout.addLayout(row)

        right_widget = QWidget()
        right_widget.setLayout(right_layout)

        content_layout.addLayout(poster_layout)
        content_layout.addWidget(right_widget, alignment=Qt.AlignTop)

        scroll_widget = QWidget()
        scroll_widget.setLayout(content_layout)
        scroll_widget.setMinimumWidth(1000)  # Ensures scrollbar appears if content overflows

        scroll_area = QScrollArea()
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f1f1f1;
                width: 12px;
                margin: 0px 0px 0px 0px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical {
                background: #888;
                min-height: 20px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical:hover {
                background: #555;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0;
                background: none;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        self.main_layout.addWidget(scroll_area)
        self.setStyleSheet("QWidget { border: none; }")

    def return_to_list(self):
        from anime_list_page import AnimeListPage
        list_window = AnimeListPage(chat_window=None)
        list_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    anime_data = load_anime_data(anime_id="frieren")
    window = AnimeDetailWindow(anime_data)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    window.setGeometry(rect)
    window.show()
    sys.exit(app.exec_())