from django.urls import path
from productapp import views

urlpatterns = [
    path("",views.home, name = "home"),
    path('<int:id>/',views.detail),
]