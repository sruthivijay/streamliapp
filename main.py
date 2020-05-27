
import streamlit as st
from streamlit import caching
import pandas as pd 
import os

st.title("Data Analysis Application")
#st.write("enter file name")

def enter_filename():
    global filename1
    filename1 = st.text_input('Enter reference filename')



def file_selector(folder_path='./data/'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

enter_filename()
#caching.clear_cache()
#uploaded_file = st.file_uploader("Choose an file...", type=["csv","xlsx"])
if st.checkbox("upload file"):
    uploaded_file = st.file_uploader("Choose an file...", type=["csv","xlsx"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        #st.image(image, caption='Uploaded Data.', use_column_width=True)
        data.to_csv("./data/"+filename1+".csv",index=False)
        st.write("file uploaded successfully")


filename = file_selector()
st.write('You selected `%s`' % filename)
data = pd.read_csv(filename)
if st.checkbox("show data"):
    st.subheader("Sample data")
    st.dataframe(data.head(10))


