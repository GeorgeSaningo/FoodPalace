from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from mainapp.app_forms import BookingForm, LoginForm
from mainapp.models import Booking


# Create your views here.
def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save()
            messages.info(request, "Booking was successfully added")
            return redirect("home")
        return render(request, "all_bookings.html", {"form": form})
    else:
        print("Home")
        form = BookingForm()
        return render(request, "index.html", {"form": form})


def booking(request, book_id):
    booking = Booking.objects.get(pk=book_id)
    if booking is not None:
        return render(request, 'index.html', {'booking': booking})
    else:
        raise Http404("Booking does not exist!")


def all_bookings(request):
    bookings = Booking.objects.all()
    paginator = Paginator(bookings, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "all_bookings.html", {"bookings": data})


def booking_delete(request, book_id):
    booking = get_object_or_404(Booking, pk=book_id)
    booking.delete()
    messages.warning(request, "This Booking was deleted permanently")
    return redirect("all")


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("all")
            messages.error(request, "Wrong Username or Password")
            return render(request, "login.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("signin")


def search_bookings(request):
    search_word = request.GET["search_word"]
    bookings = Booking.objects.filter(
        Q(name__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(bookings, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # Elastic search
    return render(request, "all_bookings.html", {"bookings": data})


def booking_details(request, book_id):
    booking = Booking.objects.get(pk=book_id)  # SELECT * FROM bookings WHERE id=1
    return render(request, "booking_details.html", {"booking": booking})
