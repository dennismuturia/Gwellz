from django.shortcuts import render
#This is the piece of code for sending the EmailField
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForms

# Create your views here.
def contact(request):
    form = contactForms(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Gwellz.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message,emailFrom, emailTo, fail_silently=True)
        print ()
    return render(request, 'contact.html', locals())
