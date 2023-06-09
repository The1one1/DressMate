from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from streamlit_extras.switch_page_button import switch_page
from sklearn.metrics import pairwise_distances
import streamlit as st
from io import BytesIO
from PIL import Image
import pandas as pd
import numpy as np
import requests
import random
import cv2

# Load dataset features and asins
@st.cache_resource()
def load_data():
    bottleneck_features_train = np.load("numpy_file/16k_data_ResNet_features2.npy")
    asins = np.load("numpy_file/16k_data_ResNet_feature_asins2.npy")
    data = pd.read_pickle("pickels/16k_apparel_data.pkl")
    df_asins = list(data["asin"])
    return bottleneck_features_train, asins, data, df_asins


# Load pre-trained ResNet50 model
@st.cache_resource()
def load_model():
    model = ResNet50(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
    return model

# Define function to extract features from input image
@st.cache_resource()
def extract_features(filename, _model):
    image = cv2.imread(filename)
    image = cv2.resize(image, (224, 224))
    image = preprocess_input(image)
    features = _model.predict(image.reshape(1, 224, 224, 3))
    return features.flatten()


# Define function to get similar products for a given image file
@st.cache_resource(experimental_allow_widgets=True)
def get_similar_products_image(filename, num_results):
    # Load dataset features and asins
    bottleneck_features_train, asins, data, df_asins = load_data()
    
    # Load pre-trained ResNet50 model
    model = load_model()
    
    # Extract features from input image
    input_features = extract_features(filename, model)

    # Compute pairwise distances between input image features and dataset features
    pairwise_dist = pairwise_distances(bottleneck_features_train, input_features.reshape(1, -1))

    # Get indices of most similar products
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]

    # Display most similar products
    for i in range(len(indices)):
        rows = data[["medium_image_url", "title", "formatted_price", "color"]].loc[
            data["asin"] == asins[indices[i]]
        ]
        
        for indx, row in rows.iterrows():
            left, right = st.columns([1, 2])
            with left:
                image_url = row["medium_image_url"]
                # Open the bytes data using the Image class from PIL
                img = Image.open(BytesIO(requests.get(image_url).content))
                # Display the image using streamlit
                st.image(img)

            with right:
                st.write("Product Title: ", row["title"])
                st.write("Price: ", row["formatted_price"])
                st.write("Color: ", row["color"])
                st.write('Rating:', ('⭐'*random.randint(1,5)))
                
                st.button('virtual try-on', key=f"try-on-{i}", type='primary')
                # st.expander('Description', expanded=True)
