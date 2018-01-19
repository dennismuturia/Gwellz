from django import forms

class contactForms(forms.Form):
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'What does your mom call you?'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Where can we email you back'}))
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Things in your mind?'}))
