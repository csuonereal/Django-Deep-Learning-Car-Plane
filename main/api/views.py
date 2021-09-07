from django.shortcuts import render
from django.contrib import messages
from . import forms
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
import os
import random

def index(request):
    form = forms.DL_FORM(request.POST or None, request.FILES or None)
    context = {'form':form}
    if form.is_valid():
        img = form.save(commit=False)
        file_name = img.dl_image
        img.save()
        image_preprocessor(file_name, request)
        
    return render(request, 'index.html', context=context)

def image_preprocessor(file,request):
    image_name = str(file)
    path = os.path.join('C:\\Users\\user\\Desktop\\python\\Django-DL-2\\main\\media', image_name)
 
    img = load_img(path)
    resized_img = img.resize((224,224))
    image = np.array(resized_img)
    image = image.reshape(1,224,224,3)

    prediction = model_loader().predict(image)
    if prediction == 1:
        messages.success(request, "It's a plane")
    else:
        messages.success(request, "It's a car")



def model_loader():
    path = 'C:\Users\csuon\Desktop\Django-DL-2\jupyter'
    model = load_model(path)

    return model

