from django import forms
from django.contrib.auth.models import User


class UserCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        'username',
        'password',
        'is_active' ,
        'is_staff',
        # 'permission',
        'is_superuser'
        ]
