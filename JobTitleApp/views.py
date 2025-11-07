from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from datetime import date
import os
import json
from web3 import Web3, HTTPProvider
from django.core.files.storage import FileSystemStorage
import base64
import urllib, mimetypes
from django.http import HttpResponse
from sentence_transformers import SentenceTransformer #loading bert sentence model
import numpy as np
from keras.models import load_model
from string import punctuation
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

bert = SentenceTransformer('nli-distilroberta-base-v2')
print("Bert model created")
#define object to remove stop words and other text processing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

#define function to clean text by removing stop words and other special symbols
def cleanText(doc):
    tokens = doc.split()
    table = str.maketrans('', '', punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = [ps.stem(token) for token in tokens]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    tokens = ' '.join(tokens)
    return tokens

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})    

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})    

def LoginAction(request):
    if request.method == 'POST':
        global username
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username == 'admin' and password == 'admin':
            context= {'data': 'Welcome Admin'}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'Invalid login details'}
            return render(request, 'UserLogin.html', context)

def Predict(request):
    if request.method == 'GET':
       return render(request, 'Predict.html', {})

def PredictAction(request):
    if request.method == 'POST':
        class_label = ['Artificial Intelligence', 'Big Data Engineer', 'Business Analyst', 'Business Intelligent Analyst', 'Cloud Architect']
        testdata = request.POST.get('t1', False)
        extension_model = load_model("model/cnn_weights.hdf5")
        data = cleanText(testdata)
        temp = []
        temp.append(data)#add message to array
        embeddings = bert.encode(temp, convert_to_tensor=True)#convert message review to bert vector
        X = embeddings.numpy()#convert vector to numpy
        print(X.shape)
        X = X[:,0:300]
        #X = X.reshape(1, -1)
        print(X.shape)
        X = np.reshape(X, (X.shape[0], 10, 10, 3))
        predict = extension_model.predict(X)
        predict = np.argmax(predict)
        output = "Job Description = "+data+"<br/>"
        output += "PREDICTED JOB TITLE =====> "+class_label[predict]+"\n"       
        context= {'data': output}        
        return render(request, 'Predict.html', context)
    
        
