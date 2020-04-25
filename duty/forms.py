from django import forms
from .models import duty
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Row, Column
class  DutyForm ( forms . Form ):
    Duty_statu =[
        ("P","pasif"),
        ("A","aktif")
    ]
    title = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'placeholder':'Duty:'}))
    #content = forms.CharField(max_length=50, required=False, label="",widget=forms.Textarea(attrs={'placeholder':'Açıklama:', 'rows':2,}))
    statu = forms.ChoiceField(choices=Duty_statu,label="")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-lg-6'),
                Column('statu', css_class='form-group col-lg-6'),
                css_class='form-row mb-0'
            ),
           # Row(
            #    Column('content', css_class='form-group col-lg-12'),
             #   class_class = 'form-row'
            #),
            Submit('submit', 'Ekle', css_class='btn btn-danger btn-block')
        )