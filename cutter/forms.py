from django import forms
from django.forms import ModelForm

from .models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['author', 'url', 'short_url', ]
