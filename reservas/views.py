from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return None