from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('category/', views.CategoryRW.as_view()),
    path('category/<int:pk>/', views.CategoryRUD.as_view()),
    path('location/', views.LocationRW.as_view()),
    path('location/<int:pk>/', views.LocationRUD.as_view()),
    path('parts/', views.PartsRW.as_view()),
    path('parts/<str:pk>/', views.PartRUD.as_view()),

    # path('parts-filter/', views.PartsFilter.as_view()), #alternative endpoint for filters
    
    # #DOCS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # #Other way if we want have separated endpoints, much straight forward
    # path('parts/', views.PartsG.as_view()),
    # path('parts/create/', views.PartsCR.as_view()),
    # path('parts/update/<str:pk>/', views.PartsUD.as_view()),
    # path('location', views.LocationG.as_view()),
    # path('location/create/', views.LocationCR.as_view()),
    # path('location/update/<int:pk>/', views.LocationUD.as_view()),
    # path('category/', views.CategoryG.as_view()),
    # path('category/create/', views.CategoryCR.as_view()),
    # path('category/update/<int:pk>/', views.CategoryUD.as_view()),
]
