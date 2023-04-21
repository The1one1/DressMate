import hydralit_components as hc
from pathlib import Path
from io import BytesIO
import streamlit as st
import requests
import random
import os

st.set_page_config(
    page_title="Cloth Recommendation System",
    page_icon=":shirt:",
    layout="wide",
    initial_sidebar_state="expanded",
)

import ResNet50 as rn
import searching as sr
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
def sidebar():
    with st.sidebar:
            
        input = st.multiselect("Select", ['Anna-Kaci',
        'Nanon', 'DSQUARED2', 'Soprano', 'Mogul Interior',
        'MKP Crop Top', 'PERI', 'BODEN', "H'nan", 'Black Temptation',
        'bankhunyabangyai store', 'Head Case Designs', 'No Boundaries', 'Worthington', 'Pleione', 'Material Girl',
        'Hip', 'Vansty', 'Exotic India', 'Ash City', 'Namnoi Clothing Store', 'Bar III', 'American Rag',
        'Tommy Hilfiger', 'Just Cavalli', 'ITMEIAL', 'Harlowe & Graham', 'YICHUN', 'XJBD', 'LOVELIF Sleeve Raglan'])

        price = st.slider("Price", 2, 100, 1)
        
        buttom = st.button("Apply", key="apply", type = 'primary')
    
    return input, price


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


def recommend_Uploded_Image(uploaded_file):
    folder = "upload"
    # save the uploaded file to the "uploads" folder with the same filename
    filepath = os.path.join(folder, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    image = Image.open(uploaded_file)
    cloth = st.sidebar.image(image, caption="Uploaded Image", width=200)
    with hc.HyLoader('',hc.Loaders.pulse_bars,):
        rn.get_similar_products_image(f"upload\{uploaded_file.name}", 100)    

    return None

def recommend_Query_Image(query):
    xc = sr.query_pinecone(query, top_k=60)
    xc = xc.to_dict()
    
    for i in range(len(xc['matches'])):
        row = xc['matches'][i]['metadata']
        left, right = st.columns([1, 2])
        with left:
            image_url = row["medium_image_url"]
            # Fetch image from URL using requests library
            response = requests.get(image_url)
            # Open the bytes data using the Image class from PIL
            img = Image.open(BytesIO(response.content))
            # Display the image using streamlit
            st.image(img)

        with right:
            st.write("Product Title: ", row["title"])
            st.write("Price: ", row["formatted_price"])
            st.write("brand: ", row['brand'])
            Star_List = ['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐']
            rating = random.randint(0, 4)
            st.write(Star_List[rating])

    return None


if(select_menu == "Home"):
    left, middle, right = st.columns([8, 0.9, 1])
    
    with left:
        query = st.text_input("", value='Latest Fashion')
        
    with middle:
        search = st.button(":mag:", key="search", type = 'primary')
        
    with right:
        uploaded_file = st.file_uploader("", key="upload")
    
    price, size = sidebar()
    
    if query and search:
        query = recommend_Query_Image(query)
        
    if uploaded_file:
        uploaded_file = recommend_Uploded_Image(uploaded_file)
    
elif (select_menu == "Virtualisation"): 
    with open('Virtualisation\Virtualisation.py') as f:
        code = f.read()
        exec(code)
        
elif (select_menu == "about"):
    with open('about/about.py') as f:
        code = f.read()
        exec(code)