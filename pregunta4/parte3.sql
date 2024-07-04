/* Productos con más de 1000 unidades vendidas en los últimos 2 meses: */
SELECT producto.nombre_producto, producto.marca, SUM(venta.unidades_vendidas) AS unidades_vendidas
FROM venta
JOIN producto ON venta.id_producto = producto.id_producto
WHERE venta.fecha_venta >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 MONTH)
GROUP BY producto.nombre_producto, producto.marca
HAVING SUM(venta.unidades_vendidas) > 1000;
