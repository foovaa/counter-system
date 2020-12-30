from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('national-card/', views.nationalCard, name="national_card"),
    path('passport/', views.passport, name="passport"),
    path('car-license/', views.carLicense, name="car_license"),
    path('car-violation/', views.carViolation, name="car_violation"),
    path('check/', views.check, name="check"),
]