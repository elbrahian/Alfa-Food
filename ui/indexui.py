from ui.general import *
from ui.login import *
from models.usuarios import *
from  ui.vista1admin import *
from menus.mainmenu import *
from ui.meseros import *
from menus.mainmenu import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
usuario=Usuarios()

class AppUi(QMainWindow):
    def __init__(self, connection):
        super().__init__()
        self.ui = Login_ui()
        self.ui.setupUi(self, connection)
        self.ui.login_successful.connect(self.handle_login_successful)

    def handle_login_successful(self, user_id):
        self.close()
        u=usuario.ObtenerUsuarioPorID(self.ui.connection,user_id)
        mainmenu(self.ui.connection,user_id)


        if u[3] == "SUPERADMIN":
            self.general_window = QMainWindow()
            general_ui = General_Ui()
            general_ui.setupUi(self.general_window, user_id, self.ui.connection)
            self.general_window.show()
        elif u[3] == "ADMIN":
            self.admin = QMainWindow()
            admin_ui = View_Admin()
            admin_ui.setupUi(self.admin, user_id, self.ui.connection)
            self.admin.show()
        elif u[3] == "MESERO":
            self.mesero = QMainWindow()
            mesero_ui = Meseros_Ui()
            mesero_ui.setupUi(self.mesero, user_id, self.ui.connection)
            self.mesero.show()

        elif u[3] == "COCINERO":
            print('c')
        else:
            print("❌Unauthorized Access❌")
