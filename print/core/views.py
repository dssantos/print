from django.shortcuts import render
from print.core.forms import PrintForm
from print.core.forms import PrintForm

from django.forms import formset_factory


acoes = [
    {
        'nome': 'a1',
        'objeto': 'Software',
        'quantidade': 1,
        'valor': 10,
    },        
    {
        'nome': 'a2',
        'objeto': 'Hardware',
        'quantidade': 2,
        'valor': 20,
    },        
    {
        'nome': 'a3',
        'objeto': 'Software',
        'quantidade': 3,
        'valor': 30,
    },        
    {
        'nome': 'a4',
        'objeto': 'Software',
        'quantidade': 4,
        'valor': 40,
    }
]

def home(request):
    PrintFormSet = formset_factory(PrintForm, extra=len(acoes))
    if request.method == 'POST':
        formset = PrintFormSet(request.POST)
        context = {'formset': formset}
    
        if formset.is_valid():
            indicacoes = [form.cleaned_data['indicacao'] for form in formset]
            for index, acao in enumerate(acoes):
                acoes[index]['indicacao'] = indicacoes[index]
            context = {'acoes': acoes}
            return render(request, 'print.html', context)
            
    else:
        formset = PrintFormSet()
        for form, acao in zip(formset, acoes):
            acao['indicacao'] = form
    return render(request, 'index.html', {'acoes': acoes, 'formset': formset})
