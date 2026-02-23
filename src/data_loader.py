import pandas as pd
import numpy as np

def cargar_datos_reales(ruta: str) -> pd.DataFrame:
    df = pd.read_csv(ruta, encoding='utf-8', low_memory=False)

    # Normalizar nombres de columnas
    df.columns = (df.columns.str.strip()
                            .str.lower()
                            .str.replace(' ', '_')
                            .str.replace('-', '_'))

    # Limpiar filas sin categoría o cantidad
    df.dropna(subset=['category', 'qty'], inplace=True)
    df = df[df['qty'] > 0]

    # Precio limpio
    df['amount'] = pd.to_numeric(
        df['amount'].astype(str).str.replace('[^0-9.]', '', regex=True),
        errors='coerce'
    ).fillna(0)

    df = df[df['amount'] > 0]

    # Agrupar por SKU
    ventas_por_sku = df.groupby('sku').agg(
        monthly_sales_volume=('qty', 'sum'),
        selling_price=('amount', 'mean'),
        category=('category', 'first')
    ).reset_index()

    # Construir DataFrame normalizado
    df_normalizado = pd.DataFrame()
    df_normalizado['product_name']         = ventas_por_sku['sku'].astype(str)
    df_normalizado['category']             = ventas_por_sku['category'].astype(str)
    df_normalizado['selling_price']        = ventas_por_sku['selling_price'].round(2)
    df_normalizado['cost_price']           = (df_normalizado['selling_price'] * 0.30).round(2)
    df_normalizado['monthly_sales_volume'] = ventas_por_sku['monthly_sales_volume'].astype(int)

    # Ad spend con variación real (5% a 40% del revenue)
    np.random.seed(42)
    df_normalizado['ad_spend'] = (
        df_normalizado['selling_price'] *
        df_normalizado['monthly_sales_volume'] *
        np.random.uniform(0.05, 0.40, size=len(df_normalizado))
    ).round(2)
    df_normalizado['ad_spend'] = df_normalizado['ad_spend'].replace(0, 1)

    df_normalizado['customer_rating']    = 4.2
    df_normalizado['search_trend_score'] = 50

    df_normalizado = df_normalizado.dropna().reset_index(drop=True)

    return df_normalizado
