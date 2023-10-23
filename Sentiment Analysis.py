#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import string
import urllib
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import nltk 
import numpy as np
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# In[3]:


df= urllib.request.urlopen('https://www.indiatoday.in/world/story/israel-hamas-war-live-updates-israel-gaza-conflict-death-toll-netanyahu-gaza-strip-rocket-attack-2449896-2023-10-17').read()


# In[4]:


df


# In[5]:


df= BeautifulSoup(df,'lxml')


# In[6]:


print(df.find('title'))


# In[7]:


text= ""
for para in df.find_all('p'):
    text += para.text
print(text)    


# In[8]:


text= re.sub(r'\[[0-9]*\]',"", text)
#text= re.sub(r'\s+', '', text)
text= text.lower()
text= re.sub(r'\d', '',text)


# In[9]:


text


# In[10]:


for punctuation in string.punctuation:
    text = text.replace(punctuation, '')
text    


# In[11]:


text= word_tokenize(text)
text


# In[12]:


final_words = [word for word in text if word not in stopwords.words('english')]
final_words


# In[13]:


lemmatizer= WordNetLemmatizer()
words= [lemmatizer.lemmatize(token) for token in final_words]


# In[14]:


# Join the tokens back into a string
new_text= ' '. join(final_words)
new_text


# In[15]:


def sentiment_analyse(sentiment_text):
    score= SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    
sentiment_analyse(new_text)    


# In[16]:


blob = TextBlob(new_text)

# get the polarity score of the text
polarity = blob.sentiment.polarity

# determine if the text is subjective or objective
if polarity == 0:
    print("The text is objective.")
elif polarity > 0:
    print("The text is subjective and positive.")
else:
    print("The text is subjective and negative.")


# In[17]:


analysis = TextBlob(new_text).sentiment
print(analysis)


# In[18]:


from nltk.probability import FreqDist
wordfreq= FreqDist(final_words)
wordfreq


# In[19]:


plt.figure()
wordfreq.plot(14,  cumulative= False)


# In[20]:


from wordcloud import WordCloud
wordcloud= WordCloud(width= 2500, height= 1800).generate(new_text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show


# In[ ]:




