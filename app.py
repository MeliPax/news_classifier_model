import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# import preprocess_kgptalkie as ps
# import re
label_enc = LabelEncoder()


# clean_doc=pickle.load(open('clean_doc.obj','rb'))
tfid= pickle.load(open('Tfidfmodels.pkl','rb'))
model=pickle.load(open('kmeanmodel.pkl','rb'))
data= pd.read_csv('news.csv')

data['category']=data['category'].apply(lambda x:x.lower())

# # Function to cleaning article headings
# def clean_text(x):
#     x = str(x).lower().replace('\\', '').replace('_', ' ')
#     x = ps.remove_emails(x)
#     x = ps.remove_urls(x)
#     x = ps.remove_html_tags(x)
#     x = ps.remove_accented_chars(x)
#     x = ps.remove_special_chars(x)
#     x = re.sub("(.)\\1{2,}", "\\1", x)
#     return x

# def clean_texts(text):
#   # Removing html characters
#   text = HTMLParser().unescape(text)
#   # Removing urls and hashtags
#   text = re.sub(r'https?:\/\/.\S+', "", text)
#   text = re.sub(r'#', '', text)
#   text = re.sub(r'^RT[\s]+', '', text)
#   # Contradiction replacement
#   dictionary={"'s":" is","n't":" not","'m":" am","'ll":" will",
#            "'d":" would","'ve":" have","'re":" are"}
#   for key,value in dictionary.items():
#       if key in text:
#           text = text.replace(key, value)
#   # Convert to lower case
#   text = text.lower()
#   # Removing stopwords
#   nltk.download('stopwords')
#   stopwords_eng = stopwords.words('english') 
#   text_tokens = text.split()
#   text_list=[]
#   for word in text_tokens:
#       if word not in stopwords_eng:
#           text_list.append(word)
#   # Remove punctuations
#   clean_text = []
#   for word in text_list:
#       if word not in string.punctuation:
#           clean_text.append(word)
#   return clean_text

def predict_news(text):
#     content = clean_texts(listToString(content[3]))
# #     encoded_text = tokenizer.texts_to_sequences([content])
#     max_length = 2
#     padded_text = pad_sequences(encoded_text, maxlen=max_length, padding='post')
    y_pred = model.predict(tfid.transform([text]))
    return y_pred

# front end elements of the web page 
html_temp = """ 
<div style ="background-color:white;padding:13px"> 
<h1 style ="color:black;text-align:center;">News classifier</h1> 
</div> 
""" 
st.markdown(html_temp, unsafe_allow_html = True) 
default_value_goes_here = ""
Content = st.text_area("Enter story text to be predected in the below textbox:", default_value_goes_here)
result =""

# content = clean_text(Content)

# if st.button("Run prediction"): 
#   pred = model.predict(tfid.transform([Content]))
result=''


if st.button("Run Classifier"): 
  pred = predict_news(Content)
  
  if pred==0:
    result='business'
    pred= int(pred)
    term='business'
    related = data[data['category']=='business']["url"]
      
  elif pred==1:
    result='other(culture,celebreties,art)'
    pred= int(pred)
    related = data[data['category']=='culture']["url"]
      
  elif pred==2:
    result='Entertainment'
    pred= int(pred)
    related = data[data['category']=='entertainment']["url"]

  elif pred==3:
    result='Politics'   
    pred= int(pred)
    related = data[data['category']=='politics']["url"]
  
  elif pred==4:
    result='sport' 
    pred= int(pred)
    related = data[data['category']=='sports']["url"]

  st.success('The predicted category of the article is: {}'.format(result))
  html_temp = """
  <div style="background-color:grey;padding:6px">
  <h6 style="color:white;">Other related articles</h3>
  </div>
  """
  st.markdown(html_temp, unsafe_allow_html=True)
  st.write(related)
