from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.EstoqueEntradaList.as_view(), name='estoque_entrada_list'),
    path('<int:pk>/', views.EstoqueEntradaDetail.as_view(), name='estoque_entrada_detail'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),

    path('saida/', views.EstoqueSaidaList.as_view(), name='estoque_saida_list'),
    path('saida/<int:pk>/', views.EstoqueSaidaDetail.as_view(), name='estoque_saida_detail'),
    path('saida/add/', views.estoque_saida_add, name='estoque_saida_add'),
]
