from django.shortcuts import render
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import numpy as np
from .forms import CheckForm
# Create your views here.
def homepage(request):
    check=''
    with open('posinegavi/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        
    model=load_model('posinegavi/sentiment.h5')    
    
    if request.method == 'POST':
        form=CheckForm(request.POST)
        if form.is_valid():
            sentence=form.cleaned_data.get('text')
            sentence = tokenizer.texts_to_sequences(sentence)
            sentence = pad_sequences(sentence, maxlen=48, dtype='int32', value=0)
            if np.argmax(model.predict(sentence)[0])==1:
                check="Positive sentence"
                return render(request,template_name="posinegavi/home.html",context={
                    "form":form,
                    "check":check
                })
            elif np.argmax(model.predict(sentence)[0])==0:
                check="Negative sentence"
                return render(request,template_name="posinegavi/home.html",context={
                    "form":form,
                    "check":check
                })
        else:
            print('no')
    else:
        form=CheckForm()                   
    return render(request=request,template_name="posinegavi/home.html",context={
        "form":form,
        "check":check
    })