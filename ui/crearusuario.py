from PyQt5 import QtCore, QtGui, QtWidgets
from models.usuarios import *
from models.restaurantes import *
u=Usuarios()
r=Restaurantes()

class Ui_Dialogcrearuser(object):
    def setupUi(self, Dialog,user_id,connection):
        Dialog.setObjectName("Crear Usuario")
        Dialog.resize(372, 273)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Nombre:")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Documento:")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 90, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Telefono:")

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 130, 241, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Contraseña:")

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 170, 151, 31))
        self.comboBox_2.setObjectName("comboBox_2")

        # Ejemplo: Agregar roles de ejemplo
        roles = ["SUPERADMIN","ADMIN", "MESERO", "COCINERO"]
        self.comboBox_2.addItems(roles)
        self.comboBox_2.currentIndexChanged.connect(self.onRoleChanged)

        self.userimage = QtWidgets.QLabel(Dialog)
        self.userimage.setGeometry(QtCore.QRect(260, 10, 101, 91))
        self.userimage.setText("")
        self.userimage.setPixmap(QtGui.QPixmap("assets/img/avatar.svg"))
        self.userimage.setScaledContents(True)
        self.userimage.setObjectName("userimage")

        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 170, 151, 31))
        self.comboBox_3.setObjectName("comboBox_3")

        # Ejemplo: Agregar restaurantes de ejemplo

        resta=r.ListarTodosLosRestaurantes(connection)
        restaurantes = [restaurante[1] for restaurante in resta]
        self.comboBox_3.addItems(restaurantes)

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(lambda: self.accept(connection))
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear Usuario"))

    def onRoleChanged(self):

        if self.comboBox_2.currentText() == "Superadmin":
            self.comboBox_3.setEnabled(False)
            self.comboBox_3.setCurrentIndex(0)
        else:
            self.comboBox_3.setEnabled(True)

    def accept(self,connection):
        if not self.lineEdit_2.text() or not self.lineEdit.text() or not self.lineEdit_3.text() or not self.lineEdit_4.text():
            QtWidgets.QMessageBox.critical(None, "Error", "Todos los campos son obligatorios.")
            return
        nombre = self.lineEdit_2.text()
        documento = self.lineEdit.text()
        telefono = self.lineEdit_3.text()
        contraseña = self.lineEdit_4.text()
        rol = self.comboBox_2.currentText()
        restaurante = self.comboBox_3.currentText()
        id_r=r.ListarRestaurantePorNombre(connection,restaurante)
        newuser=u.CrearUsuario(connection,documento,nombre,rol,True,telefono,contraseña,id_r[0])
        if newuser is False:
            QtWidgets.QMessageBox.critical(None, "Error", "Documento ya existe")
            return
        if newuser is None:
            QtWidgets.QMessageBox.critical(None, "Error", "Error al crear Usuario")
            return





