from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from django.db import models as md
from tensorflow.keras import datasets, layers, models
import numpy as np
import time

class Imagerecord(md.Model):
    url = md.URLField(max_length=1000, help_text='Enter a url that links to the article.')
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
    def result_1(self):
        CLASS_NAMES=np.array(['closed', 'reported'])
        IMG_HEIGHT = 224
        IMG_WIDTH = 224      
        list_ds = tf.data.Dataset.list_files(str(self.url))
        labeled_ds = list_ds.map(process_path)
        train_ds = prepare_for_training(labeled_ds)
        image_batch, label_batch__ = next(iter(train_ds))
        t = time.time()
        import_path = 'app/DensNetmodel_aug_1st.h5'.format(int(t))
        reloaded = tf.keras.models.load_model(import_path)
        reloaded_result_batch = reloaded.predict(image_batch2)
        predicted_id = np.argmax(reloaded_result_batch, axis=-1)
        predicted_label_batch = CLASS_NAMES[predicted_id]
        label_id = np.argmax(label_batch, axis=-1)
        result=predicted_label_batch[0].title()
        return(result)
    def result_2(self):
        CLASS_NAMES=np.array(['crack', 'hole', 'obstacle', 'plant', 'snow'])
        IMG_HEIGHT = 224
        IMG_WIDTH = 224      
        list_ds = tf.data.Dataset.list_files(str(self.url))
        labeled_ds = list_ds.map(process_path)
        train_ds = prepare_for_training(labeled_ds)
        image_batch, label_batch__ = next(iter(train_ds))
        t = time.time()
        import_path = 'app/DensNetmodel_multi.h5'.format(int(t))
        reloaded = tf.keras.models.load_model(import_path)
        reloaded_result_batch = reloaded.predict(image_batch2)
        predicted_id = np.argmax(reloaded_result_batch, axis=-1)
        predicted_label_batch = CLASS_NAMES[predicted_id]
        label_id = np.argmax(label_batch, axis=-1)
        result=predicted_label_batch[0].title()
        return(result)
    label = property(result_1)
    label2 = property(result_2)
    
    
class Inforecord(md.Model):
    reported_label = md.TextField()
    reported_label2 = md.TextField()
    location =  md.TextField()
    date = md.DateField(auto_now_add=True)
    email = md.EmailField(max_length=254)
    message =  md.TextField()