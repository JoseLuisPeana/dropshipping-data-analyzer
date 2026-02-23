import pandas as pd
import random

def generar_datos_prueba() -> pd.DataFrame:
    random.seed(42)
    data = []
    for i in range(1, 21):
        costo = round(random.uniform(5.0, 30.0), 2)
        precio_venta = round(costo * random.uniform(2.0, 4.0), 2)
        producto = {
            'product_name': f'Producto_Test_{i}',
            'category': random.choice(['Hogar', 'Mascotas', 'Tecnología', 'Belleza']),
            'cost_price': costo,
            'selling_price': precio_venta,
            'monthly_sales_volume': random.randint(10, 2000),
            'ad_spend': round(random.uniform(100.0, 3000.0), 2),
            'customer_rating': round(random.uniform(3.0, 5.0), 1),
            'search_trend_score': random.randint(10, 100)
        }
        data.append(producto)
    return pd.DataFrame(data)
