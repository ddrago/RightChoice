import django_filters
from .models import *

class UniFilter(django_filters.FilterSet):
    class Meta:
        model = Course_Uni
        fields = "__all__"

