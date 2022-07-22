from django.forms import inlineformset_factory
from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect

from apps import produto
from apps.produto.models import Produto

from .forms import EstoqueForm, EstoqueItensForm
from .models import Estoque, EstoqueItens

# Create your views here.

def estoque_entrada_list(request):
    template_name = 'estoque/estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = { 'object_list': objects }
    return render(request, template_name, context)


def estoque_entrada_detail(request, pk):
    template_name = 'estoque/estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk=pk)
    context = { 'object': obj }
    return render(request, template_name, context)


def dar_baixa_estoque(form):
    # Pega os produtos a partir da instância do formulário (Estoque)
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
    print('Estoque atualizado com sucesso.')





def estoque_entrada_add(request):
    template_name = 'estoque/estoque_entrada_form.html'

    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            dar_baixa_estoque(form)
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

    context = {
        'forms': form,
        'formset': formset,
    }

    return render(request, template_name, context)


