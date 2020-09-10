from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request,'magazine/index.html')
def about(request):
    return render(request,'magazine/about.html')