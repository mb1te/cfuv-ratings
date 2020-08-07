import django_tables2 as tables
from .models import Abiturient


class AbiturientTable(tables.Table):
    class Meta:
        model = Abiturient
