from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from home.models import BookRide, Contact

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


# Bikes
# path("450s", views.b450s, name="450s"),
# path("450x/", views.b450x, name="450x"),
# path("aurali/", views.baurali, name="aurali"),
# path("ezgo/", views.bezgo, name="ezgo"),
# path("falcon/", views.bfalcon, name="falcon"),
# path("kriti/", views.bkriti, name="kriti"),
# path("lithinoli/", views.blithinoli, name="lithinoli"),
# path("loev/", views.bloev, name="loev"),
# path("minilithino/", views.bminilithino, name="minilithino"),
# path("one/", views.bone, name="one"),
# path("roma/", views.broma, name="roma"),
# path("storie/", views.bstorie, name="storie"),
# path("stormzx/", views.bstormzx, name="stormzx"),

def bookTestRide(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        other = request.POST.get("other")
        biketype = request.POST.get("biketype")
        datetimef = request.POST.get("datetime")

        # Email this information
        subject = f"Test Ride of BikeType {biketype} booked for date: {datetimef}"
        message = f"User: {name} successfully booked Test Ride of BikeType {biketype} for date: {datetimef}.\nEmail: {email}\nPhone:{contact}\nOther: {other}\n\nECORIDE"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, settings.EMAIL_HOST_USER]
        send_mail( subject, message, email_from, recipient_list )
        print("Mail sent successfully")

        bookride = BookRide(name=name, email=email, contact=contact, other=other, biketype=biketype, datetimef=datetimef)
        bookride.save()

        return redirect("/")


def b450s(request):
    return render(request, 'home/bikes/450s.html')

def b450x(request):
    return render(request, 'home/bikes/450x.html')


def baurali(request):
    return render(request, "home/bikes/aurali.html")

def bezgo(request):
    return render(request, "home/bikes/ezgo.html")

def bfalcon(request):
    return render(request, "home/bikes/falcon.html")

def bkriti(request):
    return render(request, "home/bikes/kriti.html")

def blithinoli(request):
    return render(request, "home/bikes/lithinoli.html")

def bloev(request):
    return render(request, "home/bikes/loev.html")

def bminilithino(request):
    return render(request, "home/bikes/minilithino.html")

def bone(request):
    return render(request, "home/bikes/one.html")

def broma(request):
    return render(request, "home/bikes/roma.html")

def bstorie(request):
    return render(request, "home/bikes/storie.html")

def bstormzx(request):
    return render(request, "home/bikes/stormzx.html")
