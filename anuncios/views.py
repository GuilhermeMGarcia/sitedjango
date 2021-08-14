from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # TODO logíca da view
    return HttpResponse("Ola mundo")


