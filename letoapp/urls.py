from django.urls import path, include
from . import views

urlpatterns = [
    path('registrar/', views.registrar),
    path('login/loguear/', views.loguear),
    path('homepage/desloguear/', views.desloguear, name='logout'),
    path('login/', views.pagina_login, name='login'),
    path('', views.pagina_registro, name="registro"),
    path('homepage/', views.pagina_homepage, name="homepage"),
    path('homepage/micuenta/', views.pagina_micuenta, name='micuenta'),
]
