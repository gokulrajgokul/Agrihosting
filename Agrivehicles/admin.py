from django.contrib import admin
from .models import Vehicle,Order,Contact,UserProfile,Booking,Rating, VehicleReview

admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(Rating)
admin.site.register(VehicleReview)