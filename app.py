from PIL import Image
import streamlit as st
from agent.pipeline import run_agent
from pathlib import Path

FALLBACK_IMG = Path(__file__).parent / "data" / "images" / "image.jpg"
image = Image.open(FALLBACK_IMG)

def display_image(url):
    try:
        if url and isinstance(url, str) and url.startswith("http"):
            st.image(url, use_container_width=True)
        else:
            st.image(image, use_container_width=True)
    except:
        st.image(image, use_container_width=True)

st.set_page_config(page_title="AI Shopping Assistant", layout="wide")

st.title("🛒 AI Headphone Shopping Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask for products (e.g., Best earbuds under 50)")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response
    response = run_agent(user_input)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown("### 🛍️ Recommended Products")

        cols = st.columns(2)

        for i, product in enumerate(response):
            with cols[i % 2]:
                with st.container():
                    display_image(product.get("image"))

                    title = product.get("title", "Unknown Product")[:80]

                    st.markdown(f"#### 🎧 {title}")

                    st.markdown(
                        f"""
                        **💰 Price:** ${product.get('price', 'N/A')}  
                        **⭐ Rating:** {product.get('stars', 'N/A')}  
                        **🗣 Reviews:** {product.get('reviews', 'N/A')}  
                        **🔥 Discount:** {product.get('discount', 0)}%
                        """
                    )

                    # Button-style link
                    if product.get("url"):
                        st.markdown(
                            f"""
                            <a href="{product['url']}" target="_blank">
                                <button style="
                                    background-color:#ff4b4b;
                                    color:white;
                                    padding:8px 12px;
                                    border:none;
                                    border-radius:6px;
                                    cursor:pointer;">
                                    🛒 View Product
                                </button>
                            </a>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown("---")
    st.session_state.messages.append({"role": "assistant", "content": response})