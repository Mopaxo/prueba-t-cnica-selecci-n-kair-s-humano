/* Listado de ventas del mes actual: */
SELECT sucursal.nombre_sucursal, vendedor.nombre_vendedor, producto.marca, producto.nombre_producto,
       venta.fecha_venta, venta.unidades_vendidas, producto.precio_unitario,
       (venta.unidades_vendidas * producto.precio_unitario) AS valor_venta
FROM venta
JOIN producto ON venta.id_producto = producto.id_producto
JOIN vendedor ON venta.id_vendedor = vendedor.id_vendedor
JOIN sucursal ON venta.id_sucursal = sucursal.id_sucursal
WHERE MONTH(venta.fecha_venta) = MONTH(CURRENT_DATE())
  AND YEAR(venta.fecha_venta) = YEAR(CURRENT_DATE());
