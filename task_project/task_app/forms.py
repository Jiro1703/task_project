from django.forms import ModelForm

from .models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = (
            'name',
            'barber_name',
            'record_date',
            'bshop',
        )

