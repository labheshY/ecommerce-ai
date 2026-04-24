from langchain.tools import tool
from data.loader import get_clean_data
from logic.pipeline import recommend_products

# Load data once (important)
df = get_clean_data()


@tool
def recommend_tool(query: str) -> str:
    """
    Use this tool to recommend headphones or earbuds based on user query.
    """

    # Basic extraction (simple for now)
    query_lower = query.lower()

    product_type = None
    budget = None

    # Detect product type
    if "earbud" in query_lower or "buds" in query_lower:
        product_type = "Earbuds"
    elif "headphone" in query_lower:
        product_type = "Headphones"

    # Detect budget (very simple)
    import re
    match = re.search(r"\d+", query)
    if match:
        budget = float(match.group())

    # Call your pipeline
    results = recommend_products(
        df,
        query=query,
        product_type=product_type,
        budget=budget
    )

    # Format output
    output = []
    for _, row in results.iterrows():
        output.append(
            f"{row['title']} | Price: {row['price']} | ⭐ {row['stars']} | Reviews: {row['reviews']} | Discount: {row['discount']}%"
        )

    return "\n".join(output)