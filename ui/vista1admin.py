from PyQt5 import QtCore, QtGui, QtWidgets
from models.usuarios import *
from datetime import datetime
from models.pedidos import *
from models.productos import *
import requests
from io import BytesIO
u = Usuarios()
p=Pedidos()
pro=Productos()

class View_Admin(object):
    def setupUi(self, Form, user_id, connection):
        info_u = u.ObtenerUsuarioPorID(connection, user_id)
        list_u_restaurate=u.ObtenerUsuariosPorRestaurante(connection,info_u[6])
        list_pedidos=p.ListarPedidosPorRestaurante(connection,info_u[6])
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        list_producto=pro.ListarProductosPorRestaurante(connection,info_u[6])
        list_pedidos_dia=p.ListarPedidosPorFecha(connection,fecha_actual,info_u[6])
        Form.setObjectName("Form")
        Form.resize(1358, 745)
        Form.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(1080, 10, 275, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.redirecciones = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.redirecciones.setContentsMargins(0, 0, 0, 0)
        self.redirecciones.setObjectName("redirecciones")
        self.users = QtWidgets.QPushButton(self.layoutWidget)
        self.users.setStyleSheet("background-color: transparent;")
        self.users.setObjectName("users")
        self.redirecciones.addWidget(self.users)
        self.rest = QtWidgets.QPushButton(self.layoutWidget)
        self.rest.setStyleSheet("background-color: transparent;")
        self.rest.setObjectName("rest")
        self.redirecciones.addWidget(self.rest)
        self.fact = QtWidgets.QPushButton(self.layoutWidget)
        self.fact.setStyleSheet("background-color: transparent;")
        self.fact.setObjectName("fact")
        self.redirecciones.addWidget(self.fact)

        self.nombrerestaurante = QtWidgets.QWidget(Form)
        self.nombrerestaurante.setGeometry(QtCore.QRect(65, 150, 361, 41))
        self.nombrerestaurante.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 25px;")
        self.nombrerestaurante.setObjectName("nombrerestaurante")

        self.label_restaurante = QtWidgets.QLabel(self.nombrerestaurante)
        self.label_restaurante.setGeometry(QtCore.QRect(10, 10, 341, 21))
        self.label_restaurante.setText(info_u[7])
        self.label_restaurante.setAlignment(QtCore.Qt.AlignCenter)
        self.label_restaurante.setStyleSheet("color: black; font-size: 8pt;")

        self.usuarios = QtWidgets.QWidget(Form)
        self.usuarios.setGeometry(QtCore.QRect(15, 230, 171, 41))
        self.usuarios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 25px;")
        self.usuarios.setObjectName("usuarios")

        self.label_usuarios = QtWidgets.QLabel(self.usuarios)
        self.label_usuarios.setGeometry(
            QtCore.QRect(15, 10, 151, 21))
        self.label_usuarios.setText("Usuarios: "+str(len(list_u_restaurate)))
        self.label_usuarios.setAlignment(QtCore.Qt.AlignCenter)


        self.pedidosactivos = QtWidgets.QWidget(Form)
        self.pedidosactivos.setGeometry(QtCore.QRect(15, 290, 171, 41))
        self.pedidosactivos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 25px;")
        self.pedidosactivos.setObjectName("pedidosactivos")
        self.label_pedidosactivos = QtWidgets.QLabel(self.pedidosactivos)
        self.label_pedidosactivos.setGeometry(QtCore.QRect(15, 10, 151, 21))
        self.label_pedidosactivos.setText("Pedidos Activos: "+str(len(list_pedidos)))

        self.ventaspormes = QtWidgets.QWidget(Form)
        self.ventaspormes.setGeometry(QtCore.QRect(15, 350, 171, 41))
        self.ventaspormes.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 25px;")
        self.ventaspormes.setObjectName("ventaspormes")
        self.label_ventaspormes = QtWidgets.QLabel(self.ventaspormes)
        self.label_ventaspormes.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label_ventaspormes.setText("Ventas "+str(datetime.now().strftime('%m/%d'))+" |"+"$"+str(list_pedidos_dia))
        self.label_ventaspormes.setObjectName("label_ventaspormes")

        self.desactivar = QtWidgets.QPushButton(Form)
        self.desactivar.setGeometry(QtCore.QRect(190, 690, 171, 41))
        self.desactivar.setStyleSheet("background-color: red; border-radius: 25px;")
        self.desactivar.setObjectName("desactivar")
        self.desactivar.setText("Desactivar")

        self.activar = QtWidgets.QPushButton(Form)
        self.activar.setGeometry(QtCore.QRect(190, 630, 171, 41))
        self.activar.setStyleSheet("background-color: green; border-radius: 25px;")
        self.activar.setObjectName("activar")
        self.activar.setText("Activar")

        self.label_imagen = QtWidgets.QLabel(Form)
        self.label_imagen.setGeometry(QtCore.QRect(10, 569, 161, 161))
        self.label_imagen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 25px;")
        self.label_imagen.setObjectName("label_imagen")

        imagen = self.obtener_imagen_desde_url(info_u[8])

        if imagen is not None:
            imagen = imagen.scaled(self.label_imagen.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)
            self.label_imagen.setPixmap(imagen)
        else:
            self.label_imagen.setText(info_u[7])
            self.label_imagen.setAlignment(QtCore.Qt.AlignCenter)

        self.ventasdia = QtWidgets.QWidget(Form)
        self.ventasdia.setGeometry(QtCore.QRect(10, 410, 171, 41))
        self.ventasdia.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 25px;")
        self.ventasdia.setObjectName("ventasdia")
        self.label_ventasdia = QtWidgets.QLabel(self.ventasdia)
        self.label_ventasdia.setGeometry(QtCore.QRect(15, 10, 151, 21))
        self.label_ventasdia.setText("Productos: #"+str(len(list_producto)))
        self.label_ventasdia.setAlignment(QtCore.Qt.AlignCenter)

        self.usuario = QtWidgets.QWidget(Form)
        self.usuario.setGeometry(QtCore.QRect(10, 10, 321, 80))
        self.usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "border-radius: 25px;")
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

        self.label_nombreuser_2 = QtWidgets.QLabel(self.nombreuser_2)
        self.label_nombreuser_2.setGeometry(QtCore.QRect(0, 0, 141, 21))
        self.label_nombreuser_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nombreuser_2.setText(info_u[2])

        self.rol_2 = QtWidgets.QWidget(self.usuario)
        self.rol_2.setGeometry(QtCore.QRect(80, 40, 141, 21))
        self.rol_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rol_2.setObjectName("rol_2")

        self.label_rol_2 = QtWidgets.QLabel(self.rol_2)
        self.label_rol_2.setGeometry(QtCore.QRect(0, 0, 141, 21))
        self.label_rol_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rol_2.setText(info_u[3])

        self.exit_2 = QtWidgets.QPushButton(self.usuario)
        self.exit_2.setGeometry(QtCore.QRect(270, 10, 51, 61))
        self.exit_2.setStyleSheet("background-color: transparent;")
        self.exit_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.exit_2.setIcon(icon)
        self.exit_2.setIconSize(QtCore.QSize(30, 30))
        self.exit_2.setObjectName("exit_2")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(570, -10, 211, 121))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assets/img/image-uFlK5B6rP3-transformed-removebg-preview.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.editarmenu = QtWidgets.QPushButton(Form)
        self.editarmenu.setGeometry(QtCore.QRect(970, 150, 371, 41))
        self.editarmenu.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.editarmenu.setObjectName("editarmenu")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(380, 210, 961, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1280, 10, 75, 23))
        self.pushButton_2.setStyleSheet("Background-color: transparent; ")
        self.pushButton_2.setObjectName("pushButton_2")


        num_columns = 5
        for i, r_info in enumerate(list_producto):
            button = QtWidgets.QPushButton(Form)
            button.setObjectName(f"pushButton_{i}")
            button.setFixedSize(160, 120)
            button.setStyleSheet(
                "background-color: white;"
                "border-radius: 25px;"
                "margin: 5px;"
            )
            button.setText(r_info[1])

            row = i // num_columns
            col = i % num_columns

            button.setGeometry(QtCore.QRect(430 + col * 170, 200 + row * 140, 160, 120))

    def obtener_imagen_desde_url(self, url):
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            imagen_bytes = BytesIO(respuesta.content)
            imagen = QtGui.QPixmap()
            imagen.loadFromData(imagen_bytes.getvalue())

            return imagen
        except Exception as e:
            print(f"Error al obtener la imagen desde la URL: {e}")
            return None

    def abrir_vista_usuarios_admin(self,user_id,connection):
        print(user_id)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.users.setText(_translate("Form", "Usuarios"))
        self.rest.setText(_translate("Form", "Restaurantes"))
        self.fact.setText(_translate("Form", "Facturacion"))
        self.editarmenu.setText(_translate("Form", "Editar Menu"))
        
