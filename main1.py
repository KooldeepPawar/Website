import streamlit as st 
import pandas as pd

st.title("Welcome to WSCube")
st.header("Python")
st.subheader("Learning")
st.markdown("I love programing")

name = st.text_input("Enter your Name ")
fname = st.text_input("Enter your Father's Name")
adress = st.text_area("Enter your address ... ")
classdata = st.selectbox("Enter your class ",(1,2,3,4,5))

button = st.button("Submit")

if button :
    st.markdown(f"My name is {name} son of {fname} leaving at {adress} and studying in class {classdata} ")

dataset = pd.read_csv("BFL Jira.csv")
st.dataframe(dataset)