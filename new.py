import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

DATA_URL = (
    "datasets_74977_169835_StudentsPerformance.csv"
)

st.title("Exploratory Data Analysis: Student Performance in the Exams")

st.sidebar.title("EDA: Student Performance in the Exams")

st.markdown("This application is a Streamlit dashboard used "
            "to analyze Student's Performance's in the Exams")
st.sidebar.markdown("This application is a Streamlit dashboard used "
            "to analyze Student Performance")


@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    
    return data

data = load_data()

st.table(data.head())

#Renaming Columns

data.rename(columns=({'gender':'Gender','race/ethnicity':'Race/Ethnicity'
                     ,'parental level of education':'Parental_Level_of_Education'
                     ,'lunch':'Lunch','test preparation course':'Test_Preparation_Course'
                      ,'math score':'Math_Score','reading score':'Reading_Score'
                     ,'writing score':'Writing_Score'}),inplace=True)


a = st.sidebar.selectbox('Insights', ['Insight 1', 'Insight 2', 'Insight 3', 'Insight 4'], key='2')

if a == 'Insight 1':
    sns.scatterplot(x=data['Reading_Score'],y=data['Writing_Score'])
    st.pyplot()
    st.header('Observations')
    st.subheader('Reading Score is directly proportional to the Writing Score of Students')

if a == 'Insight 2':
    sns.distplot(data['Reading_Score'])
    st.pyplot()
    st.header('Observations')
    st.subheader('Most of the Students score between 40 and 85 marks in the Reading Exam')
    
if a == 'Insight 3':
    sns.barplot(x=data['Gender'].value_counts().index,
               y=data['Gender'].value_counts().values,
            palette="Blues_d")
    st.pyplot()
    st.header('Observations')
    st.subheader('From above, we can observe that more number of female students appeared for the exams')
    
if a == 'Insight 4':
    sns.violinplot(x= data['Gender'],y=data['Math_Score'])
    st.pyplot()

    st.header('Observations')
    st.subheader('Most females scored between 40 and 80 marks in Math with a significant number scoring below 40 whereas most males scored between 40 and 85 and very few scored below 40')
    
