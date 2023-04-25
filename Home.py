from streamlit_option_menu import option_menu
from pathlib import Path
import streamlit as st
from io import BytesIO
from PIL import Image
import requests
import random

# set up page config
st.set_page_config(
    page_title="Cloth Recommendation System",
    page_icon=":shirt:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# title
st.title("Cloth Recommendation System")

import ResNet50 as rn
import searching as sr

# set up CSS
css_file = Path.cwd() / "style" / "main.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# components
def sidebar():
    options = [
        'Anna-Kaci', 'Nanon', 'DSQUARED2', 'Soprano', 'Mogul Interior',
        'MKP Crop Top', 'PERI', 'BODEN', "H'nan", 'Black Temptation',
        'bankhunyabangyai store', 'Head Case Designs', 'No Boundaries',
        'Worthington', 'Pleione', 'Material Girl', 'Hip', 'Vansty',
        'Exotic India', 'Ash City', 'Namnoi Clothing Store', 'Bar III',
        'American Rag', 'Tommy Hilfiger', 'Just Cavalli', 'ITMEIAL',
        'Harlowe & Graham', 'YICHUN', 'XJBD', 'LOVELIF Sleeve Raglan'
    ]
    input = st.multiselect("Select brand", options)
    price = st.slider("Price range", 2, 100, (1, 100))
    return input, price

def recommend_uploaded_image(uploaded_file):
    folder = "upload"
    filepath = (Path(folder) / uploaded_file.name).resolve()
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    image = Image.open(uploaded_file)
    cloth = st.sidebar.image(image, caption="Uploaded Image", width=200)
    rn.get_similar_products_image(f"{folder}/{uploaded_file.name}", 100)    

def recommend_query_image(query):
    xc = sr.query_pinecone(query, top_k=60)
    for i in range(len(xc['matches'])):
        row = xc['matches'][i]['metadata']
        left, right = st.columns([1, 2])
        with left:
            image_url = row["medium_image_url"]
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            st.image(img)
        with right:
            st.subheader(row["title"])
            st.write(f"Brand: {row['brand']}")
            st.write(f"Price: {row['formatted_price']}")
            st.write('Rating:', ('⭐'*random.randint(1,5)))
            st.button('Virtual Try-On', type = 'primary', key = i)

# navigation bar
select_menu = option_menu(
    menu_title=None, 
    options=["Home", "Virtualisation",  "about"], 
    icons=['house', 'cloud-upload', "info"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    } 
)

# page layout
if select_menu == "Home":
    with st.sidebar:
        brands, price_range = sidebar()
        
    left, middle, right = st.columns([8, 0.9, 1])
    with left:
        query = st.text_input("", value='Latest Fashion')
    with middle:
        search = st.button(":mag:", key="search", type='primary')   
    with right:
        uploaded_file = st.file_uploader("", key="upload")
    
    # apply filters
    if query and search:
        recommend_query_image(query)
    elif uploaded_file:
        recommend_uploaded_image(uploaded_file)
else:
    module_name = select_menu.lower()
    with open(f"{module_name}/{module_name}.py") as f:
        exec(f.read())