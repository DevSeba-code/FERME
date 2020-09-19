from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home (request):
    return render(request, 'app1/index.html')


def login  (request):
    return render(request, 'app1/login.html')

def vista_cli_home (request):
    return render (request, 'app1/vista-cli-general.html')