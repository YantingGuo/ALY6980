from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from .models import Imagerecord,Inforecord
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def index(request):
    return render(request, "index.html")


def info_form(request):
    return render(request, 'info_form.html')


def upload_file(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs1 = FileSystemStorage(os.path.join(BASE_DIR, "app/static/images/upload/"))
            fs2 = FileSystemStorage(os.path.join(BASE_DIR, "app/static/images/upload/test/"))
            filename = fs1.save(myfile.name, myfile)
            filename = fs2.save(myfile.name, myfile)
            uploaded_file_url = '/static/images/upload/test/' + fs2.url(filename)
            image=Imagerecord(url=uploaded_file_url)
            t=image.label
            fs2.delete(myfile.name)
            return render(request, "file_upload.html", {
                'uploaded_file_url': '/static/images/upload/' + fs1.url(filename), 'issue': t
            })
    except Exception as e:
        print(e)
        return render(request, 'file_upload.html')
    return render(request, 'file_upload.html')


def finish(request):
    label = request.POST.get('type-issue')
    label2 = request.POST.get('class')
    location = request.POST.get('location')
    date = request.POST.get('date')
    email = request.POST.get('email')
    message = request.POST.get('message')
    print(label, label2, location, date, email, message)
    #context = {'data': data}
    return render(request, 'finish.html')





