from models.mesas import *
from models.productos import *
from models.facturacion import *
import psycopg2
import uuid
f = Factura()

class Pedidos():
    id = ""
    estado = True
    mesa= ""
    usuarios = ""

    def __init__(self):
        pass

    def CrearPedido(self, conexion, mesa, usuario):
        m = Mesas()

        m.DesactivarMesas(conexion,mesa)
        try:

            with conexion.cursor() as cursor:
                id = str(uuid.uuid4())
                consulta = """
                    INSERT INTO pedidos(id, estado, mesa, usuarios, "createdAt", "updatedAt")
                    VALUES (%s, %s, %s, %s, NOW(), NOW());
                """
                cursor.execute(consulta, (id, True, mesa, usuario))
            conexion.commit()
            f.CrearFactura(conexion,id)
            return id
        except psycopg2.Error as e:
            print("ERROR:", e)
            return False

    def CrearProductos_pedido(self, conexion, id_producto, cantidad, id_pedido):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    INSERT INTO productos_pedido(id, id_producto, id_pedido, cantidad, "createdAt", "updatedAt")
                    VALUES (%s, %s, %s, %s, NOW(), NOW());
                """
                cursor.execute(consulta, (str(uuid.uuid4()), id_producto, id_pedido, cantidad))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR:", e)
            return False

    def ObtenerPedidoPorId(self, conexion, pedido_id):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT * FROM pedidos WHERE id = %s;
                """
                cursor.execute(consulta, (pedido_id,))
                pedido = cursor.fetchone()
                if pedido:
                    return pedido
                else:
                    print(f"Pedido con ID {pedido_id} no encontrado.")
                    return None
        except psycopg2.Error as e:
            print("ERROR:", e)
            return None

    def PagarPedido(self, conexion, id_pedido, mesa):
        try:
            m = Mesas()
            with conexion.cursor() as cursor:
                consulta = """
                    UPDATE pedidos
                    SET estado = false
                    WHERE id = %s;
                """
                cursor.execute(consulta, (id_pedido,))
                conexion.commit()
            m.ActivarMesas(conexion, mesa)
            f.EmitirFactura(conexion, id_pedido, 1)
            f.EmitirFactura(conexion,id_pedido,2)
            return True
        except psycopg2.Error as e:
            print("ERROR:", e)
            return False

    def ListarPedidosLow(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                       SELECT id,estado,mesa,usuarios
                       FROM pedidos
                       WHERE estado = true;
                   """
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                if resultado:
                    return resultado
        except psycopg2.Error as e:
            print("ERROR", e)
            return

    def ListarPedidos(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id,estado,mesa
                    FROM pedidos
                """
                cursor.execute(consulta)
                pedidos = cursor.fetchall()
                produc = Productos()
                pedidos_con_info = []

                for pedido in pedidos:
                    id_p = pedido[0]
                    estado=pedido[1]
                    mesa=pedido[2]
                    consultas = """
                        SELECT id_producto, cantidad
                        FROM productos_pedido
                        WHERE id_pedido = %s;
                    """
                    cursor.execute(consultas, (id_p,))
                    productos_pedido = cursor.fetchall()
                    productos_info = []
                    total = 0
                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        cantidad = int(producto[1])
                        total_producto = info_pro[3] * cantidad
                        total += total_producto
                        producto_info = {
                            "id_producto": info_pro[0],
                            "nombre": info_pro[1],
                            "precio_unitario": info_pro[3],
                            "cantidad": cantidad,
                            "total_producto": total_producto
                        }
                        productos_info.append(producto_info)
                    pedido_info = {
                        "id_pedido": id_p,
                        "estado":estado,
                        "mesa":mesa,
                        "productos": productos_info,
                        "total_pedido": total
                    }
                    f.ActualizarValorFactura(conexion,id_p,total)
                    pedidos_con_info.append(pedido_info)
                return pedidos_con_info
        except Exception as e:
            # Manejar excepciones aquí
            print(f"Error: {str(e)}")
            return []

        except psycopg2.Error as e:
            print("ERROR:", e)
            return []

    def ListarPedidosPendientes(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id,estado,mesa
                    FROM pedidos
                    WHERE estado = true; 
                """
                cursor.execute(consulta)
                pedidos = cursor.fetchall()
                produc = Productos()
                pedidos_con_info = []

                for pedido in pedidos:
                    id_p = pedido[0]
                    estado=pedido[1]
                    mesa=pedido[2]
                    consultas = """
                        SELECT id_producto, cantidad
                        FROM productos_pedido
                        WHERE id_pedido = %s;
                    """
                    cursor.execute(consultas, (id_p,))
                    productos_pedido = cursor.fetchall()
                    productos_info = []
                    total = 0
                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        cantidad = int(producto[1])
                        total_producto = info_pro[3] * cantidad
                        total += total_producto
                        producto_info = {
                            "id_producto": info_pro[0],
                            "nombre": info_pro[1],
                            "precio_unitario": info_pro[3],
                            "cantidad": cantidad,
                            "total_producto": total_producto
                        }
                        productos_info.append(producto_info)
                    pedido_info = {
                        "id_pedido": id_p,
                        "estado":estado,
                        "mesa":mesa,
                        "productos": productos_info,
                        "total_pedido": total
                    }
                    pedidos_con_info.append(pedido_info)
                return pedidos_con_info
        except Exception as e:
            print(f"Error: {str(e)}")
            return []

        except psycopg2.Error as e:
            print("ERROR:", e)
            return []

    def ListarPedidosPagos(self, conexion):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT id,estado,mesa
                    FROM pedidos
                    WHERE estado = false; 
                """
                cursor.execute(consulta)
                pedidos = cursor.fetchall()
                produc = Productos()
                pedidos_con_info = []

                for pedido in pedidos:
                    id_p = pedido[0]
                    estado=pedido[1]
                    mesa=pedido[2]
                    consultas = """
                        SELECT id_producto, cantidad
                        FROM productos_pedido
                        WHERE id_pedido = %s;
                    """
                    cursor.execute(consultas, (id_p,))
                    productos_pedido = cursor.fetchall()
                    productos_info = []
                    total = 0
                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        cantidad = int(producto[1])
                        total_producto = info_pro[3] * cantidad
                        total += total_producto
                        producto_info = {
                            "id_producto": info_pro[0],
                            "nombre": info_pro[1],
                            "precio_unitario": info_pro[3],
                            "cantidad": cantidad,
                            "total_producto": total_producto
                        }
                        productos_info.append(producto_info)
                    pedido_info = {
                        "id_pedido": id_p,
                        "estado":estado,
                        "mesa":mesa,
                        "productos": productos_info,
                        "total_pedido": total
                    }
                    pedidos_con_info.append(pedido_info)
                return pedidos_con_info
        except Exception as e:
            print(f"Error: {str(e)}")
            return []

        except psycopg2.Error as e:
            print("ERROR:", e)
            return []

    def ListarPedidosPorMesero(self, conexion,id_user):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                        SELECT id, estado, mesa
                        FROM pedidos
                        WHERE usuarios = %s; 
                    """
                cursor.execute(consulta, (id_user,))
                pedidos = cursor.fetchall()
                produc = Productos()
                pedidos_con_info = []

                for pedido in pedidos:
                    id_p = pedido[0]
                    estado=pedido[1]
                    mesa=pedido[2]
                    consultas = """
                        SELECT id_producto, cantidad
                        FROM productos_pedido
                        WHERE id_pedido = %s;
                    """
                    cursor.execute(consultas, (id_p,))
                    productos_pedido = cursor.fetchall()
                    productos_info = []
                    total = 0
                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        cantidad = int(producto[1])
                        total_producto = info_pro[3] * cantidad
                        total += total_producto
                        producto_info = {
                            "id_producto": info_pro[0],
                            "nombre": info_pro[1],
                            "precio_unitario": info_pro[3],
                            "cantidad": cantidad,
                            "total_producto": total_producto
                        }
                        productos_info.append(producto_info)
                    pedido_info = {
                        "id_pedido": id_p,
                        "estado":estado,
                        "mesa":mesa,
                        "productos": productos_info,
                        "total_pedido": total
                    }
                    pedidos_con_info.append(pedido_info)
                return pedidos_con_info
        except Exception as e:
            print(f"Error: {str(e)}")
            return []

    def ListarPedidosPorFecha(self, conexion, fecha,id_restaurante):
        produc = Productos()
        r = Restaurantes()
        try:
            with conexion.cursor() as cursor:
                consulta = """
                                SELECT id, estado, mesa
                                FROM pedidos
                                WHERE DATE("createdAt")=%s;
                            """
                cursor.execute(consulta, (fecha,))
                pedidos = cursor.fetchall()

                restaurantes_info = {}
                total_global = 0  # Agregamos esta variable para el total global

                for pedido in pedidos:
                    consultas = """
                                    SELECT id_producto, cantidad
                                    FROM productos_pedido
                                    WHERE id_pedido = %s;
                                """
                    cursor.execute(consultas, (pedido[0],))
                    productos_pedido = cursor.fetchall()

                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        restaurante = r.ListarRestaurantePorID(conexion, info_pro[4])
                        cantidad = int(producto[1])
                        total_producto = info_pro[3] * cantidad
                        if (str(info_pro[4]) == str(id_restaurante)):
                            total_global += total_producto
                        if restaurante[1] in restaurantes_info:
                            restaurantes_info[restaurante[1]]["total"] += total_producto
                        else:
                            restaurantes_info[restaurante[1]] = {
                                "total": total_producto,
                            }

                for restaurante, info in restaurantes_info.items():
                    print(f"\nRestaurante: {restaurante} / ${info['total']}")

                print(f"\nTotal Global: ${total_global}")
                return total_global

        except Exception as e:
            # Manejar excepciones aquí
            print(f"Error: {str(e)}")
            return []

    def ListarPedidosPorRestaurante(self, conexion,id_restaurante):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                        SELECT id, estado, mesa
                        FROM pedidos
                        WHERE estado=true;
                    """
                cursor.execute(consulta)
                pedidos = cursor.fetchall()
                produc = Productos()
                pedidos_con_info = []
                for pedido in pedidos:
                    id_p = pedido[0]
                    estado=pedido[1]
                    mesa=pedido[2]
                    consultas = """
                        SELECT id_producto, cantidad
                        FROM productos_pedido
                        WHERE id_pedido = %s;
                    """
                    cursor.execute(consultas, (id_p,))
                    productos_pedido = cursor.fetchall()
                    productos_info = []
                    total = 0
                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        id_r=info_pro[4]
                        if(int(id_r) == int(id_restaurante)):
                            cantidad = int(producto[1])
                            total_producto = info_pro[3] * cantidad
                            total += total_producto
                            producto_info = {
                                "id_producto": info_pro[0],
                                "nombre": info_pro[1],
                                "precio_unitario": info_pro[3],
                                "cantidad": cantidad,
                                "total_producto": total_producto
                            }
                            productos_info.append(producto_info)

                    pedido_info = {
                        "id_pedido": id_p,
                        "estado":estado,
                        "mesa":mesa,
                        "productos": productos_info,
                        "total_pedido": total
                    }
                    if(len(pedido_info['productos']) >0):
                        pedidos_con_info.append(pedido_info)
                return pedidos_con_info
        except Exception as e:
            print(f"Error: {str(e)}")
            return []

        except psycopg2.Error as e:
            print("ERROR:", e)
            return []





