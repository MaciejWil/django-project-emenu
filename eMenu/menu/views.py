from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'

class MenuListView(ListView):
    context_object_name = 'menus'
    model = models.Menu


class MenuDetailView(DetailView):
    context_object_name = 'menu_detail'
    model = models.Menu
    template_name = 'menu/menu_detail.html'


class MenuCreateView(CreateView):
    fields = ('name','description','added_date')
    model = models.Menu
