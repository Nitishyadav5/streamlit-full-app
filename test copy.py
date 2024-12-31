import streamlit as st
st.title("STUDENT DATA ENRTY FORM ")

st.form("User Information ")
firstname =st.text_input("first name")
lastname =st.text_input("last name")
title = st.selectbox("title",["", "mr.","ms.","dr."])
age = st.number_input("age, min_value = 18, max_value= 110",step=1)
nationality =st.selectbox(
    "nationality", ["", "africa", "antarctica","asia","Europe","north america", "oceania","south america"]
)


st.header("course information")
registration_Status =st.radio(
    "registraction status ", ["registered", "not registered"], index =1
)
num_courses = st.number_input(" completed course", min_value=0 ,step=1)
num_semesters = st.number_input(" semesters ", min_value= 0 ,step = 1)


st.header("term & conditions")
accepted = st.checkbox(" I accept the terms and conditions.")

submitted  = st.form_submit_button("submit")
