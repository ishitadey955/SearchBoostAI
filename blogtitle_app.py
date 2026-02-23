import os
import streamlit as st
import pandas as pd
import io
from tenacity import retry, stop_after_attempt, wait_random_exponential


# ---------------------------
# MAIN APP
# ---------------------------
def main():
    st.set_page_config(page_title="SearchBoost AI", layout="wide")

    # Initialize session state
    if "blog_titles" not in st.session_state:
        st.session_state.blog_titles = ""

    # ---------------------------
    # Custom Styling
    # ---------------------------
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background: #1565C0;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    st.title("✍️ SearchBoost AI - SEO Blog Title Generator")

    # ---------------------------
    # API Configuration
    # ---------------------------
    with st.expander("API Configuration 🔑", expanded=False):

        st.markdown("[Get Gemini API Key](https://aistudio.google.com/app/apikey)")
        user_gemini_api_key = st.text_input("Gemini API Key", type="password")

    # ---------------------------
    # Input Section
    # ---------------------------
    with st.expander("PRO-TIP - Follow steps below", expanded=True):

        col1, col2 = st.columns(2)

        with col1:
            input_blog_keywords = st.text_input(
                "🔑 Enter main keywords",
                placeholder="AI tools, digital marketing, SEO strategies"
            )

            input_blog_content = st.text_area("📄 Blog content (Optional)")

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

            input_audience = st.text_input("🎯 Target Audience (Optional)")

    st.markdown("### How many titles?")
    num_titles = st.slider("Number of titles", 1, 10, 5)

    # ---------------------------
    # Generate Button
    # ---------------------------
    if st.button("Generate Blog Titles"):

        if not input_blog_keywords and not input_blog_content:
            st.error("Provide keywords OR blog content.")
            return

        with st.spinner("Generating blog titles..."):

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
                st.session_state.blog_titles = blog_titles
            else:
                st.error("Failed to generate titles.")

    # ---------------------------
    # Display Titles
    # ---------------------------
    if st.session_state.blog_titles:

        st.markdown("## ✨ Generated Titles")

        titles_list = parse_titles(st.session_state.blog_titles)

        for i, title in enumerate(titles_list, 1):
            st.markdown(f"**{i}. {title}**")

        # ---------------------------
        # Excel Download
        # ---------------------------
        df = pd.DataFrame({'Blog Title': titles_list})
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, engine='openpyxl')
        buffer.seek(0)

        st.download_button(
            label="📥 Download Titles as Excel",
            data=buffer,
            file_name="blog_titles.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )


# ---------------------------
# Parse Titles Cleanly
# ---------------------------
def parse_titles(raw_text):
    lines = raw_text.replace('. ', '\n').split('\n')
    titles = []
    for line in lines:
        clean = line.strip().lstrip('0123456789. ')
        if clean:
            titles.append(clean)
    return titles


# ---------------------------
# Generate Titles
# ---------------------------
def generate_blog_titles(
    input_blog_keywords,
    input_blog_content,
    input_title_type,
    input_title_intent,
    input_language,
    user_gemini_api_key=None,
    num_titles=5,
    input_audience=None
):

    prompt = f"""
Generate {num_titles} SEO-optimized blog titles.

Rules:
- Use main keyword
- 50-60 characters
- Include one question, one list, one how-to
- Mention target audience if provided
- Blog Type: {input_title_type}
- Search Intent: {input_title_intent}
- Language: {input_language}

Keywords: {input_blog_keywords}
Content: {input_blog_content}
Audience: {input_audience}

Return only the titles.
"""

    return gemini_text_response(prompt, user_gemini_api_key)


# ---------------------------
# Gemini API Call
# ---------------------------
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


# ---------------------------
if __name__ == "__main__":
    main()
