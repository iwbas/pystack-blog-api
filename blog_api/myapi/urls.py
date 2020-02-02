from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pages', views.PageViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'audios', views.AudioViewSet)
router.register(r'texts', views.TextViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]