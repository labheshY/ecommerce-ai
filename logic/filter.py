def apply_filters(df, product_type=None, budget=None):
    result = df.copy()

    if product_type:
        result = result[result["product_type"] == product_type]

    if budget:
        result = result[result["price"] <= budget]

    return result