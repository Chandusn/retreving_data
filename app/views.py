from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LOW=WebPage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)
