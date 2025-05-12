# view/signup_dialog.py
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QCheckBox, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QMessageBox,QSpinBox
)
from PyQt5.QtCore import Qt
from controllers.account_controller import signup

from datetime import date

class SignUpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Account")
        self.resize(400, 340)
        self.setModal(True)

        main = QVBoxLayout(self)
        main.setContentsMargins(12,12,12,12)
        form = QFormLayout()
        main.addLayout(form)

       
        self.txt_user  = QLineEdit(); form.addRow("Username:", self.txt_user)
        main.addWidget(QLabel("(2–16 characters)"))

        pw_h = QHBoxLayout()
        self.txt_pw = QLineEdit()
        self.txt_pw.setEchoMode(QLineEdit.Password)
        chk = QCheckBox("Show Password")
        chk.stateChanged.connect(lambda s: self.txt_pw.setEchoMode(
            QLineEdit.Normal if s==Qt.Checked else QLineEdit.Password))
        pw_h.addWidget(self.txt_pw); pw_h.addWidget(chk)
        form.addRow("Password:", pw_h)

        age_h = QHBoxLayout()
        self.spn_age = QSpinBox()
        self.spn_age.setRange(0, 150)  # Giới hạn tuổi từ 0 đến 150
        self.spn_age.setFixedWidth(80)
        age_h.addWidget(self.spn_age)
        form.addRow("Age:", age_h)

        main.addStretch()
        btn = QPushButton("Create Account")
        btn.clicked.connect(self._handle_signup)
        main.addWidget(btn)

        main.addStretch()
        ln = QPushButton("Already have an account? Login")
        ln.setFlat(True)
        ln.clicked.connect(self._to_login)
        main.addWidget(ln)

    def _handle_signup(self):
        username = self.txt_user.text().strip()
        password = self.txt_pw.text().strip()
        age = self.spn_age.value()  # Lấy giá trị tuổi từ QSpinBox

        if not (username and password and age):
            QMessageBox.warning(self, "Error", "Please fill all the fields.")
            return

        result = signup(username, password, age)

        if "error" in result:
            QMessageBox.critical(self, "Signup Failed", result["error"])
        else:
            QMessageBox.information(self, "Success", "Account created. Please login.")
            self.accept()


    def _to_login(self):
        self.accept()
        self.parent().open_login_dialog()
