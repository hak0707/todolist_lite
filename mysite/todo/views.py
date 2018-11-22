# from django.shortcuts import render

# # Create your views here.
# def hello(req)

from django.http import HttpResponse

# def hello(request):
    # return HttpResponse("Hello world!")

def hello(request):
    return HttpResponse("<u style=\"background-color: royalblue;\">hello</u>")

def byeBye(request):
    return HttpResponse("Bye Bye")