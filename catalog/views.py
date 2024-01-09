from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'



def contacts_page(request):
    return render(request, 'catalog/contacts.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    formset_class = inlineformset_factory(Product, Version, form=VersionForm, extra=1, fields=('version_number', 'version_name', 'is_active'))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context_data['formset'] = self.formset_class(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = self.formset_class(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')