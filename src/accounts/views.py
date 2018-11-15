# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import UserCreate

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username,password=password)
        login(request, user)
        messages.success(request , "Created {} successfully !! ".format(username))
        return redirect("restaurants:restaurants")
    else:
        form = UserCreationForm()
    return render(request, "create.html", {"form": form})

@permission_required("accounts.can_read")
def users(request):
    users = User.objects.all()
    context = {
    "users" : users,
    }
    return render(request , "users/users_list.html", context)


class UserDetailView(PermissionRequiredMixin, DetailView):
    template_name = "users/user_details.html"
    queryset = User.objects.all()
    permission_required = ("accounts.can_read")

class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = "create.html"
    success_url = "/accounts/users"
    permission_required = (
    ("accounts.can_read"),
    )

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs = super(UserUpdateView, self).get_context_data()
        kwargs["title"] = "Update {}".format(kwargs["user"])
        return kwargs

def change_password(request, pk ):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'create.html', {
        'form': form ,
        'title' : "change {} password".format(user)
    })


class UserChangePassword(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PasswordChangeForm
    template_name = "create.html"
    success_url = "/accounts/users"
    permission_required = (
    ("accounts.can_read"),
    )

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs = super(UserChangePassword, self).get_context_data()
        kwargs["title"] = "Change Password {}".format(kwargs["user"])
        return kwargs
