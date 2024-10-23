from models.restaurantes import *
from models.productos import *
from models.pedidos import *
from models.mesas import *

#Clases
usuario = Usuarios()
restaurante = Restaurantes()
productos= Productos()
pedido = Pedidos()
mesa=Mesas()



def MenuMesero(connection, user):
    global restaurante

    while True:
        print(
            """
            ============================
            =======MENU PRINCIPAL=======
    
                * Opcion 1: Crear pedidos 
                * Opcion 2: Ver Todos Los Pedidos
                * Opcion 3: Ver Productos
                * Opcion 4: Procesar Pedido🛃
                * Opcion 5: SALIR

            ============================
            ============================
            """
        )
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            id_pedido = ""
            print("====Crear Pedido====")
            mesas = mesa.ListarMesasActivas(connection)
            for mesas_info in mesas:
                print(f"*Mesa # {mesas_info[0]}")
            id_mesa = int(input("Ingrese el número de Mesa: "))

            new_pedido = pedido.CrearPedido(connection, id_mesa, user[0])
            if new_pedido:
                id_pedido = new_pedido
            while True:
                pro = productos.ListarProductos(connection)
                for i, pro_info in enumerate(pro, start=1):
                    if (pro_info[2]):
                        print(f"{i}. Nombre: {pro_info[1]}")

                seleccion = int(input("Ingrese el número de producto: "))
                if 1 <= seleccion <= len(pro):
                    id_pro = pro[seleccion - 1][0]
                    cantidad = int(input("Ingrese la cantidad: "))
                    new = pedido.CrearProductos_pedido(connection,id_pro,cantidad,id_pedido)
                    seguir = input("¿Desea agregar otro producto? (s/n): ")
                    if seguir != 's':
                        break
                else:
                    print("Número de producto no válido")
            print("PEDIDO CREADO CON EXITO")

        elif opcion == "3":
            print("====Productos====")
            pro = productos.ListarProductos(connection)
            if pro:
                for pro_info in pro:
                    print("ID:", pro_info[0])
                    print("Nombre:", pro_info[1])
                    print("Precio: $", pro_info[3])
                    print(f"Estado: {'Activo✅' if pro_info[2] else 'Inactivo❌'}")
                    print("------------------------------")
            else:
                print("no existen productos")

        elif opcion == '2':
            print("====PEDIDOS ACTIVOS====")
            ped=pedido.ListarPedidos(connection)
            for pedi in ped:
                print(f"ID de Pedido: {pedi['id_pedido']}")
                print(f"Mesa #{pedi['mesa']}")
                print(f"Estado del Pedido: {'Sin Pagar❌' if pedi['estado'] else 'Pago✅'}")
                print("Productos:")
                for product in pedi['productos']:
                    print(f"  - Nombre: {product['nombre']}")
                    print(f"    Cantidad: {product['cantidad']}")
                    print(f"    Precio Unitario: ${product['precio_unitario']}")
                    print(f"    Total Producto: ${product['total_producto']}")
                print("------------------------------")
                print(f"💲Total del Pedido: ${pedi['total_pedido']}")
                print("------------------------------")
                print("\n")

        elif opcion=='4':
            print("====PROCESAR PEDIDOS 🛃====")
            low = pedido.ListarPedidosPendientes(connection)
            mesa_id_pedido_map = {pedi_info["mesa"]: pedi_info["id_pedido"] for pedi_info in low}
            for i, pedi_info in enumerate(low, start=1):
                print(f"Mesa #{pedi_info['mesa']} | 💲Total $:{pedi_info['total_pedido']} ")
            seleccion = int(input("Ingrese el número de Mesa a procesar: "))
            if seleccion in mesa_id_pedido_map:
                id_pedido = mesa_id_pedido_map[seleccion]
                print(seleccion)
                pedido.PagarPedido(connection,id_pedido,seleccion)

            else:
                print("Número de Mesa no válido")

        elif opcion == '5':
            print("Cerrando sesion...")
            print("Hasta luego")
            break
        else:
            print("Opción no válida")