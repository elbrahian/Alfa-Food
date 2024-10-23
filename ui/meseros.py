from PyQt5 import QtCore, QtGui, QtWidgets
from models.usuarios import *
from models.mesas import *
from models.restaurantes import *
u=Usuarios()
res=Restaurantes()
mes=Mesas()
import requests
from io import BytesIO

class Meseros_Ui(object):
    def setupUi(self, Form,user_id,connection):
        info_u = u.ObtenerUsuarioPorID(connection, user_id)
        r=res.ListarTodosLosRestaurantes(connection)
        m=mes.ListarMesas(connection)
        Form.setObjectName("Form")
        Form.resize(1358, 736)
        Form.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.usuario = QtWidgets.QWidget(Form)
        self.usuario.setGeometry(QtCore.QRect(10, 10, 321, 80))
        self.usuario.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 25px;")
        self.usuario.setObjectName("usuario")
        self.fotouser_2 = QtWidgets.QLabel(self.usuario)
        self.fotouser_2.setGeometry(QtCore.QRect(0, 0, 81, 71))
        self.fotouser_2.setText("")
        self.fotouser_2.setPixmap(QtGui.QPixmap("assets/img/avatar.svg"))
        self.fotouser_2.setScaledContents(True)
        self.fotouser_2.setObjectName("fotouser_2")

        self.nombreuser_2 = QtWidgets.QWidget(self.usuario)
        self.nombreuser_2.setGeometry(QtCore.QRect(90, 10, 141, 21))
        self.nombreuser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombreuser_2.setObjectName("nombreuser_2")

        self.rol_2 = QtWidgets.QWidget(self.usuario)
        self.rol_2.setGeometry(QtCore.QRect(80, 40, 141, 21))
        self.rol_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rol_2.setObjectName("rol_2")

        self.nombreuser_2 = QtWidgets.QLabel(self.usuario)
        self.nombreuser_2.setGeometry(QtCore.QRect(90, 10, 141, 21))
        self.nombreuser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombreuser_2.setObjectName("nombreuser_2")
        self.nombreuser_2.setText(info_u[2])

        # Crear el widget para el rol
        self.rol_2 = QtWidgets.QLabel(self.usuario)
        self.rol_2.setGeometry(QtCore.QRect(80, 40, 141, 21))
        self.rol_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rol_2.setObjectName("rol_2")
        self.rol_2.setText(info_u[3])

        self.exit_2 = QtWidgets.QPushButton(self.usuario)
        self.exit_2.setGeometry(QtCore.QRect(270, 10, 51, 61))
        self.exit_2.setStyleSheet("background-color: transparent;")
        self.exit_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_2.setIcon(icon)
        self.exit_2.setIconSize(QtCore.QSize(30, 30))
        self.exit_2.setObjectName("exit_2")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(570, -10, 211, 121))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assets/img/image-uFlK5B6rP3-transformed-removebg-preview.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 130, 371, 51))
        self.label.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(950, 130, 331, 51))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

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





        # Create the grid for showing tables
        show_tables_grid = QtWidgets.QWidget(Form)
        show_tables_grid.setGeometry(QtCore.QRect(880, 190, 461, 541))
        show_tables_grid.setObjectName("show_tables_grid")

        show_grid_layout = QtWidgets.QGridLayout(show_tables_grid)
        show_grid_layout.setSpacing(20)  # Adjust the spacing between buttons
        print(m)
        mesas = [{"numero": i, "estado": i % 2 == 0} for i in range(1, 11)]

        for mesa in m:
            button = QtWidgets.QPushButton(show_tables_grid)
            button.setObjectName(f"pushButton_show_{mesa[0]}")
            button.setFixedSize(100, 100)

            # Set the mesa number as the text on the button
            button.setText(f"Mesa {mesa[0]}")

            # Determine the color based on the mesa's estado
            estado = mesa[1]
            color = "green" if estado else "red"
            button.setStyleSheet(
                f"background-color: {color};"
                "border-radius: 25px;"
                "margin: 10px;"
            )

            show_grid_layout.addWidget(button, (mesa[0] - 1) // 5, (mesa[0] - 1) % 5)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Crear pedido"))
        self.label_2.setText(_translate("Form", "Pedidos Activos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Meseros_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
