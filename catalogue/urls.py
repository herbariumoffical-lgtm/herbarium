from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('herbarium/<str:barcode>/', views.detail, name='detail'),
    path('api/search/', views.search_api, name='search_api'),
]
