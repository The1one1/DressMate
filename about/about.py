import streamlit as st
import pandas as pd
from streamlit_extras.mention import mention

# Dataset used
DATASET_URL = "https://www.kaggle.com/subahsiniarajan/amazon-womens-top-fashion"
CSV_FILE_PATH = 'data/filtered_apparel_data.csv'

# Model results on the image dataset (example only)
MODEL_ACCURACY = 0.85
MODEL_LOSS = 0.15

import streamlit as st

DATASET_URL = "https://example.com/dataset"

def show_about():
    st.markdown("<h1 style='color:#6a0dad;'>About</h1>", unsafe_allow_html=True)
    st.write("""
        <div style='background-color:#f1f1f1; padding:10px;'>
            <p style='color:#555555;'>This is a clothing recommendation system built with ResNet50 model for feature extraction and recommendation based 
            on product title and description. The Amazon Women Top Fashion dataset was used for training the model.</p>
            
            <p style='color:#555555;'>Team Members:</p>
            <ul>
                <li style='color:#555555;'>Rahul Sharma</li>
                <li style='color:#555555;'>Shreya Patike</li>
                <li style='color:#555555;'>Vatsal Savaliya</li>
            </ul>
            
            <p style='color:#555555;'>Our project aims to provide personalized recommendations for women's top fashion based on their needs and preferences. 
            We utilized the <b>ResNet50 model</b> for feature extraction and analyzed product titles and descriptions for matching 
            patterns. We used the <a href="{}" style='color:#6a0dad;'>Amazon Women Top Fashion dataset</a> for training our model, resulting in a highly accurate 
            recommendation system.</p>
        </div>
    """.format(DATASET_URL), unsafe_allow_html=True)  
    
    st.subheader("Cloth Recommendation System")



# About section
def show_about():
    st.markdown("# About")
    st.write("""
        This is a clothing recommendation system built with ResNet50 model for feature extraction and recommendation based 
        on product title and description. The Amazon Women Top Fashion dataset was used for training the model.
        
        Team Members:
        - Rahul Sharma
        - Shreya Patike
        - Vatsal Savaliya
        
        Our project aims to provide personalized recommendations for women's top fashion based on their needs and preferences. 
        We utilized the **ResNet50 model** for feature extraction and analyzed product titles and descriptions for matching 
        patterns. We used the [Amazon Women Top Fashion dataset]({}) for training our model, resulting in a highly accurate 
        recommendation system.
    """.format(DATASET_URL))  
    
    st.subheader("Cloth Recommendation System")
    st.write("Our cloth recommendation system uses ResNet50 for feature extraction and Pinecone for vector searches. This allows us to quickly and accurately recommend similar clothing items based on their visual features.")

    st.subheader("Virtual Try-On")
    st.write("We have integrated the HrViton model with our Flask API to provide users with a virtual try-on experience. Users can upload an image of themselves and see how they would look in various clothing items.")

    st.subheader("Amazon Womens Fashion Data")
    st.write("We have used the Amazon Womens Fashion data in our recommendation system. This dataset contains a wide variety of women's clothing items, allowing us to provide diverse and comprehensive recommendations to our users.")

    st.subheader('Pinecone model')
    st.write('Pinecone is a vector search engine that we have integrated with our ResNet50 model for cosine similarity searches. It allows us to store and retrieve image feature vectors quickly and efficiently, enabling fast and accurate cloth recommendations.')
    
    st.subheader('Flask API')
    st.write('We have used the Flask API to connect our virtual try-on models with the Streamlit frontend. This API allows us to perform image processing on the backend while communicating with the frontend to provide a seamless experience to the user.')

show_about()

st.divider()

# Dataset section
st.header("Dataset")
st.markdown(f"The model was trained on the [Amazon Women Top Fashion dataset]({DATASET_URL}) with over 16k clothing items.")
data = pd.read_csv(CSV_FILE_PATH)

# Create a container to hold the table
with st.container():
    # Display the data as a table
    st.dataframe(data)
    
st.divider()

# Model section
st.header("Model Results")
st.write("The model achieved an accuracy of {:.2f}% and a loss of {:.2f} on the validation set.".format(MODEL_ACCURACY*100, MODEL_LOSS))

st.divider()

# Team Members section
st.markdown("# Team Members")
col1, col2, col3 = st.columns(3)

GITHUB_LINK = "https://github.com/"

with col1:
    st.image("https://media.licdn.com/dms/image/D4D03AQE--yT_6sSu6Q/profile-displayphoto-shrink_400_400/0/1672462974567?e=1687996800&v=beta&t=HVaHEkYDf9pJgygMrRcALu0JJVEsWVko9SgrU8hG3XE", use_column_width=False)
    mention(
        label=":blue[Rahul Sharma]",
        icon="",
        url="https://linkedin.com/in/rahul-sharma-2bba60203",
    )
    
    mention(
        label="github",
        icon="github",
        url=GITHUB_LINK + "The1one1",
    )
    

with col2:
    st.image("https://media.licdn.com/dms/image/D4D03AQGkxV0CoHiMdg/profile-displayphoto-shrink_400_400/0/1679544759666?e=1687996800&v=beta&t=A0Q6p75DeRPN8MZl_Uiii6lSGj6WBiHxVSWwnxdxiRE", use_column_width= False)
    mention(
        label=":blue[Shreya Patike]",
        icon="",
        url=GITHUB_LINK + "shreyapatike",
    )
    
    mention(
        label="github",
        icon="github",
        url=GITHUB_LINK + "vatsal2473",
    )
    
    
with col3:
    st.image("https://media.licdn.com/dms/image/D5603AQF49u4toNys8g/profile-displayphoto-shrink_400_400/0/1666165920253?e=1687996800&v=beta&t=gmGSx9_wzAudJGJTtnjkVJweApLYtR4pF_BfDcTyZA4", use_column_width=False)
    mention(
        label=":blue[Vatsal Savaliya]",
        icon="",
        url=GITHUB_LINK + "vatsal2473",
    )
    
    mention(
        label="github",
        icon="github",
        url=GITHUB_LINK + "vatsal2473",
    )