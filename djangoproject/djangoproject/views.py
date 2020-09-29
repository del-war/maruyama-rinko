from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    title = 'MARUYAMA CHEMICAL COMPANY'
    dict = {
        'title':title
    }
    return render(request, 'home.html', context=dict)
