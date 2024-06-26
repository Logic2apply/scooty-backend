from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from home.models import BookRide, Contact, EmailSubscribe
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "home/index.html")


def vehicle(request):
    return render(request, "home/vehicle.html")


@login_required(login_url="/auth/signin/")
def contact(request):
    if request.method == "POST":
        try:
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("email")
            message = request.POST.get("message")

            subject = f"Thanks for contacting to Ecoride"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            subject = f"{fname} {lname} contacted to Ecoride"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, email_from, recipient_list)

            contact = Contact(fname=fname, lname=lname, email=email, message=message)
            contact.save()
            messages.success(request, "Thanks for contacting to Ecoride")
        except:
            messages.error(request, "Something went wrong")
    return render(request, "home/contact.html")


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


@login_required(login_url="/auth/signin/")
def bookTestRide(request):
    if request.method == "POST":
        try:
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
            send_mail(subject, message, email_from, recipient_list)
            print("Mail sent successfully")

            bookride = BookRide(
                name=name,
                email=email,
                contact=contact,
                other=other,
                biketype=biketype,
                datetimef=datetimef,
            )
            bookride.save()
            messages.success(request, "Ride Booked Successfully")
            return redirect("/")
        except:
            messages.error(request, "Something went wrong")
            return redirect("/")


@login_required(login_url="/auth/signin/")
def feedback(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            subject = f"Feedback from {name}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                f"Message: {message}\n\nSent by:{email}\nECORIDE",
                email_from,
                recipient_list,
            )
            messages.success(request, "Feedback sent successfully")
            return redirect("/feedback/")
        except:
            messages.error(request, "Something went wrong")
    return render(request, "home/feedback.html")


@login_required(login_url="/auth/signin/")
def emailSubscribe(request):
    if request.method == "POST":
        try:
            email = request.POST.get("emails")

            subscribe = EmailSubscribe(email=email)
            subscribe.save()
            send_mail(
                "Subscribed to ECORIDE",
                f"Message: {email} subscribed to ECORIDE",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER, email],
            )
            messages.success(request, "You Subscribed to Ecoride Successfully!")
            return redirect("/")
        except:
            messages.error(request, "Something went wrong")
            return redirect("/")
    return redirect("/")


@login_required(login_url="/auth/signin/")
def accessories(request):
    return render(request, "home/accessories.html")


def products(request):
    products = {
        "items": [
            {
                "sys": {"id": "1"},
                "fields": {
                    "title": "Galaxy S10 5G",
                    "price": 910.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "2"},
                "fields": {
                    "title": "Galaxy S10+",
                    "price": 812.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "3"},
                "fields": {
                    "title": "Galaxy S10",
                    "price": 712.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "4"},
                "fields": {
                    "title": "Galaxy S10e",
                    "price": 622.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "5"},
                "fields": {
                    "title": "Galaxy A2 Core",
                    "price": 688.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "6"},
                "fields": {
                    "title": "Galaxy M30",
                    "price": 532.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "7"},
                "fields": {
                    "title": "Galaxy M20",
                    "price": 545.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "8"},
                "fields": {
                    "title": "Galaxy M10",
                    "price": 440.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "9"},
                "fields": {
                    "title": "Galaxy A80",
                    "price": 386.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "10"},
                "fields": {
                    "title": "Galaxy A70",
                    "price": 378.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "11"},
                "fields": {
                    "title": "Galaxy A60",
                    "price": 289.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
            {
                "sys": {"id": "12"},
                "fields": {
                    "title": "Galaxy A30",
                    "price": 248.99,
                    "image": {
                        "fields": {
                            "file": {
                                "url": "https://www.91-cdn.com/hub/wp-content/uploads/2023/11/Samsung-Galaxy-S24-series-1.jpg"
                            }
                        }
                    },
                },
            },
        ]
    }
    return JsonResponse(products)


def about(request):
    return render(request, "home/about.html")


def b450s(request):
    return render(request, "home/bikes/450s.html")


def b450x(request):
    return render(request, "home/bikes/450x.html")


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
