import pandas as pd
import os
from src.processing import calcular_metricas_dropshipping
from src.data_loader import cargar_datos_reales

if __name__ == "__main__":
    print("=" * 50)
    print("  DROPSHIPPING DATA ANALYZER v2.0")
    print("=" * 50)

    ruta_raw = 'data/raw/amazon_sales.csv'

    if os.path.exists(ruta_raw):
        print(f"\n✅ Cargando datos reales desde: {ruta_raw}")
        df_crudo = cargar_datos_reales(ruta_raw)
    else:
        print("\n⚠️  Archivo no encontrado. Usando datos sintéticos...")
        from src.synthetic_data import generar_datos_prueba
        df_crudo = generar_datos_prueba()

    print(f"📦 Productos cargados: {len(df_crudo)}")

    print("\n⚙️  Calculando métricas y Score Ganador...")
    df_procesado = calcular_metricas_dropshipping(df_crudo)

    os.makedirs('data/output', exist_ok=True)
    ruta_salida = 'data/output/productos_analizados.csv'
    df_procesado.to_csv(ruta_salida, index=False)
    print(f"💾 Resultados guardados en: {ruta_salida}")

    print("\n" + "=" * 50)
    print("       🏆 TOP 5 PRODUCTOS GANADORES")
    print("=" * 50)
    top_5 = df_procesado[[
        'product_name', 'category', 'winner_score',
        'estimated_roas', 'profit_margin_unit', 'clasificacion'
    ]].head(5)
    print(top_5.to_string(index=False))

    print("\n" + "=" * 50)
    print("       📊 RESUMEN GENERAL")
    print("=" * 50)
    print(f"  Total productos analizados : {len(df_procesado)}")
    print(f"  Productos GANADORES        : {len(df_procesado[df_procesado['clasificacion'] == '🏆 GANADOR'])}")
    print(f"  Productos POTENCIALES      : {len(df_procesado[df_procesado['clasificacion'] == '⚡ POTENCIAL'])}")
    print(f"  Productos a DESCARTAR      : {len(df_procesado[df_procesado['clasificacion'] == '❌ DESCARTAR'])}")
    print(f"  Score promedio             : {df_procesado['winner_score'].mean():.2f}")
    print(f"  ROAS promedio              : {df_procesado['estimated_roas'].mean():.2f}x")
    print("=" * 50)

