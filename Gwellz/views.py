from django.shortcuts import render
# We no longer need this
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
#This will be the contact page rendered
def contact(request):
    return render(request, 'contact.html')
