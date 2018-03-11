import datetime
from django.forms.widgets import SelectDateWidget
from django import forms
from suit.widgets import SuitSplitDateTimeWidget
from suit.widgets import HTML5Input

class CurrencyFilterForm(forms.Form):
    min_date = forms.DateTimeField(widget=SuitSplitDateTimeWidget, label="от", required=False)
    max_date = forms.DateTimeField(widget=SuitSplitDateTimeWidget, label="до", required=False)
