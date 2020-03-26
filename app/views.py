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
    uploaded_file_url = request.session.get('uploaded_file_url')
    return render(request, 'info_form.html', {
        'uploaded_file_url': uploaded_file_url
    })


def upload_file(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            prediction_path = "app/static/images/upload/test/"
            storage_path = "app/static/images/upload/"
            fs1 = FileSystemStorage(os.path.join(BASE_DIR, storage_path))
            fs2 = FileSystemStorage(os.path.join(BASE_DIR, prediction_path))
            filename = fs1.save(myfile.name, myfile)
            filename = fs2.save(myfile.name, myfile)
            uploaded_file_url = "/static/images/upload/" + fs1.url(filename)
            image=Imagerecord(url=uploaded_file_url)
            t=image.label
            fs2.delete(myfile.name)
            request.session['uploaded_file_url'] = uploaded_file_url
            return render(request, "file_upload.html", {
                'uploaded_file_url': uploaded_file_url, 'issue': t
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





