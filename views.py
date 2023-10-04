from django.shortcuts import render

# Create your views here.
def index(request):
    render(request,"index.html")
    
def about(request):
    render(request,"about.html")

def register(request):
    render(request,"register.html")