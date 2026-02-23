import pandas as pd

def calcular_metricas_dropshipping(df: pd.DataFrame) -> pd.DataFrame:
    """Procesa los datos de productos y calcula el Score Ganador."""

    df['profit_margin_unit'] = df['selling_price'] - df['cost_price']
    df['total_revenue'] = df['selling_price'] * df['monthly_sales_volume']
    df['estimated_roas'] = df['total_revenue'] / df['ad_spend'].replace(0, 1)

    max_sales = df['monthly_sales_volume'].max()
    max_roas = df['estimated_roas'].max()

    df['winner_score'] = (
        (df['monthly_sales_volume'] / max_sales * 40) +
        (df['estimated_roas'] / max_roas * 30) +
        (df['customer_rating'] / 5 * 20) +
        (df['search_trend_score'] / 100 * 10)
    )

    df_result = df.sort_values(by='winner_score', ascending=False).round(2)
    return df_result
