from agent.agent import create_agents
# import json
def run_agent(user_input: str) -> str:
    agent = create_agents()
    response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
    products = []
    #ollama response needs to be loaded from json string, gemini response is already structured so we can directly access it
    # loaded_response = json.loads(response["messages"][1].content) 
    # --- Code for gemini model ---
    for product in response["structured_response"].products:
        products.append({
            "title": product.name,
            "price": product.price,
            "stars": product.rating,
            "reviews": product.reviews,
            "discount": product.discount,
            "image" : product.imgUrl,
            "url" : product.productURL
        })
        
    # --- Code for ollama ---
    # for product in loaded_response["products"]:
    #     products.append({
    #         "title": product["name"],
    #         "price": product["price"],
    #         "stars": product["rating"],
    #         "reviews": product["reviews"],
    #         "discount": product["discount"],
    #         "image" : product["imgUrl"],
    #         "url" : product["productURL"]
    #     })

    return products