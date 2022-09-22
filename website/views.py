from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Submitted")
    context = {'form': form}
    return render(request, 'index.html', context)
