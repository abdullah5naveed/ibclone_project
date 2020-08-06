from django.shortcuts import render
from imagebazar.models import *


# Create your views here.

def home(request):
    return render(request, 'imagebazar/home.html')



def viewimage(request):
    viewall = Images.objects.all()
    Data = { 'images': viewall }
    return render(request, 'imagebazar/viewimage.html', Data)