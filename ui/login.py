from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from database.config import *
from models.usuarios import *
import sys
class Login_ui(QtCore.QObject):

    login_successful = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.connection = None
    def setupUi(self, Form,connection):
        self.connection = connection
        Form.setObjectName("From")
        Form.resize(1358, 745)
        Form.setStyleSheet("background-color: rgb(230, 230, 230);")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(0, -180, 851, 1091))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/img/wave.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(590, 150, 201, 201))
        self.label.setMaximumSize(QtCore.QSize(201, 201))
        self.label.setStyleSheet("aling:center;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/img/avatar.svg"))
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1090, 0, 261, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("assets/img/image-uFlK5B6rP3-transformed-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 580, 161, 41))
        self.pushButton_2.setStyleSheet("background-color:rgb(13, 153, 255); border-radius:5px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(550, 420, 272, 41))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255); border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Cedula")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(550, 510, 272, 41))
        self.lineEdit_3.setStyleSheet("background-color:rgb(255, 255, 255); border-radius: 5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setPlaceholderText("Contraseña")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setFont(font)

        self.lineEdit.returnPressed.connect(self.on_pushButton_2_clicked)
        self.lineEdit_3.returnPressed.connect(self.on_pushButton_2_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Iniciar Sesion"))

    def on_pushButton_2_clicked(self):
        cedula = self.lineEdit.text()
        contraseña = self.lineEdit_3.text()
        if cedula and contraseña:
            usuario = Usuarios()
            u = usuario.Login(self.connection, cedula, contraseña)
            if u:
                self.login_successful.emit(u)
            else:
                self.show_error_dialog("Cedula o contraseña inválidos")
        else:
            self.show_error_dialog("Por favor, complete todos los campos")

    def show_error_dialog(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)

        msg_box.setStyleSheet("""
               QMessageBox {
                   background-color: #f0f0f0;
                   border-radius: 10px;
               }
               QMessageBox QLabel {
                   font-size: 16px;
               }
               """)
        msg_box.exec()
