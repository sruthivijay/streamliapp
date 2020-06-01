
import streamlit as st
from streamlit import caching
import pandas as pd 
import os
import plotly.figure_factory as ff

st.title("Data Analysis Application")
#st.write("enter file name")

def enter_filename():
    global filename1
    filename1 = st.text_input('Enter reference filename')



def file_selector(folder_path='./data/'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)
activities = ["EDA","Plots","Model Building","About"]	
choice = st.sidebar.selectbox("Select Activities",activities)
if choice == "EDA":
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

    st.subheader("view summary statistics")
    if st.checkbox("Show selected columns"):
        columns = data.columns.tolist()
        selected_columns = st.multiselect("Select Columns",data.columns,default=None)
        if selected_columns == []:
            st.subheader("Please select a column from the dropdown")
        else:
            new_data = data[selected_columns]
            st.dataframe(new_data.describe())
    if st.checkbox("Missing value percentage"):
        missing_data = pd.DataFrame((data.isna().sum()/data.shape[1])*100)
        missing_data.reset_index(inplace=True)
        missing_data.columns = ["column_name","missing_percentage"]
        st.write(missing_data)
#feature = st.selectbox('Which feature?', df.columns[0:4])
    st.button("Distribution plots")
    if st.checkbox("Select columns"):
        columns = data.columns.tolist()
        selected_columns = st.multiselect("Select variables",data.columns,default=None)
        if selected_columns == []:
            st.text("Please select a column")
        else:
            list_ = []
            for column in selected_columns:
                list_.append(data[column].values)
            hist_data = list_
            group_labels = selected_columns
            colors = ['rgb(0, 0, 100)', 'rgb(0, 200, 200)']
            fig1 = ff.create_distplot(hist_data, group_labels,colors)
            fig1.update_layout(title_text='Customized Distplot')
            st.plotly_chart(fig1)


