from django.urls import path

from .views import IndexView , redirect_url

urlpatterns = [
    path('<str:slug>/', redirect_url, name='new_link'),
    path('', IndexView.as_view(), name='index'),
]
