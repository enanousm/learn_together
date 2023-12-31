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
    path('homepage/ramo/', views.ramo, name='ramo'),
    path('homepage/<correo>', views.email, name='email'),
    path('actualizar_horario/', views.pagina_horario, name='actualizar_horario'),
    path('actualizar_horario/actualizar/', views.actualizar, name='actualizar')
]
