from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from mainapp.app_forms import BookingForm
from mainapp.models import Booking


# Create your views here.
def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save()
            messages.info(request, "Guest was Successfully saved")
            return redirect("home")
        return render(request, "index.html", {"form": form})
    else:
        print("Home")
        form = BookingForm()
        return render(request, "index.html", {"form": form})


def book_table(request):
    return None


def guest(request, guest_id):
    book = Booking.objects.get(pk=guest_id)
    if guest is not None:
        return render(request, 'index.html', {'guest': guest})
    else:
        raise Http404("Guest does not exist!")


def add(request):
    return None