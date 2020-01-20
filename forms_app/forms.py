from django import forms
from .models import *

class reg_forms(forms.ModelForm):
    class Meta():
        model=reg_tbl
        fields=['name','age']

class add_img_forms(forms.ModelForm):
    class Meta():
        model=add_image
        fields=['name','img']