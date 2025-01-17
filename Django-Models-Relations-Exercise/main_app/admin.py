from django.contrib import admin

from main_app.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model','year', 'owner', 'car_details']

    @staticmethod
    def car_details(obj):
        try:
            owner_name = obj.owner.name

        except AttributeError:
            owner_name = 'No owner'

        try:
            registration = obj.registration.registration_number
        except AttributeError:
            registration = 'No registration number'

        return f"Owner: {owner_name}, Registration: {registration}"

    car_details.short_description = 'Short Details'