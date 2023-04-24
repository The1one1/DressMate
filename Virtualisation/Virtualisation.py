import streamlit as st 
import requests
import io

url = "https://de89-104-197-163-57.ngrok-free.app/upload"

left, right = st.columns(2)
human_image = cloth_image = st.empty()
with left:
    cloth_image = st.file_uploader('Upload Cloth Image', type=['jpg', 'png', 'jpeg'])

with right:
    human_image = st.file_uploader('Upload Human Image', type=['jpg', 'png', 'jpeg'])

# @st.cache(ttl=3600, show_spinner=False) # set a cache for 1 hour with no spinner
# @st.experimental_time_it() # report time taken to execute function
@st.cache_resource()
def mask_image(cloth_image, human_image):
    payload={}
    files=[
        ('original',('00008_00.jpg',io.BytesIO(human_image.read()) ,'image/jpeg')),
        ('cloth',('00013_00.jpg',io.BytesIO(cloth_image.read()),'image/jpeg'))
    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.json()['result']

# if cloth_image and human_image:
  
if st.button('Search', type='primary'):
  with st.spinner('Searching...'):
          
    image_result = mask_image(cloth_image, human_image)
    
    left, middle, right = st.columns(3)
    with left:
      st.write("Cloth Image")
      st.image(cloth_image)  
      
    with middle:
      st.write("Human Image")
      st.image(human_image)
      
    with right:
      st.warning("Result")
      st.image(image_result)
      
    cloth_image = human_image = None
