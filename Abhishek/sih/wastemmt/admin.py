from django.contrib import admin

# Register your models here.

from .models import images
admin.site.register(images)
#
# from .models import Rental
# admin.site.register(Rental)


from .models import logcredential
admin.site.register(logcredential)

# import json
# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields




# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#           'widget': map_widgets.GoogleMapsAddressWidget(attrs={
#               'data-autocomplete-options': json.dumps({
#                   'types': ['geocode', 'establishment'],
#                   'componentRestrictions': {
#                       'country': 'us'
#                   }
#               })
#           })
#         },
#     }