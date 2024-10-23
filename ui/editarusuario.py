from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 244)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 210, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Desactivar = QtWidgets.QPushButton(Dialog)
        self.Desactivar.setGeometry(QtCore.QRect(110, 190, 88, 27))
        self.Desactivar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border: 2px solid #000000;")
        self.Desactivar.setObjectName("Desactivar")
        self.Activar = QtWidgets.QPushButton(Dialog)
        self.Activar.setGeometry(QtCore.QRect(10, 190, 88, 27))
        self.Activar.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #000000;")
        self.Activar.setObjectName("Activar")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 120, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.userimage = QtWidgets.QLabel(Dialog)
        self.userimage.setGeometry(QtCore.QRect(290, 10, 101, 91))
        self.userimage.setText("")
        self.userimage.setPixmap(QtGui.QPixmap("../../../macrohard-poo/assets/img/avatar.svg"))
        self.userimage.setScaledContents(True)
        self.userimage.setObjectName("userimage")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "Nombre:"))
        self.lineEdit_2.setText(_translate("Dialog", "Rol:"))
        self.Desactivar.setText(_translate("Dialog", "Desactivar"))
        self.Activar.setText(_translate("Dialog", "Activar"))
        self.lineEdit_3.setText(_translate("Dialog", "Estado:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
