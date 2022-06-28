from django.urls import path

from property_app.api.views import CompanyDetailsAPIView, CompanyListAPIView, PropertyDetailsAPIView, PropertyListAPIView

urlpatterns = [
    path('', PropertyListAPIView.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetailsAPIView.as_view(), name='property-detail'),
    
    path('company/', CompanyListAPIView.as_view(), name='company-list'),
    path('company/<int:pk>/', CompanyDetailsAPIView.as_view(), name='company-list'),
    
]
