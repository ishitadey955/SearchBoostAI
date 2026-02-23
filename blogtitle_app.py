import time
import os
import json
import streamlit as st
from tenacity import retry, stop_after_attempt, wait_random_exponential
import pandas as pd
import io


def main():
    # Page config
    st.set_page_config(page_title="SearchBoost AI", layout="wide")

    # ✅ Initialize session state (FIXES KEYERROR)
    if "blog_titles" not in st.session_state:
        st.session_state["blog_titles"] = ""

    # Styling
    st.markdown("""
        <style>
        ::-webkit-scrollbar-track { background: #e1ebf9; }
        ::-webkit-scrollbar-thumb {
            background-color: #90CAF9;
            border-radius: 10px;
            border: 3px solid #e1ebf9;
        }
        ::-webkit-scrollbar-thumb:hover { background: #64B5F6; }
        ::-webkit-scrollbar { width: 16px; }
        div.stButton > button:first-child {
            background: #1565C0;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            font-weight: bold;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    st.title("✍️ SearchBoost AI -  SEO Blog Title & Headline Generator")

    # API Configuration
    with st.expander("API Configuration 🔑", expanded=False):
        st.markdown("""
        <a href="https://aistudio.google.com/app/apikey" target="_blank">Get Gemini API Key</a><br>
        <a href="https://serper.dev" target="_blank">Get SERPER API Key</a>
        """, unsafe_allow_html=True)

        user_gemini_api_key = st.text_input("Gemini API Key", type="password")
        user_serper_api_key = st.text_input("Serper API Key", type="password")

    # Input Section
    with st.expander("PRO-TIP - Follow steps below", expanded=True):

        col1, col2 = st.columns(2)

        with col1:
            input_blog_keywords = st.text_input(
                "🔑 Enter main keywords",
                placeholder="AI tools, digital marketing, SEO strategies"
            )

            input_blog_content = st.text_area(
                "📄 Blog content (Optional)"
            )

        with col2:
            input_title_type = st.selectbox(
                "📝 Blog Type",
                ('General', 'How-to Guides', 'Tutorials', 'Listicles',
                 'Newsworthy Posts', 'FAQs', 'Checklists/Cheat Sheets')
            )

            input_title_intent = st.selectbox(
                "🔍 Search Intent",
                ('Informational Intent', 'Commercial Intent',
                 'Transactional Intent', 'Navigational Intent')
            )

            input_language = st.selectbox(
                "🌐 Language",
                ["English", "Spanish", "French", "German",
                 "Chinese", "Japanese", "Other"]
            )

            if input_language == "Other":
                input_language = st.text_input("Specify Language")

            input_audience = st.text_input(
                "🎯 Target Audience (Optional)"
            )

    st.markdown("### How many titles?")
    num_titles = st.slider("Number of titles", 1, 10, 5)

    # 🔥 Generate Button
    if st.button("Generate Blog Titles"):

        with st.spinner("Generating blog titles..."):

            if not input_blog_keywords and not input_blog_content:
                st.error("Provide keywords OR blog content.")
            else:
                blog_titles = generate_blog_titles(
                    input_blog_keywords,
                    input_blog_content,
                    input_title_type,
                    input_title_intent,
                    input_language,
                    user_gemini_api_key,
                    num_titles,
                    input_audience
                )

                if blog_titles:
                    st.session_state["blog_titles"] = blog_titles
                else:
                    st.error("Failed to generate titles.")

    # ✅ Display titles OUTSIDE button block
    if st.session_state["blog_titles"]:

        st.markdown("## ✨ Generated Titles")

    titles_raw = st.session_state["blog_titles"]

    titles_list = [
        t.strip().lstrip('0123456789. ')
        for t in titles_raw.replace('. ', '\n').split('\n')
        if t.strip()
    ]

    for i, title in enumerate(titles_list, 1):
        st.markdown(f"{i}. {title}")

        # Excel Export
        titles_list = [
            t.strip().lstrip('0123456789. ')
            for t in st.session_state["blog_titles"].split('\n')
            if t.strip()
        ]

        df = pd.DataFrame({'Blog Title': titles_list})
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, engine='openpyxl')
        buffer.seek(0)

        st.download_button(
            "Download Titles as Excel",
            buffer,
            "blog_titles.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


def generate_blog_titles(input_blog_keywords,
                         input_blog_content,
                         input_title_type,
                         input_title_intent,
                         input_language,
                         user_gemini_api_key=None,
                         num_titles=5,
                         input_audience=None):

    prompt = f"""
Generate {num_titles} SEO-optimized blog titles.

Rules:
- Use main keyword
- 50-60 characters
- Include one question, one list, one how-to
- Mention target audience if provided
- Clear search intent
- Language: {input_language}

Keywords: {input_blog_keywords}
Content: {input_blog_content}
Audience: {input_audience}

Return only the titles.
"""

    return gemini_text_response(prompt, user_gemini_api_key)


@retry(wait=wait_random_exponential(min=1, max=60),
       stop=stop_after_attempt(3))
def gemini_text_response(prompt, user_gemini_api_key=None):

    import google.generativeai as genai

    api_key = user_gemini_api_key or os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("Gemini API Key missing.")
        return None

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Gemini Error: {e}")
        return None


if __name__ == "__main__":
    main()
