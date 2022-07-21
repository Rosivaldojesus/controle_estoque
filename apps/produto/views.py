from django.shortcuts import render
from apps.produto.models import Produto

# Create your views here.

def produto_list(request):
    template_name ='produto/produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name ='produto/produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)



