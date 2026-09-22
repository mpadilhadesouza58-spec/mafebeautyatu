from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Produto
from .forms import ProdutoForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 6

    def get_queryset(self):
        queryset = Produto.objects.all().order_by('nome')

        busca = self.request.GET.get('q')

        if busca:
            queryset = queryset.filter(nome__icontains=busca)

        return queryset


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/produto_detail.html'
    context_object_name = 'produto'


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_lista')


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_lista')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_lista')
