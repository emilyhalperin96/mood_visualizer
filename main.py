# HINTS 
#glop library to get a list of file names 
#use sorted function to sort the list 
import glob 
import streamlit as st 
import plotly.express as ps 
from nltk.sentiment import SentimentIntensityAnalyzer

#created a file path list
filepaths = sorted(glob.glob('diary/*.txt'))
#prints as something like ['diary/2023-10-21.txt', 'diary/2023-10-22.txt']

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

dates = [name.strip('.txt').strip('diary/') for name in filepaths]

st.tile('Diary Tone')
st.subheader('Positivity')
pos_figure = px.line(x=dates, y=positivity, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(pos_figure)

st.subheader('Negativity')
pos_figure = px.line(x=dates, y=positivity, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(pos_figure)