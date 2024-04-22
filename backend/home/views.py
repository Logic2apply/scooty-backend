from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def vehicle(request):
    return render(request, 'home/vehicle.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'Thanks for contacting to Ecoride'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

        subject = f'{fname} {lname} contacted to Ecoride'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail( subject, message, email_from, recipient_list )

        contact = Contact(fname=fname, lname=lname, email=email, message=message)
        contact.save()
    return render(request, 'home/contact.html')
