import numpy as np

def rank_products(df, weights, top_n=5):
    df = df.copy()

    # Normalize reviews (log scaling)
    df["reviews_score"] = np.log1p(df["reviews"])

    # Bestseller to numeric
    df["bestseller_score"] = df["isBestSeller"].astype(int)

    # Final score
    df["score"] = (
        df["stars"] * weights["stars"] +
        df["reviews_score"] * weights["reviews"] +
        df["discount"] * weights["discount"] +
        df["bestseller_score"] * weights["bestseller"]
    )

    # Sort
    df = df.sort_values(by="score", ascending=False)

    return df.head(top_n)