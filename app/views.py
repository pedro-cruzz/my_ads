from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def app_hello(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())