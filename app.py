import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()


tfid= pickle.load(open('Tfidfmodels.pkl','rb'))
model=pickle.load(open('kmeanmodel.pkl','rb'))
data= pd.read_csv('https://raw.githubusercontent.com/Diane10/news_classifier/main/All_combined_New_papers%20-%20Sheet1.csv')
      
# front end elements of the web page 
html_temp = """ 
<div style ="background-color:white;padding:15px"> 
<h1 style ="color:black;text-align:center;">News Classifier App</h1> 
</div> 
""" 
st.markdown(html_temp, unsafe_allow_html = True) 
default_value_goes_here = ""
Content = st.text_area("Paste your news story to classify:", default_value_goes_here)
result =""
data= pd.read_csv('https://raw.githubusercontent.com/Diane10/capstone/main/result.csv')

if st.button("Run Classifier"): 
  pred = model.predict(tfid.transform([Content]))
  if pred==1:
    st.write('Politics')   
    pred= int(pred)
    related = data[data['category']=='politics']["url"]
  elif pred==0:
    st.write('Entertainment')
    pred= int(pred)
    related = data[data['category']=='entertainment']["url"]
      
  elif pred==2:
    st.write('sport') 
    pred= int(pred)
    pred= int(pred)
    related = data[data['category']=='sports']["url"]
  elif pred==3:
    st.write('other(culture,celebreties,art)')
    pred= int(pred)
    related = data[data['category']=='culture']["url"]
  elif pred==4:
    st.write('business')
    pred= int(pred)
    term='business'
    related = data[data['category']=='business']["url"]
