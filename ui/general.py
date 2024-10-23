from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from models.usuarios import *
from models.restaurantes import *
import requests
from io import BytesIO
from ui.restaurante import *
from ui.vistausuariosadmin import Ui_Form



class General_Ui(object):
    def setupUi(self, Form, user_id, connection):
        restaurante = Restaurantes()
        r = restaurante.ListarTodosLosRestaurantes(connection)
        Form.setObjectName("Form")
        Form.resize(1358, 745)
        Form.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(580, 0, 261, 151))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assets/img/image-uFlK5B6rP3-transformed-removebg-preview.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1210, 10, 75, 23))
        self.pushButton.setStyleSheet("Background-color: transparent; ")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1280, 10, 75, 23))
        self.pushButton_2.setStyleSheet("Background-color: transparent; ")
        self.pushButton_2.setObjectName("pushButton_2")


        vistaprincipalsuperadmin = QtWidgets.QWidget()
        self.gridLayoutWidget_2 = QtWidgets.QWidget(vistaprincipalsuperadmin)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 751, 551))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setFixedSize(820, 550)



        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 311, 81))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 40px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(260, 0, 41, 81))
        self.exit.setStyleSheet("background-color: transparent;")
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setIconSize(QtCore.QSize(40, 40))
        self.exit.setObjectName("exit")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 81, 81))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/img/avatar.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 101, 21))
        self.label_2.setStyleSheet("font-size: 13px")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 101, 21))
        self.label_3.setObjectName("label_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 180, 321, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(30, 170, 381, 521))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(410, 170, 381, 521))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.usuarios_admin_window = None
        self.pushButton_2.clicked.connect(lambda: self.abrir_vista_usuarios_admin(user_id,connection))

        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(900, 330, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")

        num_columns = 4
        for i, r_info in enumerate(r):
            button = QtWidgets.QPushButton(Form)
            button.setObjectName(f"pushButton_{i}")
            button.setFixedSize(180, 140)
            button.setStyleSheet(
                "background-color: white;"
                "border-radius: 25px;"
                "margin: 10px;"
            )
            if r_info[3] is not None:
                image_url = r_info[3]
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_data = BytesIO(response.content)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(image_data.getvalue())
                    icon = QtGui.QIcon(pixmap)
                    button.setIcon(icon)
                    button.setIconSize(QtCore.QSize(160, 120))
                else:
                    print(f"Failed to download image from {image_url}")
            else:
                button.setText(r_info[1])

            row = i // num_columns
            col = i % num_columns

            button.setGeometry(QtCore.QRect(70 + col * 170, 200 + row * 140, 160, 120))

            button.clicked.connect(lambda checked, index=i, r_info=r_info: self.restaurant_button_clicked(index, r_info,user_id,connection))

        self.retranslateUi(Form, user_id, connection)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def restaurant_button_clicked(self, index, restaurant_info, user_id, connection):
        print(f"Restaurant ID: {restaurant_info[0]}")
        restaurante_window = QtWidgets.QMainWindow()
        ui = Ui_Restaurante()
        ui.setupUi(restaurante_window)
        restaurante_window.show()


    def abrir_vista_usuarios_admin(self,user_id,connection):
        if not self.usuarios_admin_window:
            self.usuarios_admin_window = QtWidgets.QMainWindow()
            ui_usuarios_admin = Ui_Form()
            ui_usuarios_admin.setupUi(self.usuarios_admin_window,user_id, connection)
        self.usuarios_admin_window.show()

    def retranslateUi(self, Form, user_id, connection):
        user = Usuarios()
        u = user.ObtenerUsuarioPorID(connection, user_id)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Facturacion"))
        self.pushButton_2.setText(_translate("Form", "Usuarios"))
        self.label_2.setText(_translate("Form", u[2]))
        self.label_3.setText(_translate("Form", u[3]))
        self.pushButton_4.setText(_translate("Form", "Cerrar ventas del dia"))








