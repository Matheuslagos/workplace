from django.urls import path
from . import views

app_name = "logiq"
urlpatterns = [
    path('', views.index, name='index'),
    path('documento', views.documento, name='documento'),
    path('documentoCompleto', views.documentoCompleto, name='documentoCompleto'),
    path('render_pdf_view', views.render_pdf_view, name='render_pdf_view'),
    path('render_pdf_view_onlydoc', views.render_pdf_view_onlydoc,
         name='render_pdf_view_onlydoc'),
]
