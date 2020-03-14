from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.http import HttpResponse

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def index(request):
    return render(request, "index.html")

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(os.path.join(BASE_DIR, "app/static/images/upload"))
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = '/static/images/upload/' + fs.url(filename)
        return render(request, "file_upload.html", {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file_upload.html')