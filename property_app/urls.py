from django.urls import path

from property_app.views import property_list, property_detail

urlpatterns = [
    path('list/', property_list, name='property-list'),
    path('<int:pk>/', property_detail, name='property-detail'),
]
