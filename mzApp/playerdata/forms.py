from django import forms

class PlayerDataForm(forms.Form):
    data_input = forms.CharField(widget=forms.Textarea, label="Input Data")
