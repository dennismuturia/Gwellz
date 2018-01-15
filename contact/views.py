from django.shortcuts import render
from .forms import contactForms

# Create your views here.
def contact(request):
    form = contactForms(request.POST or None)

    if form.is_valid:
        print (request.POST)
    return render(request, 'contact.html', locals())
