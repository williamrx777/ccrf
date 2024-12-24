from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('quemsomos/', views.quem_somos, name='quemsomos'),
    path('culto/', views.culto, name='culto'),
    path('contato/', views.contato, name='contato'),

]