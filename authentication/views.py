from django.shortcuts import render
import google_auth

# Create your views here.
def index(request):
    return render(request, 'login.html')


def login(request):

    return render(request, 'success.html')