from django.contrib import admin
from django.urls import path
from app.views import PersonView, RegisterView, RegisterFormView, WelcomeView
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RegisterView.as_view(),name="register"),
    path('home/',RegisterFormView, name="home"),
    path('welcome/',WelcomeView, name="welcome"),
    path('persons/',views.PersonView, name="persons"),
]