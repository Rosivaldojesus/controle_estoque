from django.urls import path

from apps.produto.views import produto_list, produto_detail

app_name = 'produto'

urlpatterns = [
    path('', produto_list, name='produto_list'),
    path('<int:pk>', produto_detail, name='produto_detail'),

]
