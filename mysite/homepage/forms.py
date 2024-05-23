from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Andreas')
    email = forms.EmailField(label='andreas.blanck@ymail.com')