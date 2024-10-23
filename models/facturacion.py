from models.pedidos import *
from models.productos import *
from  models.restaurantes import *
import psycopg2
import uuid


class Factura:
    def __init__(self):
        pass

    def CrearFactura(self, conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    INSERT INTO facturas(id, id_pedido, "createdAt", "updatedAt")
                    VALUES (%s, %s, NOW(), NOW());
                """
                cursor.execute(consulta, (str(uuid.uuid4()), id_pedido))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def BuscarFacturaPorPedido(self, conexion, id_pedido):
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    SELECT * FROM facturas
                    WHERE id_pedido = %s;
                """
                cursor.execute(consulta, (id_pedido,))
                factura = cursor.fetchone()
                if factura:
                    return factura
                else:
                    return None
        except psycopg2.Error as e:
            print("ERROR", e)
            return None

    def ActualizarValorFactura(self, conexion, id_pedido, nuevo_valor):
        print(id_pedido)
        try:
            with conexion.cursor() as cursor:
                consulta = """
                    UPDATE facturas
                    SET total = %s, "updatedAt" = NOW()
                    WHERE id_pedido = %s;
                """
                cursor.execute(consulta, (nuevo_valor, id_pedido))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("ERROR", e)
            return False

    def EmitirFactura(self,conexion,id_pedido,tipo):
        produc = Productos()
        r=Restaurantes()
        if(tipo==1):
            print("Factura Mesero")
            try:
                with conexion.cursor() as cursor:
                    consulta = """
                            SELECT id,estado,mesa
                            FROM pedidos
                            WHERE id=%s;
                        """
                    cursor.execute(consulta, (id_pedido,))
                    pedido = cursor.fetchone()

                    consultas = """
                            SELECT id_producto, cantidad
                            FROM productos_pedido
                            WHERE id_pedido = %s;
                        """
                    cursor.execute(consultas, (id_pedido,))
                    productos_pedido = cursor.fetchall()

                    restaurantes_info = {}

                    for producto in productos_pedido:
                        info_pro = produc.ObtenerProductoPorID(conexion, producto[0])
                        restaurante = r.ListarRestaurantePorID(conexion, info_pro[4])
                        cantidad = int(producto[1])
                        total_producto = info_pro[3] * cantidad

                        if restaurante[1] in restaurantes_info:
                            restaurantes_info[restaurante[1]]["total"] += total_producto
                            restaurantes_info[restaurante[1]]["productos"].append({
                                "id_producto": info_pro[0],
                                "nombre": info_pro[1],
                                "precio_unitario": info_pro[3],
                                "cantidad": cantidad,
                                "total_producto": total_producto
                            })
                        else:
                            restaurantes_info[restaurante[1]] = {
                                "total": total_producto,
                                "productos": [{
                                    "id_producto": info_pro[0],
                                    "nombre": info_pro[1],
                                    "precio_unitario": info_pro[3],
                                    "cantidad": cantidad,
                                    "total_producto": total_producto
                                }]
                            }

                    print(restaurantes_info)
                    for restaurante, info in restaurantes_info.items():
                        print(f"\nRestaurante: {restaurante}")
                        print(f"{'Producto':<20} {'Cantidad':<10} {'Precio Unitario':<15} {'Total Producto':<15}")
                        for producto in info["productos"]:
                            print(
                                f"{producto['nombre']:<20} {producto['cantidad']:<10} {producto['precio_unitario']:<15} {producto['total_producto']:<15}")
                        print(f"\nTotal del Restaurante: {info['total']}\n{'-' * 60}")
            except Exception as e:
                # Manejar excepciones aquí
                print(f"Error: {str(e)}")
                return []

        if (tipo == 2):
                print("Factura Cliente")
                with conexion.cursor() as cursor:
                    consulta = """
                        SELECT id, estado, mesa
                        FROM pedidos
                        WHERE id = %s;
                    """
                    cursor.execute(consulta, (id_pedido,))
                    pedido = cursor.fetchone()
                    produc = Productos()
                    pedidos_con_info = []

                    id_p = pedido[0]
                    estado = pedido[1]
                    mesa = pedido[2]
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
                        "estado": estado,
                        "mesa": mesa,
                        "productos": productos_info,
                        "total_pedido": total
                    }
                    pedidos_con_info.append(pedido_info)

                print(pedidos_con_info)
                return pedidos_con_info









