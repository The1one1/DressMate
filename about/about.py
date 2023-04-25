import streamlit as st
import pandas as pd
from streamlit_extras.mention import mention

# Dataset used
DATASET_URL = "https://drive.google.com/file/d/1sPUUZBQ20MsI-V4NlEUc_y5RAfbPUfzv/view?usp=share_link"
CSV_FILE_PATH = 'filtered_apparel_data.csv'

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

# About section
st.markdown("# About")
st.write("""
        Our project aims to provide personalized recommendations for women's top fashion 
        based on their needs and preferences. We utilized the **ResNet50 model** for feature 
        extraction and analyzed product titles and descriptions for matching patterns. 
        We used the [Amazon Women Top Fashion dataset]({}) for training our model, resulting in 
        a highly accurate recommendation system.
        """.format(DATASET_URL))
  
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
    st.image("upload/1561.jpg", use_column_width=False)
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
        url=GITHUB_LINK + "The1one1",
    )
    
    mention(
        label="github",
        icon="github",
        url=GITHUB_LINK + "The1one1",
    )
    
    
with col3:
    st.image("upload/1561.jpg", use_column_width=False)
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