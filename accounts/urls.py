from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name="dashboard"),
     path('login/', views.login, name="login"),
     path('signup/', views.signup, name="signup"),
     path('manager/', views.manager, name="manager"),
     path('staff/', views.staff, name="staff"),
     path('utility/', views.utility, name="utility")
]