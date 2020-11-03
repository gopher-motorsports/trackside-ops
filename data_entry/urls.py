from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/data_collection', views.collectData, name='data_collection'),
    path('/view_data', views.viewData, name='view_data'),
]