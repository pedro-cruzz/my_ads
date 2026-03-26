from django.contrib import admin

# Register your models here.

from .models import Customer, City, Actor, Country

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

# Register your models here.
admin.site.register(Customer, CustomerAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'get_country')

    def get_country(self, obj):
        return obj.country.country

    get_country.short_description = 'Country'

# Register your models here.
admin.site.register(City, CityAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

# Register your models here.
admin.site.register(Actor, ActorAdmin)

