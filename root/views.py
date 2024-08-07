from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request ,'root/index.html')
def service(request):
    return render(request,'root/service-details.html')
def starter(request):
    return render(request,'root/starter-page.html')
