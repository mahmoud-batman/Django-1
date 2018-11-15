# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item
from .forms import ItemCreate
from restaurants.models import Restaurant
# Create your views here.
class ItemlistView(LoginRequiredMixin, ListView):
    def get_queryset(self, *args, **kwargs):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

class ItemDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self, *args, **kwargs):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemCreate
    template_name = 'create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        kwargs["restaurant"] = Restaurant.objects.filter(owner=self.request.user)
        return kwargs

    def get_queryset(self, *args, **kwargs):
        queryset = Item.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add Item"
        return context

class ItemUpdateView(LoginRequiredMixin, UpdateView):
        form_class = ItemCreate
        template_name = 'create.html'
        def get_queryset(self, *args, **kwargs):
            queryset = Item.objects.filter(user=self.request.user)
            return queryset

        def get_context_data(self, *args, **kwargs):
            context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
            context['title'] = "Update Item"
            return context

        def get_form_kwargs(self):
            kwargs = super(ItemUpdateView, self).get_form_kwargs()
            kwargs["user"] = self.request.user
            return kwargs
