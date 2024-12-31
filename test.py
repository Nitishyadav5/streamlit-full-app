import streamlit as st
st.title("hello, Nikki !")

st.write("this is my first streamlit app .")

st.text("this i plain text")

st.markdown("** this is markdown text.**")

name  = st.text_input("enter your name:!")
age = st.number_input ("enter your age :", min_value= 0 , max_value= 120)
st.write(f"hello {name}, you are {age} year old !")

uploaded_file = st.file_uploader (" choose a file ")
if uploaded_file:
    st.write("file up loaded:", uploaded_file.name)


st.sidebar.header("sidebar")
option =st.sidebar.selectbox("choose an option : ",) ["kgf","puspa 2"]
st.sidebar.write(f"you chose : {option}")
