from django import forms

class RequestForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  request = forms.CharField(widget=forms.Textarea)
  