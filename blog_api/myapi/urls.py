from django.urls import include, path
from .views import PageList, PageDetail

app_name = 'pages'

urlpatterns = [
    path('pages/', PageList.as_view()),
    path('pages/<int:pk>', PageDetail.as_view()),
]