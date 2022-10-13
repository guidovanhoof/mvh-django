from django.urls import path
from . import views

urlpatterns = [
    path('', views.kalenders, name="kalenders"),
    path('<jaar>', views.kalender, name="kalender"),
]
