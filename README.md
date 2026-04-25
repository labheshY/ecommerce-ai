# 🛒 AI Headphone Shopping Assistant

An AI-powered recommendation system that helps users discover the best headphones and earbuds based on their preferences, budget, and intent.

This project combines **LLM-based query understanding** with a **custom ranking engine** built on real-world e-commerce data.

---

## 🚀 Features

* 🎧 Smart product recommendations (Headphones & Earbuds)
* 💬 Natural language query support (e.g., *“best earbuds under 50”*)
* 🧠 AI-powered intent understanding using:

  * Google Gemini (cloud)
  * Ollama (local LLM)
* ⚙️ Custom ranking engine based on:

  * Ratings ⭐
  * Reviews 🗣
  * Discount 🔥
  * Popularity 🏆
* 🖼 Clean UI with product cards, images, and links
* 🔄 Dynamic weighting based on user query (cheap, popular, best, etc.)

---

## 🧠 Models Used

### 🔹 Gemini (Cloud LLM)

* Used for:

  * Query parsing
  * Response explanation
* Model: `gemini-2.5-flash-lite`

### 🔹 Ollama (Local LLM)

* Used for:

  * Offline inference
  * Privacy-focused usage
* Model used:

  * `granite3.1-dense:2b`

---

## 📊 Dataset

* Source: Amazon Products Dataset (Kaggle, 2023)
* Contains:

  * Product title
  * Price & list price
  * Ratings & reviews
  * Category information
  * Bestseller flag

⚠️ Note:
The dataset is a **static snapshot (2023)** and not real-time.

---

## 🏗 Architecture

```text
User Query
   ↓
LLM (Gemini / Ollama)
   ↓
Intent + Entity Extraction
   ↓
Custom Logic Engine
   → Filtering
   → Dynamic Weight Selection
   → Ranking
   ↓
Top Products
   ↓
LLM (Explanation)
   ↓
Streamlit UI
```

---

## 📂 Project Structure

```text
ecommerce-ai/
│
├── agent/        # LLM pipeline (Gemini + Ollama)
├── logic/        # Filtering, ranking, weights
├── data/         # Data loader & preprocessing
├── assets/       # Images (placeholders)
├── app.py        # Streamlit UI
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/labheshY/ecommerce-ai.git
cd ecommerce-ai

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔑 Setup

### Gemini (Required for cloud mode)

Set your API key:

```bash
set GOOGLE_API_KEY=your_api_key   # Windows
```

---

### Ollama (Optional - local mode)

Install Ollama and run:

```bash
ollama run model_you_want
If already install just pull using
ollama pull your_model
```

---

## 💡 Example Queries

* “Best earbuds under 50”
* “Cheap headphones with good rating”
* “Most popular earbuds”
* “Good headphones with discount”

---

## 🧪 How It Works

* LLM extracts:

  * Product type
  * Budget
  * Intent (cheap, best, popular)
* Logic layer:

  * Filters dataset
  * Applies dynamic weights
  * Ranks products
* LLM generates explanation for results

---

## 📌 Future Improvements

* 🔄 Real-time product data (API integration)
* ❤️ User preferences & personalization
* 📊 Product comparison feature
* 🌐 Deployment (Streamlit Cloud / Render)

---

## 📸 Demo

<img width="684" height="706" alt="Capture123" src="https://github.com/user-attachments/assets/2bb62e42-3259-49bf-b597-4d37cb3ba71c" />


---

## 🤝 Contributing

Feel free to fork and improve the project.

---

## 📜 License

This project is for educational purpose.

---

## 👨‍💻 Author

**Labhesh Yawalkar**

---
