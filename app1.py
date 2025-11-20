import streamlit as st

st.title("明日")

name = st.text_input("名前を入力")

st.write(name)

camera_phote = st.camera_input("写真を撮影してくれ")
if camera:
  st.image(camera, caption="写真",use_column_width=True)
