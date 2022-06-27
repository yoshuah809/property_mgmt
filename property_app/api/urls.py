from django.urls import path

from property_app.api.views import PropertyDetailsAPIView, PropertyListAPIView

urlpatterns = [
    path('list/', PropertyListAPIView.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetailsAPIView.as_view(), name='property-detail'),
]
