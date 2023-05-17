from django.contrib import admin
from .models import Location, Extra, Station, Network



class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'city', 
        'country', 
        'latitude', 
        'longitude', 
    )


class ExtraAdmin(admin.ModelAdmin):
    list_display = (
        'address', 
        'altitude', 
        'ebikes', 
        'has_ebikes', 
        'last_updated', 
        'normal_bikes', 
        'payment', 
        'payment_terminal', 
        'renting', 
        'returning', 
        'slots', 
        'uid', 
    )


class StationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'timestamp', 
        'latitude', 
        'longitude', 
        'free_bikes', 
        'empty_slots', 
    )



class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        'company', 
        'gbfs_href', 
        'href', 
        'name', 
        'id_network', 
    )

admin.site.register(Location, LocationAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Network, NetworkAdmin)
