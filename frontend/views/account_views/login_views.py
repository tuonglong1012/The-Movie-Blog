# view/login_dialog.py
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QHBoxLayout, QLineEdit,
    QCheckBox, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
from controllers.account_controller import login

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.resize(380, 260)
        self.setModal(True)
        
        self.user_info = None 

        main = QVBoxLayout(self)
        main.setContentsMargins(12, 12, 12, 12)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        main.addLayout(form)

        self.txt_user = QLineEdit()
        form.addRow("Username:", self.txt_user)

        pw_h = QHBoxLayout()
        self.txt_pw = QLineEdit()
        self.txt_pw.setEchoMode(QLineEdit.Password)
        chk = QCheckBox("Show Password")
        chk.stateChanged.connect(
            lambda s: self.txt_pw.setEchoMode(
                QLineEdit.Normal if s == Qt.Checked else QLineEdit.Password
            )
        )
        pw_h.addWidget(self.txt_pw)
        pw_h.addWidget(chk)
        form.addRow("Password:", pw_h)

        self.chk_rem = QCheckBox("Stay logged in?")
        main.addWidget(self.chk_rem)

        main.addStretch()
        btn = QPushButton("Login")
        btn.clicked.connect(self._handle_login)
        main.addWidget(btn)

        main.addStretch()
        su = QPushButton("Sign Up")
        su.setFlat(True)
        su.clicked.connect(self._to_signup)
        main.addWidget(su)

    def _handle_login(self):
        username = self.txt_user.text().strip()
        password = self.txt_pw.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Missing Information", "Please enter both username and password.")
            return

        result = login(username, password)
        if "error" in result:
            QMessageBox.critical(self, "Login Failed", result["error"])
        else:
            self.user_info = result  # ✅ Lưu lại thông tin user để các phần khác dùng
            QMessageBox.information(self, "Login Successful", f"Welcome, {result['username']}!")
            self.accept()


    def _to_signup(self):
        self.accept()
        self.parent().open_signup_dialog()

    def get_user_info(self):
        return self.user_info

