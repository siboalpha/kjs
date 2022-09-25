from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form}
    return render(request, 'index.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')
