/* De los productos sin ventas en el presente año, monto total de ventas en el año anterior: */
SELECT producto.nombre_producto, producto.marca, COALESCE(SUM(venta.unidades_vendidas * producto.precio_unitario), 0) AS total_venta
FROM producto
LEFT JOIN venta ON venta.id_producto = producto.id_producto
               AND YEAR(venta.fecha_venta) = YEAR(CURRENT_DATE()) - 1
WHERE NOT EXISTS (
    SELECT 1
    FROM venta AS v
    WHERE v.id_producto = producto.id_producto
      AND YEAR(v.fecha_venta) = YEAR(CURRENT_DATE())
)
GROUP BY producto.nombre_producto, producto.marca;
