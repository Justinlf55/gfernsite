from django.urls import re_path
from . import views

urlpatterns = [
    re_path('home', views.main),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    re_path('logout', views.logout),
]