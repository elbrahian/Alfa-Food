from models.restaurantes import *
from models.productos import *
from models.pedidos import *
from models.mesas import *

# Clases
usuario = Usuarios()
restaurante = Restaurantes()
productos = Productos()
pedido = Pedidos()
mesa = Mesas()

def Menucocinero(connection, user):
    while True:
        pedido_r = pedido.ListarPedidosPorRestaurante(connection, user[6])
        if len(pedido_r) > 0:
            notificacion = f"🚨 ¡Tienes {len(pedido_r)}, pedidos pendientes! 🚨"
        else:
            notificacion = ""
        print("=======", user[7], "========")
        print(
            f"""
            {notificacion}
            ============================
            =======MENU PRINCIPAL=======

                * Opcion 1: Ver Pedidos
                * Opcion 2: Terminar Pedidos
                * Opcion 3: ver productos
                * Opcion 3: SALIR

            ============================
            ============================
            """
        )
        opcion = input("Elija una opcion: ")
        if opcion == '1':
            print("====PEDIDOS PENDIENTES====")
            pedido_r=pedido.ListarPedidosPorRestaurante(connection,user[6])
            for info_pedi in pedido_r:
                for product in info_pedi['productos']:
                    print(f"  - Nombre: {product['nombre']}")
                    print(f"    Cantidad: {product['cantidad']}")

        if opcion == '2':
            print("====TERMNAR PERDIDO====")

        elif opcion == '3':
            print("====PRODUCTOS DE RESTAURATE====")
            pro = productos.ListarProductosPorRestaurante(connection, user[6])
            if pro:
                for pro_info in pro:
                    print("Nombre:", pro_info[1],"Precio: $", pro_info[3],f"Estado: {'✅' if pro_info[2] else '❌'}")
                    print("------------------------------")
            else:
                print("no existen productos")

        elif opcion == '4':
            print("Cerrando sesion...")
            print("Hasta luego")
            break
        else:
            print("Opción no válida")