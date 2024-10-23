
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from ui.editarusuario import Ui_Dialog
from ui.crearusuario import Ui_Dialogcrearuser
from models.usuarios import *
u=Usuarios()

class Ui_Form(object):
    def setupUi(self, Form,user_id, connection):

        info_u=u.ObtenerUsuarioPorID(connection,user_id)
        list_usuarios=u.ObtenerUsuarios(connection)
        Form.setObjectName("Form")
        Form.resize(1358, 772)
        Form.setStyleSheet("background-color: rgb(230, 230, 230);")

        self.infouser = QtWidgets.QWidget(Form)
        self.infouser.setGeometry(QtCore.QRect(10, 10, 321, 80))
        self.infouser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.infouser.setObjectName("infouser")

        self.nombreuser = QtWidgets.QWidget(self.infouser)
        self.nombreuser.setGeometry(QtCore.QRect(90, 10, 141, 21))
        self.nombreuser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombreuser.setObjectName("nombreuser")

        self.rol = QtWidgets.QWidget(self.infouser)
        self.rol.setGeometry(QtCore.QRect(80, 40, 141, 21))
        self.rol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rol.setObjectName("rol")

        self.label_nombreuser = QtWidgets.QLabel(self.infouser)
        self.label_nombreuser.setGeometry(QtCore.QRect(90, 10, 141, 21))
        self.label_nombreuser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_nombreuser.setObjectName("label_nombreuser")
        self.label_nombreuser.setText(info_u[2])

        self.label_rol = QtWidgets.QLabel(self.infouser)
        self.label_rol.setGeometry(QtCore.QRect(80, 40, 141, 21))
        self.label_rol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_rol.setObjectName("label_rol")
        self.label_rol.setText(info_u[3])

        self.userimage = QtWidgets.QLabel(self.infouser)
        self.userimage.setGeometry(QtCore.QRect(0, 0, 81, 71))
        self.userimage.setText("")
        self.userimage.setPixmap(QtGui.QPixmap("assets/img/avatar.svg"))
        self.userimage.setScaledContents(True)
        self.userimage.setObjectName("userimage")
        self.exit = QtWidgets.QPushButton(self.infouser)
        self.exit.setGeometry(QtCore.QRect(280, 10, 31, 61))
        self.exit.setStyleSheet("background-color: transparent;\n"
"image: url(:/exit/right-from-bracket-solid.svg);")
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setIconSize(QtCore.QSize(30, 30))
        self.exit.setObjectName("exit")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1080, 10, 275, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.redirecciones_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.redirecciones_2.setContentsMargins(0, 0, 0, 0)
        self.redirecciones_2.setObjectName("redirecciones_2")
        self.redireccionrest = QtWidgets.QPushButton(self.layoutWidget_2)
        self.redireccionrest.setStyleSheet("background-color: transparent;")
        self.redireccionrest.setObjectName("redireccionrest")
        self.redirecciones_2.addWidget(self.redireccionrest)
        self.redireccionfact = QtWidgets.QPushButton(self.layoutWidget_2)
        self.redireccionfact.setStyleSheet("background-color: transparent;")
        self.redireccionfact.setObjectName("redireccionfact")
        self.redirecciones_2.addWidget(self.redireccionfact)

        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(550, -20, 261, 151))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assets/img/image-uFlK5B6rP3-transformed-removebg-preview.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.agregaruser = QtWidgets.QPushButton(Form)
        self.agregaruser.setGeometry(QtCore.QRect(1220, 100, 121, 71))
        self.agregaruser.setStyleSheet("background-color: transparent;")
        self.agregaruser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/img/plus-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.agregaruser.setIcon(icon1)
        self.agregaruser.setIconSize(QtCore.QSize(80, 80))
        self.agregaruser.setObjectName("agregaruser")
        self.cuadrousuarios = QtWidgets.QWidget(Form)
        self.cuadrousuarios.setGeometry(QtCore.QRect(10, 180, 211, 80))
        self.cuadrousuarios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")

        self.cuadrousuarios.setObjectName("cuadrousuarios")
        self.nombreuser_2 = QtWidgets.QWidget(self.cuadrousuarios)
        self.nombreuser_2.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.nombreuser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombreuser_2.setObjectName("nombreuser_2")
        self.rol_2 = QtWidgets.QWidget(self.cuadrousuarios)
        self.rol_2.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.rol_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rol_2.setObjectName("rol_2")
        self.editaruser = QtWidgets.QPushButton(self.cuadrousuarios)
        self.editaruser.setGeometry(QtCore.QRect(170, 10, 31, 31))
        self.editaruser.setStyleSheet("")
        self.editaruser.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('assets/img/pen-to-square-regular.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editaruser.setIcon(icon2)
        self.editaruser.setIconSize(QtCore.QSize(30, 30))
        self.editaruser.setObjectName("editaruser")
        self.estado = QtWidgets.QWidget(self.cuadrousuarios)
        self.estado.setGeometry(QtCore.QRect(170, 50, 21, 21))
        self.estado.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border: 2px solid #8f8f91;\n"
"border-radius: 20px;")
        self.estado.setObjectName("estado")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.editaruser.clicked.connect(self.abrir_cuadro_dialogo)
        self.agregaruser.clicked.connect(lambda: self.abrir_cuadro_dialogoagregar(user_id, connection))



        # Dimensiones iniciales para la cuadrícula
        x = 9
        y = 180
        cuadro_width = 200
        cuadro_height = 80

        num_columnas = 6
        num_filas = 5

        for usuario in list_usuarios:
            cuadro_usuario, editar_usuario = self.create_user_box(Form, x, y, cuadro_width, cuadro_height,usuario[2], usuario[3], usuario[4])
            x += cuadro_width + 10  # Espacio entre cuadros

            # Conectar la señal del botón de editar
            editar_usuario.clicked.connect(lambda _, user=usuario: self.abrir_cuadro_dialogo(user[0],user[2], user[3], user[4],connection))

            if x + cuadro_width > num_columnas * (cuadro_width + 10) + 9:
                x = 9
                y += cuadro_height + 10


    def abrir_cuadro_dialogoagregar(self,user_id,connection):

        dialog_crear_usuario = QtWidgets.QDialog()
        ui_crear_usuario = Ui_Dialogcrearuser()
        ui_crear_usuario.setupUi(dialog_crear_usuario,user_id,connection)
        dialog_crear_usuario.exec_()

    def abrir_cuadro_dialogo(self,id, username, role, estado,connection):
        # Crea el cuadro de diálogo
        dialog = QtWidgets.QDialog()
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)

        # Configura los campos con los datos del usuario
        dialog_ui.lineEdit.setText(f"Nombre: {username}")
        dialog_ui.lineEdit_2.setText(f"Rol: {role}")
        dialog_ui.lineEdit_3.setText(f"Estado: {'Activo' if estado else 'Inactivo'}")

        dialog_ui.Activar.clicked.connect(lambda: self.activar_usuario(id,username,connection))
        dialog_ui.Desactivar.clicked.connect(lambda: self.desactivar_usuario(id,username,connection))

        # Muestra el cuadro de diálogo
        result = dialog.exec_()

    def activar_usuario(self,id, username,connection):
        print(f"Usuario {username} activado")
        u.ActivarUsuario(connection,id)

    def desactivar_usuario(self,id, username,connection):
        print(f"Usuario {username} desactivado")
        u.DesactivarUsuario(connection,id)

    def create_user_box(self, parent, x, y, width, height, username, role, estado):
        cuadro_usuario = QtWidgets.QWidget(parent)
        cuadro_usuario.setGeometry(QtCore.QRect(x, y, width, height))
        cuadro_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 25px;")

        nombre_usuario = QtWidgets.QLabel(cuadro_usuario)
        nombre_usuario.setGeometry(QtCore.QRect(10, 10, 141, 21))
        nombre_usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        nombre_usuario.setObjectName("nombreuser_2")

        rol_usuario = QtWidgets.QLabel(cuadro_usuario)
        rol_usuario.setGeometry(QtCore.QRect(10, 40, 141, 21))
        rol_usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        rol_usuario.setObjectName("rol_2")

        editar_usuario = QtWidgets.QPushButton(cuadro_usuario)
        editar_usuario.setGeometry(QtCore.QRect(170, 10, 31, 31))
        editar_usuario.setStyleSheet("")
        editar_usuario.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets\img\pen-to-square-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editar_usuario.setIcon(icon2)
        editar_usuario.setIconSize(QtCore.QSize(30, 30))
        editar_usuario.setObjectName("editaruser")

        estado_usuario = QtWidgets.QWidget(cuadro_usuario)
        estado_usuario.setGeometry(QtCore.QRect(170, 50, 21, 21))
        estado_usuario.setStyleSheet("background-color: {};".format("green" if estado else "red") +
                                     "\nborder: 2px solid #8f8f91;\n"
                                     "border-radius: 20px;")
        estado_usuario.setObjectName("estado")
        nombre_usuario.setText(username)
        rol_usuario.setText(role)

        return cuadro_usuario, editar_usuario

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.redireccionrest.setText(_translate("Form", "Restaurantes"))
        self.redireccionfact.setText(_translate("Form", "Facturacion"))


