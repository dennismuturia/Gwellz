from django.shortcuts import render
#This is the piece of code for sending the EmailField
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForms

# Create your views here.
def contact(request):
    form = contactForms(request.POST or None)
    subject = ''
    message = ''
    email = ''
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    if form.is_valid:
        print (request.POST)
    return render(request, 'contact.html', locals())
