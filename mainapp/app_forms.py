from django import forms
from mainapp.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "date", "min": "2023-01-01", "max": "2025-12-31"}),
            "number_of_people": forms.NumberInput(attrs={"max": 30, "min": 1})
        }
        labels = {
            "dateandtime": "Date and Time ",
            "email": "Email Address"
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)
