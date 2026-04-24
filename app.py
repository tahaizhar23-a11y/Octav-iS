import streamlit as st
from PIL import Image

st.set_page_config(page_title="Smart Vision App")

st.title("Smart Vision App")
st.write("Upload an image and it will be displayed below 👇")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
