from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Drives', views.DrivesViewSet)
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path('', views.viewData, name='home'),
    path('collectdata', views.collectData, name='collectdata'),
    path('view_data', views.viewData, name='view_data'),
    path('filter_data', views.filter_data, name='filter_data'),
    path('create_user', views.createUser, name='create_user'),
	path('view_team', views.viewTeam, name="view_team"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
