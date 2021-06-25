from django.shortcuts import render
from django.shortcuts import redirect
import  pyshorteners as ps
from .forms import Url
# Create your views here.
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        form = Url(request.POST)
        if form.is_valid():
            old = form.cleaned_data["url"]
            url  = old
            u=ps.Shortener().tinyurl.short(url)
        return render(request, 'index.html',{'link':u,'url':form})
    else:
        form = Url()
    return render(request, 'index.html', {'url':form})
