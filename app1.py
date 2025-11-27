import streamlit as st

st.title("明日")

name = st.text_input("名前を入力")

st.write(name)

st.checkbox("同意します")
address = st.selectbox("次の中から現住所を教えて",["京都府","大阪府"])
st.write(address)

st.multiselect("趣味を次から複数選んでください",["映画","音楽"])


camera = st.camera_input("写真を撮影してくれ")
if    camera:
        st.image(camera, caption="写真",use_column_width=True)
