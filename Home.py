import streamlit as st
from pathlib import Path
import shutil
import os

st.set_page_config(
    page_title="Cloth Recommendation System",
    page_icon=":shirt:",
    layout="wide",
    initial_sidebar_state="expanded",
)

import ResNet50 as rn
from PIL import Image
from streamlit_option_menu import option_menu


# !----- Path Settings -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"


# ! ----CSS file -----
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Cloth Recommendation System")


# ! ---- Filters ----
with st.sidebar:
    price = st.slider("Price", 0, 1000, 100)
    size = st.selectbox("Size", ["S", "M", "L", "XL", "XXL"])

# !---- navigaton bar ----
select_menu = option_menu(
    menu_title = None, 
    options = ["Home", "Virtualisation",  "about"], 
    icons=['house', 'cloud-upload', "info"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    } 
)

if(select_menu == "Home"):
    with st.form("my_form"):
        # Create an input field for the file
        uploaded_file = st.file_uploader("Choose a file")
        submit_button = st.form_submit_button(label="Get Recommendation")

    if uploaded_file is not None:
        folder = "upload"
        # save the uploaded file to the "uploads" folder with the same filename
        filepath = os.path.join(folder, uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # st.success(f"Saved file: {uploaded_file.name}")

    # Use Pillow library to open and display the uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        cloth = st.sidebar.image(image, caption="     Uploaded Image", width=200)

    if submit_button:
        with st.spinner(text="In progress..."):
            rn.get_similar_products_image(f"upload\{uploaded_file.name}", 400)


elif (select_menu == "Virtualisation"): 
    with open('Virtualisation\Virtualisation.py') as f:
        code = f.read()
        exec(code)
        
elif (select_menu == "about"):
    st.write("This is an about page")