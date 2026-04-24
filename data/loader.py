import pandas as pd

def load_data():
    # Load datasets
    df_products = pd.read_csv("data/amazon_products.csv")
    df_categories = pd.read_csv("data/amazon_categories.csv")

    # Merge datasets
    df = pd.merge(
        df_products,
        df_categories,
        left_on="category_id",
        right_on="id",
        how="left"
    )

    return df


def clean_data(df):
    # Keep only headphones & earbuds
    df = df[df["category_name"] == "Headphones & Earbuds"].copy()

    # Select relevant columns
    df = df[[
        "title",
        "category_name",
        "price",
        "listPrice",
        "stars",
        "reviews",
        "isBestSeller",
        "imgUrl",
        "productURL"
    ]]

    # Remove invalid prices
    df = df[df["price"] > 0].copy()

    # Ensure numeric
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["listPrice"] = pd.to_numeric(df["listPrice"], errors="coerce")

    # ---- Discount ----
    df["discount"] = 0.0

    valid_mask = df["listPrice"] > df["price"]
    df.loc[valid_mask, "discount"] = (
        (df.loc[valid_mask, "listPrice"] - df.loc[valid_mask, "price"])
        / df.loc[valid_mask, "listPrice"]
    ) * 100

    df["discount"] = df["discount"].round(2)

    # ---- Product Type Classification ----
    df["product_type"] = "Headphones"

    df.loc[
        df["title"].str.contains("earbud|buds", case=False, na=False),
        "product_type"
    ] = "Earbuds"

    return df


def get_clean_data():
    df = load_data()
    df = clean_data(df)
    return df
