from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.estoque_entrada_list, name='estoque_entrada_list'),

]
