from django.urls import path
from . import views

app_name = "logiq"
urlpatterns = [
    path('', views.index, name='index'),
]
