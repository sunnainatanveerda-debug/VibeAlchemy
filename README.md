# ✨ VibeAlchemy
### Turn Cultural Vibes Into Business Ideas

**Created by Sunnaina Tanveer**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://vibealchemy-q3392wjk4znqwp8wwi74ua.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Powered by Qloo](https://img.shields.io/badge/Powered%20by-Qloo-purple)](https://www.qloo.com/)

## 🌐 Live Demo

**Try VibeAlchemy:**  
https://vibealchemy-q3392wjk4znqwp8wwi74ua.streamlit.app/

VibeAlchemy is a cultural intelligence-powered business ideation application that helps aspiring entrepreneurs turn cultural interests into creative business concepts.

By combining user-provided business preferences with cultural insights retrieved through the Qloo API, VibeAlchemy explores related cultural entities, genres, and themes, then presents business concept ideas and recommendations.

## 🚀 Key Features

- **Cultural Entity Identification:** Identify a musician, artist, film, food, or brand using Qloo.
- **Cultural Connections:** Discover related cultural entities through Qloo.
- **Cultural Insights:** Explore related genres and cultural themes.
- **Business Concept Generation:** Develop business concepts using the selected cultural anchor and business preferences.
- **Personalized Business Brief:** Specify business type, location, target audience, starting budget, and atmosphere.
- **Business Recommendations:** Receive experience recommendations and product or menu ideas.
- **Downloadable Report:** Download a business concept report as a text file.

## 🏪 Supported Business Types

VibeAlchemy supports four business categories:

1. Café
2. Pop-up shop
3. Dessert business
4. Small retail brand

## 🔄 How It Works

1. Select a business type.
2. Enter your business location and target audience.
3. Choose your approximate starting budget and preferred atmosphere.
4. Enter a cultural anchor, such as a musician, artist, film, food, or brand.
5. VibeAlchemy uses the Qloo API to identify the cultural entity and retrieve cultural connections and insights.
6. Explore the generated business concept, cultural inspiration, and recommendations.
7. Download your business concept report.

## 🛠️ Technology Stack

- Python
- Streamlit
- Qloo API
- Requests
- python-dotenv

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sunnainatanveerda-debug/VibeAlchemy.git
```

### 2. Navigate to the project folder

```bash
cd VibeAlchemy
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment on Windows

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure your Qloo API key

Create a `.env` file in the project folder:

```env
QLOO_API_KEY=your_qloo_api_key_here
```

Replace the placeholder with your own Qloo API key. Never publish your actual API key.

### 7. Run the application

```bash
streamlit run app.py
```

## 🔐 Security

- API credentials are stored in `.env` locally.
- Streamlit Cloud uses its Secrets configuration for hosted deployment.
- `.env` and `.venv/` are excluded using `.gitignore`.
- Never commit private API keys or credentials to a public repository.

## ⚠️ Project Disclaimer

VibeAlchemy is a business ideation prototype. Cultural connections are exploratory insights and should not be interpreted as proof of customer preferences, market demand, profitability, or guaranteed business success. Business ideas should be independently researched and validated.

## 👩‍💻 Creator

**Sunnaina Tanveer**

Aspiring Data Scientist | Data Analytics | Business Intelligence

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Qloo](https://www.qloo.com/) — Cultural intelligence and insights.
- [Streamlit](https://streamlit.io/) — Application framework.

---

**VibeAlchemy — Discover cultural connections. Imagine new possibilities. Build creative business concepts.**
