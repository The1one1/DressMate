import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cloth Recommendation System",
    page_icon=":shirt:",
    layout="wide",
    initial_sidebar_state="expanded",
)

import ResNet50 as rn
from PIL import Image


# !----- Path Settings -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"


# ! ----CSS file, PDF and Profile Pic -----
with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

st.title("Cloth Recommendation System")


left, right = st.columns([1, 2])

# with left:
uploaded_file1 = st.file_uploader(
    label = "", type=["jpg", "jpeg", "png"], key="cloth"
)
# Use Pillow library to open and display the uploaded image

# with right:
if uploaded_file1 is not None:
    image = Image.open(uploaded_file1)
    cloth = st.sidebar.image(image, caption="Uploaded Image", width=200)


if st.button("Get Recommendation"):
    with st.spinner(text="In progress..."):
        rn.get_similar_products_image('1.jpg', 400)
