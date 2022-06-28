from django.urls import include, path
from rest_framework.routers import DefaultRouter
from property_app.api.views import CommentDetail, CommentList, CompanyDetailsAPIView, CompanyListAPIView, CompanyViewSet, PropertyDetailsAPIView, PropertyListAPIView, CommentCreate

router = DefaultRouter()
router.register('company',CompanyViewSet, basename='company' )

urlpatterns = [
    path('property/', PropertyListAPIView.as_view(), name='property-list'),
    path('property/<int:pk>/', PropertyDetailsAPIView.as_view(), name='property-detail'),
    
    path('', include(router.urls)),
    
    # path('company/', CompanyListAPIView.as_view(), name='company-list'),
    # path('company/<int:pk>/', CompanyDetailsAPIView.as_view(), name='company-detail'),
  
    path('property/<int:pk>/comment-create/', CommentCreate.as_view(), name='comment-create'),
    path('property/<int:pk>/comment/', CommentList.as_view(), name='comment-list'),
    path('property/comment/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    
]
