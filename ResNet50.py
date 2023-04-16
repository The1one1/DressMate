from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.metrics import pairwise_distances
from matplotlib import gridspec
import streamlit as st
from io import BytesIO
from PIL import Image
import pandas as pd
import numpy as np
import requests
import cv2

# Load dataset features and asins
@st.cache_resource()
def load_data():
    bottleneck_features_train = np.load("16k_data_ResNet_features2.npy")
    asins = np.load("16k_data_ResNet_feature_asins2.npy")
    data = pd.read_pickle("16k_apparel_data.pkl")
    df_asins = list(data["asin"])
    return bottleneck_features_train, asins, data, df_asins


bottleneck_features_train, asins, data, df_asins = load_data()


# Load pre-trained ResNet50 model
@st.cache_resource()
def load_model():
    model = ResNet50(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
    return model

# Load pre-trained ResNet50 model
model = load_model()


# Define function to extract features from input image
@st.cache_resource()
def extract_features(filename):
    image = cv2.imread(filename)
    image = cv2.resize(image, (224, 224))
    image = preprocess_input(image)
    features = model.predict(image.reshape(1, 224, 224, 3))
    return features.flatten()


# Define function to get similar products for a given image file
def get_similar_products_image(filename, num_results):
    # Extract features from input image
    input_features = extract_features(filename)

    # Compute pairwise distances between input image features and dataset features
    pairwise_dist = pairwise_distances(
        bottleneck_features_train, input_features.reshape(1, -1)
    )

    # Get indices of most similar products
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]

    # Display most similar products
    for i in range(len(indices)):
        rows = data[["medium_image_url", "title", "formatted_price", "color"]].loc[
            data["asin"] == asins[indices[i]]
        ]
        for indx, row in rows.iterrows():
            left, right = st.columns(2)
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
                st.write("Color: ", row["color"])
            
            st.divider()
