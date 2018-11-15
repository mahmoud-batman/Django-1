from django.conf.urls import url, include
from accounts.views import *

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    url(r'^signup/$', register,name="register"),
    url(r'^users/$', users ,name="users"),
    url(r'^users/(?P<pk>\d+)/$', UserDetailView.as_view(),name="details"),
    url(r'^users/(?P<pk>\d+)/update/$', UserUpdateView.as_view(),name="update"),
    # url(r'^users/(?P<pk>\d+)/password/$', UserChangePassword.as_view() ,name="change-password"),
    url(r'^users/(?P<pk>\d+)/password/$', change_password ,name="change-password"),

]
