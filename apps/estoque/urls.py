from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.estoque_entrada_list, name='estoque_entrada_list'),
    path('<int:pk>/', views.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),

    path('saida/', views.estoque_saida_list, name='estoque_saida_list'),
    path('saida/<int:pk>/', views.estoque_saida_detail, name='estoque_saida_detail'),


]
