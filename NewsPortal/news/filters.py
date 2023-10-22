from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms

class PostFilter(FilterSet):
    date_create = DateFilter(field_name='date_create', widget=forms.DateInput(attrs={'type': 'date'}),
                             lookup_expr='date__gte')
class Meta:
    model = Post
    fields = {
        'author': ['iexact'],
        'title': ['icontains'],
        }