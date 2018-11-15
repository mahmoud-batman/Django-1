from django import forms
from .models import Restaurant
from .validators import validate_category

class RestaurantAddForm(forms.Form):
    name        = forms.CharField()
    location    = forms.CharField(required = False)
    category    = forms.CharField(required = False )

class RestaurantAddModelForm(forms.ModelForm):
    # email = forms.EmailField() # this field just for testing validation with clean_email func.
    category = forms.CharField(validators=[validate_category])
    class Meta:
        model = Restaurant
        fields = [
        'name' , 'location' , 'category'
         # , 'email'
        ]

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if ".edu" in email:
    #         raise forms.ValidationError("We Can't Accept EDU emails .")
    #     else :
    #         return email
