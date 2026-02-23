# 🚀 SearchBoostAI  
### AI-Powered SEO Blog Title Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![AI Powered](https://img.shields.io/badge/AI-Google%20Gemini-orange)

SearchBoostAI is a powerful AI-driven SEO blog title generator designed to help bloggers, marketers, founders, and content creators craft high-converting, search-optimized headlines in seconds.

Generate compelling blog titles aligned with search intent, audience targeting, and SEO best practices — effortlessly.

---

## ✨ Features

- ✅ AI-generated SEO-optimized blog titles  
- ✅ Supports multiple languages  
- ✅ Blog type customization (How-to, Listicles, Tutorials, etc.)  
- ✅ Search intent targeting  
- ✅ Target audience personalization  
- ✅ Excel export for generated titles  
- ✅ Clean and responsive Streamlit UI  
- ✅ Session-based state management  
- ✅ Automatic retry logic for API reliability  

---

## 🧠 How It Works

SearchBoostAI uses Google Gemini AI to:

- Analyze your blog keywords
- Understand optional blog content
- Adapt to blog type & search intent
- Include audience targeting
- Generate 50–60 character optimized titles
- Ensure question, list, and how-to variations

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/ishitadey955/SearchBoostAI.git
cd SearchBoostAI
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the App

```bash
streamlit run blogtitle_app.py
```

Your browser will open automatically at:

```
http://localhost:8501
```

---

# 🔐 API Configuration

SearchBoostAI uses **Google Gemini API**.

### Option 1 – Enter API Key in App
Use the **API Configuration** section inside the app.

### Option 2 – Set Environment Variable

**Windows**
```bash
set GEMINI_API_KEY=your_api_key_here
```

**Mac/Linux**
```bash
export GEMINI_API_KEY=your_api_key_here
```

Get your API key here:  
👉 https://aistudio.google.com/app/apikey

---

# 🌍 Deploy to Streamlit Cloud

1. Push your project to GitHub  
2. Go to https://share.streamlit.io  
3. Click **New App**
4. Connect your repository  
5. Select:
   - Branch: `main`
   - File: `blogtitle_app.py`
6. Add environment variable:
   - `GEMINI_API_KEY`

Click **Deploy**

Your app will be live within minutes 🚀

---

# 🖥 Simple Setup (Non-Technical Users – Windows)

1. Install Python from https://python.org  
   ⚠️ Make sure to check **"Add Python to PATH"**

2. Download this repository as ZIP  
3. Extract the folder  
4. Open Command Prompt  
5. Navigate to folder:
   ```bash
   cd C:\Path\To\SearchBoostAI
   ```
6. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
7. Run:
   ```bash
   streamlit run blogtitle_app.py
   ```

---

# 📊 Example Use Cases

- Bloggers optimizing SEO headlines  
- Affiliate marketers increasing CTR  
- Content agencies generating client titles  
- Startup founders creating ranking content  
- SEO professionals testing keyword variations  

---

# 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- Pandas
- Tenacity (retry handling)
- OpenPyXL (Excel export)

---

# 📁 Project Structure

```
SearchBoostAI/
│
├── blogtitle_app.py
├── requirements.txt
├── README.md
└── .streamlit/
```

---

# 📈 Roadmap

- [ ] Title scoring system
- [ ] SEO difficulty analysis
- [ ] Competitor SERP analysis
- [ ] Content brief generation
- [ ] SaaS version

---

# 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

# 📜 License

MIT License

---

# 💡 Why SearchBoostAI?

Instead of guessing which titles might rank…

SearchBoostAI generates structured, SEO-aligned headlines built for:

- Higher CTR
- Better rankings
- Clear search intent match
- Audience relevance

All in seconds.

---

# ⭐ Support

If you like this project:

- ⭐ Star the repository  
- 🍴 Fork it  
- 📢 Share it  

---
