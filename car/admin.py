from django.contrib import admin
from .models import Car
from .forms import CarAdminForm

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
