"""_summary_
"""
import pandas as pd

def calcular_metricas_dropshipping(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa un DataFrame con datos en crudo de productos y calcula
    el Margen, el ROAS estimado y el Score Ganador.

    Args:
        df (pd.DataFrame): Datos de productos con columnas 'selling_price',
                        'cost_price', 'monthly_sales_volume', 'ad_spend',
    'customer_rating', y 'search_trend_score'.

    Returns:
        pd.DataFrame: El mismo DataFrame con las nuevas métricas calculadas
        y ordenado por los mejores productos.
    """
    # 1. Calcular el margen de ganancia por unidad
    df['profit_margin_unit'] = df['selling_price'] - df['cost_price']

    # 2. Calcular los ingresos totales y el ROAS estimado
    df['total_revenue'] = df['selling_price'] * df['monthly_sales_volume']

    # Evitar división por cero en el gasto publicitario
    df['estimated_roas'] = df['total_revenue'] / df['ad_spend'].replace(0, 1)

    # 3. Calcular el Score Ganador (Normalizado)
    # Ponderación: Ventas(40%), ROAS(30%), Rating(20%), Tendencia(10%)
    max_sales = df['monthly_sales_volume'].max()
    max_roas = df['estimated_roas'].max()

    df['winner_score'] = (
        (df['monthly_sales_volume'] / max_sales * 40) +
        (df['estimated_roas'] / max_roas * 30) +
        (df['customer_rating'] / 5 * 20) +
        (df['search_trend_score'] / 100 * 10)
    )

    # 4. Ordenar los resultados de mayor a menor score y redondear
    df_result = df.sort_values(by='winner_score', ascending=False).round(2)

    return df_result
