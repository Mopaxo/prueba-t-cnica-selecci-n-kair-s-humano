/* Productos sin ventas en el presente año: */
SELECT producto.nombre_producto, producto.marca
FROM producto
WHERE NOT EXISTS (
    SELECT 1
    FROM venta
    WHERE venta.id_producto = producto.id_producto
      AND YEAR(venta.fecha_venta) = YEAR(CURRENT_DATE())
);
