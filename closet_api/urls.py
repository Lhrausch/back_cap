from django.urls import path
from . import views

urlpatterns = [
    path('api/closet', views.ClothingList.as_view(), name='closet_list'),
    path('api/closet/<int:pk>', views.ClothingDetail.as_view(), name='closet_detail'),
]
