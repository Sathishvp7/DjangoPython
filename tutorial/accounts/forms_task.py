from django import forms


class Homeform(forms.Form):
    post = forms.CharField()