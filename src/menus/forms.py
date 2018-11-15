from django import forms
from .models import Item
from restaurants.models import Restaurant

class ItemCreate(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant' ,
            'name' ,
            'contents' ,
            'excludes' ,
            'public'
        ]

    def __init__(self, user=None, restaurant=None , *args, **kwargs):
        print(user)
        print(kwargs)
        super(ItemCreate, self).__init__(*args, **kwargs)
        self.fields["restaurant"].queryset = Restaurant.objects.filter(owner=user)
        # self.fields["restaurant"].queryset = restaurant
