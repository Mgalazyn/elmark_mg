from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryRW.as_view()),
    path('category/<int:pk>/', views.CategoryRUD.as_view()),
    path('location/', views.LocationRW.as_view()),
    path('location/<int:pk>/', views.LocationRUD.as_view()),
    path('parts/', views.PartsRW.as_view()),
    path('parts/<str:pk>/', views.PartRUD.as_view()),
]
