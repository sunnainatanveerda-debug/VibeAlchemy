# ✨ VibeAlchemy
### Turn Cultural Vibes Into Business Ideas

**Created by Sunnaina Tanveer**

VibeAlchemy is an AI-powered business idea generator that uses Qloo cultural intelligence to help aspiring entrepreneurs turn cultural interests into creative business concepts.

Whether you're planning a café, pop-up shop, dessert business, or small retail brand, VibeAlchemy helps you explore cultural connections and develop a business concept around your chosen audience, location, budget, and atmosphere.

## 🚀 Features

- **Cultural Entity Recognition:** Identify a musician, artist, film, food, or brand using Qloo.
- **Cultural Connections:** Explore related artists and other cultural entities.
- **Business Concept Generation:** Generate business concepts based on your selected business type and cultural inspiration.
- **Personalized Business Brief:** Include location, target audience, starting budget, and preferred atmosphere.
- **Cultural Inspiration:** Explore related genres and cultural themes.
- **Business Recommendations:** Get experience and product or menu ideas suited to the selected business type.
- **Downloadable Report:** Download your generated business concept as a text report.

## 🏪 Supported Business Types

1. Café
2. Pop-up shop
3. Dessert business
4. Small retail brand

## 🛠️ Technologies Used

- Python
- Streamlit
- Qloo API
- Requests
- Python-dotenv

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd VibeAlchemy
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install streamlit requests python-dotenv
```

### 6. Configure your Qloo API key

Create a `.env` file in the project folder:

```env
QLOO_API_KEY=your_qloo_api_key_here
```

Replace the placeholder with your own API key. Never publish your actual API key.

### 7. Run the application

```bash
streamlit run app.py
```

## 🔐 Security

- API credentials are stored in `.env`.
- `.env` and `.venv/` are excluded through `.gitignore`.
- Never commit private API keys or credentials to GitHub.

## ⚠️ Important Note

VibeAlchemy is a business ideation prototype. Cultural connections are exploratory insights, not proof of customer preferences, market demand, profitability, or guaranteed business success. Generated ideas should be validated through independent market research.

## 👩‍💻 Creator

**Sunnaina Tanveer**

Aspiring Data Scientist | Data Analytics & Business Intelligence

## 🙏 Acknowledgements

Built using the Qloo API and Streamlit.

---

*VibeAlchemy — Discover cultural connections. Imagine new possibilities. Build creative business concepts.*