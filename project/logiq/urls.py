from django.urls import path
from . import views

app_name = "logiq"
urlpatterns = [
    path('', views.index, name='index'),
    path('documento', views.documento, name='documento'),
    path('documentoCompleto', views.documentoCompleto, name='documentoCompleto'),
]
