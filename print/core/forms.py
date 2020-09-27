from django import forms

class PrintForm(forms.Form):
    options = (('Não','Não'), ('Sim','Sim'))
    indicacao = forms.ChoiceField(choices=options)
