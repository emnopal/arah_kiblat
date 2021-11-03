import time

from django.shortcuts import render
from .models import Parse
from django import forms


class ParseForm(forms.ModelForm):
    lokasi = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg",
               "placeholder": "Masukan lokasi atau masukan koordinat"}
    ))

    class Meta:
        model = Parse
        fields = ('lokasi',)


def home(request):
    template = 'index.html'
    context = {}

    context['form'] = ParseForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        used_form = ParseForm(request.POST)

        # If URL is valid
        if used_form.is_valid():
            time.sleep(2)
            obj = used_form.save()
            lokasi = obj.lokasi
            sudut = obj.sudut
            context['lokasi'] = lokasi
            context['sudut'] = sudut
            context['form'] = ParseForm()
            return render(request, template, context)

        # Else
        context['errors'] = used_form.errors

        return render(request, template, context)
