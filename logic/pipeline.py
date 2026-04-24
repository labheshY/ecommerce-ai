from logic.filter import apply_filters
from logic.weights import get_weights
from logic.ranking import rank_products

def recommend_products(df, query, product_type=None, budget=None):
    # Step 1: filters
    filtered_df = apply_filters(df, product_type, budget)

    # Step 2: weights
    weights = get_weights(query)

    # Step 3: ranking
    ranked_df = rank_products(filtered_df, weights)

    return ranked_df