from django import forms
from .models import Produto, Promocao


class ProdutoForm(forms.ModelForm):
    categoria = forms.ChoiceField(
        choices=[
            ('', 'Selecione uma categoria'),
            ('Rosto', 'Rosto'),
            ('Olhos', 'Olhos'),
            ('Lábios', 'Lábios'),
        ],
        label='Categoria',
        widget=forms.Select(attrs={
            'class': 'campo-categoria'
        }),
        initial=''
    )

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria', 'estoque']


class PromocaoForm(forms.ModelForm):
    class Meta:
        model = Promocao
        fields = [
            'produto',
            'titulo',
            'descricao',
            'preco_promocional',
            'data_inicio',
            'data_fim',
        ]

        labels = {
            'produto': 'Produto',
            'titulo': 'Nome da promoção',
            'descricao': 'Descrição',
            'preco_promocional': 'Preço promocional (R$)',
            'data_inicio': 'Data de início',
            'data_fim': 'Data de término',
        }

        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }