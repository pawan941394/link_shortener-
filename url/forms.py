from django import forms
class Url(forms.Form):
    url = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Enter URL here','id':'input' }))
