from django.urls import path

from property_app.views import property_list

urlpatterns = [
    path('list/', property_list, name='property-list'),
]
