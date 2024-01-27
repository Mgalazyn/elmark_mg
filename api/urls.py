from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ApiOverview, name='home'),
    # path('create/', views.add_parts, name='add-part'),
    # path('all/', views.view_parts, name='view_parts'),
    path('parts/', views.PartsList.as_view()),
    path('parts/<str:pk>/', views.PartDetails.as_view()),
]
