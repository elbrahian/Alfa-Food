from ui.indexui import *
from database.config import *
from datetime import  datetime
from menus.mainmenu import *

from models.pedidos import *
conexion = Basedatos("containers-us-west-46.railway.app", 7072, "postgres", "EbugePePwW5BJpDNNk8Q", "railway")

connection = conexion.conectar()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_app = AppUi(connection)
    login_app.show()
    sys.exit(app.exec_())

