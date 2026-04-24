def get_weights(query: str):
    query = query.lower()

    # Default weights
    weights = {
        "stars": 0.4,
        "reviews": 0.3,
        "discount": 0.2,
        "bestseller": 0.1
    }

    # Discount-focused
    if any(word in query for word in ["discount", "deal", "cheap", "offer"]):
        weights = {
            "stars": 0.3,
            "reviews": 0.2,
            "discount": 0.4,
            "bestseller": 0.1
        }

    # Quality-focused
    elif any(word in query for word in ["best", "good", "quality"]):
        weights = {
            "stars": 0.5,
            "reviews": 0.3,
            "discount": 0.1,
            "bestseller": 0.1
        }

    # Popularity-focused
    elif any(word in query for word in ["popular", "trending", "most"]):
        weights = {
            "stars": 0.3,
            "reviews": 0.5,
            "discount": 0.1,
            "bestseller": 0.1
        }

    # Gaming / performance
    elif "gaming" in query:
        weights = {
            "stars": 0.5,
            "reviews": 0.4,
            "discount": 0.1,
            "bestseller": 0.0
        }

    return weights