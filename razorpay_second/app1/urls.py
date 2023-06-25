from django.urls import path,include
from .views import home, success

urlpatterns = [
    path('', home, name="home"),
    path('success', success, name="success"),
]