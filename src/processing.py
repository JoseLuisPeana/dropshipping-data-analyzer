import pandas as pd

def calcular_metricas_dropshipping(df: pd.DataFrame) -> pd.DataFrame:

    df['profit_margin_unit'] = (df['selling_price'] - df['cost_price']).round(2)
    df['profit_margin_pct']  = ((df['profit_margin_unit'] / df['selling_price']) * 100).round(2)
    df['total_revenue']      = (df['selling_price'] * df['monthly_sales_volume']).round(2)
    df['total_profit']       = (df['profit_margin_unit'] * df['monthly_sales_volume']).round(2)
    df['estimated_roas']     = (df['total_revenue'] / df['ad_spend'].replace(0, 1)).round(2)

    def normalizar(serie):
        rango = serie.max() - serie.min()
        return (serie - serie.min()) / rango if rango != 0 else 0

    df['winner_score'] = (
        normalizar(df['monthly_sales_volume']) * 40 +
        normalizar(df['estimated_roas'])        * 30 +
        (df['customer_rating'] / 5)             * 20 +
        (df['search_trend_score'] / 100)        * 10
    ).round(2)

    def clasificar(score):
        if score >= 55:
            return '🏆 GANADOR'
        elif score >= 30:
            return '⚡ POTENCIAL'
        else:
            return '❌ DESCARTAR'

    df['clasificacion'] = df['winner_score'].apply(clasificar)
    df_result = df.sort_values(by='winner_score', ascending=False).reset_index(drop=True)

    return df_result
