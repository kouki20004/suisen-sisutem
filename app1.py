import streamlit as st

st.title("明日")

name = st.text_input("名前を入力")

st.write(name)

st.checkbox("同意します")
address = st.selectbox("次の中から現住所を教えて",["京都府","大阪府"])
st.write(address)

hobby= st.multiselect("趣味を次から複数選んでください",["映画","音楽"])
st.write(hobby)

score=st.slider("この映画を100点満点で評価してください",0,10,0)
st.write(score)

st.radio("性別を選んでくれ",["男性","女性"])

list=[
        {"latitude":35.05, "longitude":135.76},
        {"latitude":35.04, "longitude":135.75},
]
st.map(list)


camera = st.camera_input("写真を撮影してくれ")
if    camera:
        st.image(camera, caption="写真",use_column_width=True)
