from django.contrib import admin
from mainapp.models import Booking

# Register your models here.

admin.site.site_header = "GS Data DB"
admin.site.index_title = "GS DB"


class BookingAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "date", "number_of_people"]
    search_fields = ["name", "email", "phone"]
    list_filter = ["name"]


admin.site.register(Booking, BookingAdmin)
