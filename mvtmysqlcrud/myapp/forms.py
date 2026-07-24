from django import forms
from myapp.models import Product

class ProductForm(forms.ModelForm):
      ProId = forms.IntegerField()
      ProName = forms.CharField(max_length=40)
      ProImg = forms.CharField(max_length=100)
      ProPrice = forms.IntegerField()
      class Meta:
            model = Product
            fields ='__all__'