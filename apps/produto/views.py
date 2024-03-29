from django.shortcuts import render
from apps.produto.models import Produto
from apps.produto.forms import ProdutoForm
from django.views.generic.edit import CreateView, UpdateView
from django.http import JsonResponse

# Create your views here.

def produto_list(request):
    template_name = 'produto/produto_list.html'
    objects = Produto.objects.all()

    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains=search)


    context = {'object_list': objects}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto/produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
    

def produto_add(request):
    template_name = 'produto/produto_form.html'
    return render(request, template_name)
    

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto/produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto/produto_form.html'
    form_class = ProdutoForm



def produto_json(request, pk):
    ''' Retorna o produto id e estoque'''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})

