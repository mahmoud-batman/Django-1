# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView

from .models import Restaurant
from .forms import RestaurantAddForm, RestaurantAddModelForm


# Create your views here.
'''
ListView function based view
'''
def restaurantsView(request):
    template_name = "restaurants/restaurants.html"
    queryset      = Restaurant.objects.all()
    context       = {
        "object_list" : queryset
    }
    return render(request , template_name , context)
'''
 ListView class based view
'''
class RestaurantsListView(LoginRequiredMixin, ListView):
    template_name = "restaurants/restaurants.html"
    # paginate_by = 100 # the number of items per page

    def get_queryset(self, *args, **kwargs):
        # slug = self.kwargs['slug'] # ==> slug = self.kwargs.get('slug')
        # if slug :
        #     queryset = Restaurant.objects.filter(
        #     Q(category__iexact = slug)
        #     | Q(category__icontains = slug)
        #     )
        # else :
        #     queryset = Restaurant.objects.all()
        queryset = Restaurant.objects.filter(owner = self.request.user)
        return queryset

'''
 DetailView class based view
'''
class RestaurantsDetailView(DetailView):
    template_name = "restaurants/restaurant_detail.html"
    queryset = Restaurant.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs.get('pk'))
        # print(self.kwargs)
        context = super(RestaurantsDetailView, self).get_context_data(*args, **kwargs) # DetailView.get_context_data(self)
        print(context)
        return context

'''
 CreateView function based view
'''
# @login_required(login_url='/login/')
@login_required() # by default to /accounts/login
def restaurantsCreate(request):
    template_name = "restaurants/create.html"
    form = RestaurantAddForm()
    errors = None
    if request.method == "POST":
        # form = RestaurantAddForm(request.POST)
        form = RestaurantAddModelForm(request.POST)
        """ we can replace previous three lines :
            form = RestaurantAddForm()
            if request.method == "POST":
                form = RestaurantAddForm(request.POST)
            with that line >> form = RestaurantAddForm(request.POST or None)
        """
        if form.is_valid():
            if request.user.is_authenticated():
                instance       = form.save(commit=False)
                instance.owner = request.user
                instance.save()
                return HttpResponseRedirect("/restaurants/")
            ## Standard forms.Form ( RestaurantAddForm )
            # obj = Restaurant.objects.create(
            #     name     = form.cleaned_data.get('name'),
            #     location = form.cleaned_data.get('location'),
            #     category = form.cleaned_data.get('category')
            # )
            else :
                return HttpResponseRedirect("/login/")

        if form.errors:
            print(form.errors)
            errors = form.errors
        ## OLD SCHOOL SAVING DATA (NOT SECURED )
        # restaurant = Restaurant()
        # restaurant.name = request.POST.get('name')
        # restaurant.location = request.POST.get('location')
        # restaurant.category = request.POST.get('category')
        # restaurant.save()
    context       = {
        "form" : form ,
        "errors" : errors
    }
    return render(request , template_name , context)

'''
 CreateView class based view
'''
class  RestaurantsCreateForm(LoginRequiredMixin , CreateView):
    form_class = RestaurantAddModelForm
    template_name = "create.html"
    # login_url = "/login/" # we added LOGIN_URL in the settings instead .
    # success_url = "/restaurants/" # we added get_absolute_url instead .
    def form_valid(self, form):
        instance        = form.save(commit=False)
        instance.owner  = self.request.user # request is built in the class
        return super(RestaurantsCreateForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantsCreateForm, self).get_context_data(*args, **kwargs)
        context['title'] = "Add Restaurant"
        return context

'''
 UpdateView class based view
'''
class RestaurantUpdateView(LoginRequiredMixin, UpdateView):#, PermissionRequiredMixin):
    form_class = RestaurantAddModelForm
    template_name = "create.html"

    # permission_required = 'restaurant.can_update'

    def get_queryset(self):
        queryset = Restaurant.objects.filter(owner = self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs = super(RestaurantUpdateView, self).get_context_data()
        kwargs["title"] = "Update Restaurant: {}".format(kwargs["restaurant"])
        return kwargs

'''
 TemplateView class based view
'''
class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        # context = context['view']
        print(context)
        return context


# ______________________________________________________________________________
# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         print(args)
#         print(kwargs['id'])
#         id = kwargs['id']
#         context = {
#         "id" : id ,
#             }
#         return render(request , 'restaurants/contact.html' , context)
# ______________________________________________________________________________
def home(request):
    text = "hello django"
    context = {
    "text" : text
    }
    return render(request , 'home.html' , context )
    # return HttpResponse("hello django ")
#
