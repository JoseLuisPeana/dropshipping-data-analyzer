import pandas as pd
import random
from src.processing import calcular_metricas_dropshipping

def generar_datos_prueba() -> pd.DataFrame:
    """Genera 20 productos de prueba para simular datos extraídos."""
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

if __name__ == "__main__":
    print("Iniciando análisis de dropshipping...")

    df_crudo = generar_datos_prueba()
    print(f"Datos obtenidos: {len(df_crudo)} productos.")

    print("Calculando métricas y Score Ganador...")
    df_procesado = calcular_metricas_dropshipping(df_crudo)

    ruta_guardado = 'data/productos_analizados.csv'
    df_procesado.to_csv(ruta_guardado, index=False)

    print(f"\n¡Análisis completado! Resultados guardados en: {ruta_guardado}")

    print("\n--- TOP 3 PRODUCTOS GANADORES ---")
    top_3 = df_procesado[['product_name', 'category', 'winner_score', 'estimated_roas']].head(3)
    print(top_3)
