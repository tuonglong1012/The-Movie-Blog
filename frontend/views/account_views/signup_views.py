# view/signup_dialog.py
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QCheckBox, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QMessageBox,QSpinBox,QDateEdit
)
from PyQt5.QtCore import Qt
from controllers.account_controller import signup
from PyQt5.QtCore import Qt, QDate
from datetime import date

from datetime import date

class SignUpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Account")
        self.resize(400, 360)
        self.setModal(True)

        main = QVBoxLayout(self)
        main.setContentsMargins(12, 12, 12, 12)
        form = QFormLayout()
        main.addLayout(form)

        self.txt_user = QLineEdit(); form.addRow("Username:", self.txt_user)
        main.addWidget(QLabel("(2–16 characters)"))

        pw_h = QHBoxLayout()
        self.txt_pw = QLineEdit()
        self.txt_pw.setEchoMode(QLineEdit.Password)
        chk = QCheckBox("Show Password")
        chk.stateChanged.connect(lambda s: self.txt_pw.setEchoMode(
            QLineEdit.Normal if s == Qt.Checked else QLineEdit.Password))
        pw_h.addWidget(self.txt_pw); pw_h.addWidget(chk)
        form.addRow("Password:", pw_h)

        # Thay thế QSpinBox bằng QDateEdit để nhập ngày sinh
        dob_h = QHBoxLayout()
        self.date_birth = QDateEdit()
        self.date_birth.setCalendarPopup(True)
        self.date_birth.setDisplayFormat("dd/MM/yyyy")
        self.date_birth.setDate(QDate.currentDate())
        self.date_birth.setFixedWidth(120)
        dob_h.addWidget(self.date_birth)
        form.addRow("Date of Birth:", dob_h)

        main.addStretch()
        btn = QPushButton("Create Account")
        btn.clicked.connect(self._handle_signup)
        main.addWidget(btn)

        main.addStretch()
        ln = QPushButton("Already have an account? Login")
        ln.setFlat(True)
        ln.clicked.connect(self._to_login)
        main.addWidget(ln)

    def calculate_age(self):
        dob = self.date_birth.date().toPyDate()
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def _handle_signup(self):
        username = self.txt_user.text().strip()
        password = self.txt_pw.text().strip()
        dob_qdate = self.date_birth.date()
        date_of_birth = dob_qdate.toString("yyyy-MM-dd")  # Chuyển sang chuỗi yyyy-MM-dd

        if not (username and password):
            QMessageBox.warning(self, "Error", "Please fill all the fields.")
            return

        age = self.calculate_age()
        if age <= 0 or age > 150:
            QMessageBox.warning(self, "Invalid Date", "Please enter a valid date of birth.")
            return

        result = signup(username, password, date_of_birth)  # Truyền ngày sinh thay vì tuổi

        if "error" in result:
            QMessageBox.critical(self, "Signup Failed", result["error"])
        else:
            QMessageBox.information(self, "Success", "Account created. Please login.")
            self.accept()


    def _to_login(self):
        self.accept()
        self.parent().open_login_dialog()
