import streamlit as st 
st.write('Hellow')
# import ResNet50 as rn
# import os
# import hydralit_components as hc
# from PIL import Image


# left, right = st.columns([1, 1])

# with left:
#     cloth = st.file_uploader("Cloth Image", key="cloth")
    
# with right:
#     human = st.file_uploader("Human Image", key="human")
   
    
# def recommend_Uploded_Image(cloth, human):
#     folder = "Cloth"
#     # save the uploaded file to the "uploads" folder with the same filename
#     filepath = os.path.join(folder, cloth.name)
#     with open(filepath, "wb") as f:
#         f.write(cloth.getbuffer())

#     image = Image.open(cloth)
#     cloth = st.sidebar.image(image, caption="Uploaded Image", width=200)
#     with hc.HyLoader('',hc.Loaders.pulse_bars,):
#         rn.get_similar_products_image(f"upload\{cloth.name}", 100)

# recommend_Uploded_Image(cloth, human)

# with hc.HyLoader('',hc.Loaders.pulse_bars,):
#         rn.get_similar_products_image("input_images/1561.jpg", 100)    