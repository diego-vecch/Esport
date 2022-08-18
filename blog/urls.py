from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="Blog"),
    path("categoria/<int:categoria_id>/", views.categoria, name="categoria"),
    path("entrada/<int:post_id>/", views.entrada, name="valordelnameentrada"),
    path("misEntradas/", views.misEntradas, name="misEntradas"),



]