from django.db import models as md


class Imagerecord(md.Model):
    url = md.URLField(max_length=1000, help_text='Enter a url that links to the article.')
    label = md.TextField()
    label2 = md.TextField()
    
    
class Inforecord(md.Model):
    reported_label = md.TextField()
    reported_label2 = md.TextField()
    location =  md.TextField()
    date = md.DateField(auto_now_add=True)
    email = md.EmailField(max_length=254)
    message =  md.TextField()