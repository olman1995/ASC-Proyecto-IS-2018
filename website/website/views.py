from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return HttpResponseRedirect("/inicio")