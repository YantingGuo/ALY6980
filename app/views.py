from __future__ import absolute_import, division, print_function, unicode_literals
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Imagerecord,Inforecord
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import time
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
def get_label(file_path):
          parts = tf.strings.split(file_path, os.path.sep)
          return parts[-2] == CLASS_NAMES
def decode_img(img):
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)
        return tf.image.resize(img, [IMG_WIDTH, IMG_HEIGHT])
def process_path(file_path):
        label = get_label(file_path)
        img = tf.io.read_file(file_path)
        img = decode_img(img)
        return img, label
def prepare_for_training(ds, cache=True, shuffle_buffer_size=1000):
        if cache:
            if isinstance(cache, str):
                   ds = ds.cache(cache)
            else:
                   ds = ds.cache()
        ds = ds.shuffle(buffer_size=shuffle_buffer_size)
        ds = ds.repeat()
        ds = ds.batch(BATCH_SIZE)
        return ds
def result_1(url):
        CLASS_NAMES=np.array(['reported', 'closed'])
        IMG_HEIGHT = 224
        IMG_WIDTH = 224      
        list_ds = tf.data.Dataset.list_files(str(url))
        labeled_ds = list_ds.map(process_path)
        train_ds = prepare_for_training(labeled_ds)
        image_batch, label_batch__ = next(iter(train_ds))
        t = time.time()
        import_path = 'app/DensNetmodel_aug_1st.h5'.format(int(t))
        reloaded = keras.models.load_model(import_path)
        reloaded_result_batch = reloaded.predict(image_batch)
        predicted_id = np.argmax(reloaded_result_batch, axis=-1)
        predicted_label_batch = CLASS_NAMES[predicted_id]
        label_id = np.argmax(label_batch, axis=-1)
        result=str(predicted_label_batch[0].title())
        return(result)
def result_2(url):
        CLASS_NAMES=np.array(['crack', 'hole', 'obstacle', 'plant', 'snow'])
        IMG_HEIGHT = 224
        IMG_WIDTH = 224      
        list_ds = tf.data.Dataset.list_files(str(url))
        labeled_ds = list_ds.map(process_path)
        train_ds = prepare_for_training(labeled_ds)
        image_batch, label_batch__ = next(iter(train_ds))
        t = time.time()
        import_path = 'app/DensNetmodel_multi.h5'.format(int(t))
        reloaded = keras.models.load_model(import_path)
        reloaded_result_batch = reloaded.predict(image_batch)
        predicted_id = np.argmax(reloaded_result_batch, axis=-1)
        predicted_label_batch = CLASS_NAMES[predicted_id]
        label_id = np.argmax(label_batch, axis=-1)
        result=predicted_label_batch[0].title()
        return(result)

def index(request):
    return render(request, "index.html")


def info_form(request):
    return render(request, 'info_form.html')


def upload_file(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(os.path.join(BASE_DIR, "app/static/images/upload"))
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = '/static/images/upload/' + fs.url(filename)
            l1=result_1(uploaded_file_url)
            l2=result_2(uploaded_file_url)
            image=Imagerecord(url=str(uploaded_file_url),label1=l1,label2=l2)
            image.save()
            if l1=='reported':
                t=True
            else:
                t=False
            return render(request, "file_upload.html", {
                'uploaded_file_url': uploaded_file_url, 'issue': t
            })
    except:
        return render(request, 'file_upload.html')
    return render(request, 'file_upload.html')


def finish(request):
    label = request.POST.get('type-issue')
    label2 = request.POST.get('class')
    location = request.POST.get('location')
    date = request.POST.get('date')
    email = request.POST.get('email')
    message = request.POST.get('message')
    info= Inforecord(reported_label=label, reported_labe2=label2, location=location, date=date, email=email, message=message)
    info.save()
    #context = {'data': data}
    return render(request, 'finish.html')





