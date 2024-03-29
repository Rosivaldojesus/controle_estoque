from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from apps.core.models import TimeStampedModel
from apps.produto.models import Produto
from  .managers import EstoqueEntradaManager, EstoqueSaidaManager

# Create your models here.

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    nf = models.PositiveIntegerField('Nota Fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        if self.nf:
            return f'{self.pk} - {self.nf } - {self.created.strftime ("%d-%m-%Y") }'
        return f'{self.pk} -- {self.created.strftime ("%d-%m-%Y")}'

    def get_absolute_url(self):

        return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return f'---'





class EstoqueEntrada(Estoque):

    objects = EstoqueEntradaManager()

    class Meta:
        proxy=True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'

    def get_absolute_url(self):    
        return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})



class EstoqueSaida(Estoque):

    objects = EstoqueSaidaManager()
    
    class Meta:
        proxy=True
        verbose_name = 'estoque saida'
        verbose_name_plural = 'estoque saida'

    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_saida_detail', kwargs={'pk': self.pk})


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.pk} - {self.estoque} - {self.produto}'

