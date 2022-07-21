from django.urls import path

from apps.produto.views import ProdutoCreate, produto_list, produto_detail, produto_add
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>', views.produto_detail, name='produto_detail'),
    path('add/', views.ProdutoCreate.as_view(), name='produto_add')

]
