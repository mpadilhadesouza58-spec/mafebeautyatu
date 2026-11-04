from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Promocao(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='promocoes'
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco_promocional = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.titulo