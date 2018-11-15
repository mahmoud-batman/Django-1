from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantsListView.as_view(),name="restaurants-list"),
    # url(r'^restaurants/create$' , restaurantsCreate, name="restaurant-create" ) ,
    url(r'^create$' ,  RestaurantsCreateForm.as_view(),name="create" ) ,
    url(r'^(?P<slug>[-\w]+)/update$', RestaurantUpdateView.as_view(),name="update"),
    url(r'^(?P<slug>[-\w]+)/$', RestaurantsDetailView.as_view(),name="details"),

    url(r'^$' , RestaurantsListView.as_view(), name="restaurants" ) ,

]
