from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collectdata', views.collectData, name='collectdata'),
    path('view_data', views.viewData, name='view_data'),
    path('create_user', views.createUser, name='create_user'),
]