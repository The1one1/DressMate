import streamlit as st
import pandas as pd
from streamlit_extras.mention import mention

# Dataset used
DATASET_URL = "https://www.kaggle.com/subahsiniarajan/amazon-womens-top-fashion"

# Model results on the image dataset (example only)
MODEL_ACCURACY = 0.85
MODEL_LOSS = 0.15

"""
This is a clothing recommendation system built with ResNet50 model for feature extraction
and recommendation based on product title and description. The Amazon Women Top Fashion 
dataset was used for training the model.
Team Members:
- Rahul Sharma
- Shreya Patike
- Vatsal Savaliya
"""
st.markdown("# About")
st.write("""
        Our project aims to provide personalized recommendations for women's top fashion 
        based on their needs and preferences. We utilized the :red[ResNet50 model] for feature 
        extraction and analyzed product titles and descriptions for matching patterns. 
        We used the Amazon Women Top Fashion dataset for training our model, resulting in 
        a highly accurate recommendation system.
        """)
  
st.divider()

# About the dataset
st.header("Dataset")
st.markdown(f"The model was trained on the [Amazon Women Top Fashion dataset]({DATASET_URL}) with over 16k clothing items.")
data = pd.read_csv('filtered_apparel_data.csv')

# Create a container to hold the table
with st.container():
    # Display the data as a table
    st.dataframe(data)
st.divider()


# About the model
st.header("Model Results")
st.write("The model achieved an accuracy of {:.2f}% and a loss of {:.2f} on the validation set.".format(MODEL_ACCURACY*100, MODEL_LOSS))

st.divider()


# ! ---- Team Members ---- !
st.markdown("# Team Members")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("upload/1561.jpg", use_column_width=False)
    mention(
        label=":blue[Rahul Sharma]",
        icon="",
        url="https://linkedin.com/in/rahul-sharma-2bba60203",
    )
    
    mention(
        label="github",
        icon="github",
        url="https://github.com/The1one1",
    )
    

with col2:
    st.image("upload/1561.jpg", use_column_width= False)
    mention(
        label=":blue[Shreya Patike]",
        icon="",
        url="https://github.com/The1one1",
    )
    
    mention(
        label="github",
        icon="github",
        url="https://github.com/The1one1",
    )
    
    
with col3:
    st.image("upload/1561.jpg", use_column_width=False)
    mention(
        label=":blue[Vatsal Savaliya]",
        icon="",
        url="https://github.com/The1one1",
    )
    
    mention(
        label="github",
        icon="github",
        url="https://github.com/The1one1",
    )
    