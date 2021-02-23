from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tests', views.TestViewSet)
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('collectdata', views.collectData, name='collectdata'),
    path('view_data', views.viewData, name='view_data'),
    path('create_user', views.createUser, name='create_user'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
