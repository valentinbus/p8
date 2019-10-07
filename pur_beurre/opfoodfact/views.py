from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

request = HttpRequest()

# Create your views here.
def opfoodfact(request):
    
    return HttpResponse("<h1>I'm In</h1>")
