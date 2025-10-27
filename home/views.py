from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request, 'home/home.html')