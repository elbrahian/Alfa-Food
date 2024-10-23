from menus.superadmin import *
from menus.admin import *
from menus.mesero import *
from menus.cocinero import *

usuario = Usuarios()
def mainmenu(connection, id):
    us = usuario.ObtenerUsuarioPorID(connection, id)
    print(
        """

   _____  .__   _____         ___________               .___
  /  _  \ |  |_/ ____\____    \_   _____/___   ____   __| _/
 /  /_\  \|  |\   __\\__  \    |    __)/  _ \ /  _ \ / __ | 
/    |    \  |_|  |   / __ \_  |     \(  <_> |  <_> ) /_/ | 
\____|__  /____/__|  (____  /  \___  / \____/ \____/\____ | 
        \/                \/       \/                    \/ 

        """
    )
    print ("!HOLA¡ ", us[2], "(", us[3], ")", " BIENVENIDO")
    if us[3]=="SUPERADMIN":
        MenuSuperAdmin(connection, us)
    elif us[3]=="ADMIN":
        MenuAdmin(connection, us)
    elif us[3]=="MESERO":
        MenuMesero(connection, us)
    elif us[3]=="COCINERO":
        Menucocinero(connection, us)
    else:
        print( "error")
