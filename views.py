from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item

# Read - Fetch all items
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

class ItemCreateView(CreateView):
    model = Item
    template_name = 'crudapp/item_form.html'  # Correct path
    fields = ['name', 'description']
    success_url = reverse_lazy('item-list')


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'crudapp/item_form.html'  # ✅ Correct path
    fields = ['name', 'description']
    success_url = reverse_lazy('item-list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'crudapp/item_confirm_delete.html'  # ✅ Correct path
    success_url = reverse_lazy('item-list')
