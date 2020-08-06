from django.shortcuts import render
from imagebazar.models import *


# Create your views here.

def home(request):
    viewall = Images.objects.all()
    category = Categories.objects.all()
    Data = { 'images': viewall, 'category':category }

    return render(request, 'imagebazar/home.html', Data)


def viewcategory(request, cid):

    cate = Categories.objects.all()

    viewall = Images.objects.filter(category=cid)

    Data = { 'images': viewall, 'category':cate }
    return render(request, 'imagebazar/home.html', Data)