from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/update$', ItemUpdateView.as_view(),name="update"),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(),name="details"),
    url(r'^create$' , ItemCreateView.as_view(),name="create" ) ,
    url(r'^$' , ItemlistView.as_view(), name="list" ) ,
]
