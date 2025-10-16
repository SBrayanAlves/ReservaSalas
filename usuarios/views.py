from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


