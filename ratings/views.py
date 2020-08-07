from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Abiturient
from .forms import *


def index(request):
    return HttpResponseRedirect('bac')


def bac(request):
    if request.method == 'POST':
        form = AbiturientBachelorForm(request.POST)
        if form.is_valid():
            table = Abiturient.objects.all().filter(field=form.cleaned_data['field'],
                                                    form=form.cleaned_data['form'],
                                                    type="бакалавриат")
            outp = "по направлению подготовки " + form.cleaned_data['field'] + ", форма ообучения " + form.cleaned_data['form'] + "\n"
            return render(request, 'bac.html', {'need': True, 'table': table, 'print': outp, 'form': AbiturientBachelorForm})

    else:
        return render(request, 'bac.html', {'need': False, 'form': AbiturientBachelorForm, 'print': ''})


def spec(request):
    if request.method == 'POST':
        form = AbiturientSpecialtyForm(request.POST)
        if form.is_valid():
            table = Abiturient.objects.all().filter(field=form.cleaned_data['field'],
                                                    form=form.cleaned_data['form'],
                                                    type="специалитет")
            outp = "по направлению подготовки " + form.cleaned_data['field'] + ", форма ообучения " + form.cleaned_data['form'] + "\n"
            return render(request, 'spec.html', {'need': True, 'table': table, 'print': outp, 'form': AbiturientSpecialtyForm})

    else:
        return render(request, 'spec.html', {'need': False, 'form': AbiturientSpecialtyForm, 'print': ''})


def mag(request):
    if request.method == 'POST':
        form = AbiturientMagisterForm(request.POST)
        if form.is_valid():
            table = Abiturient.objects.all().filter(field=form.cleaned_data['field'],
                                                    form=form.cleaned_data['form'],
                                                    type="магистратура")
            outp = "по направлению подготовки " + form.cleaned_data['field'] + ", форма ообучения " + form.cleaned_data['form'] + "\n"
            return render(request, 'mag.html', {'need': True, 'table': table, 'print': outp, 'form': AbiturientMagisterForm})

    else:
        return render(request, 'mag.html', {'need': False, 'form': AbiturientMagisterForm, 'print': ''})


def asp(request):
    if request.method == 'POST':
        form = AbiturientGraduateForm(request.POST)
        if form.is_valid():
            table = Abiturient.objects.all().filter(field=form.cleaned_data['field'],
                                                    form=form.cleaned_data['form'],
                                                    type="аспирантура")
            outp = "по направлению подготовки " + form.cleaned_data['field'] + ", форма ообучения " + form.cleaned_data['form'] + "\n"
            return render(request, 'asp.html', {'need': True, 'table': table, 'print': outp, 'form': AbiturientGraduateForm})

    else:
        return render(request, 'asp.html', {'need': False, 'form': AbiturientGraduateForm, 'print': ''})


def ordinate(request):
    if request.method == 'POST':
        form = AbiturientOrdinateForm(request.POST)
        if form.is_valid():
            table = Abiturient.objects.all().filter(field=form.cleaned_data['field'],
                                                    form=form.cleaned_data['form'],
                                                    type="ординатура")
            outp = "по направлению подготовки " + form.cleaned_data['field'] + ", форма ообучения " + form.cleaned_data['form'] + "\n"
            return render(request, 'ord.html', {'need': True, 'table': table, 'print': outp, 'form': AbiturientOrdinateForm})

    else:
        return render(request, 'ord.html', {'need': False, 'form': AbiturientOrdinateForm, 'print': ''})


def search(request):
    if request.method == 'POST':
        form = AbiturientSearchForm(request.POST)
        if form.is_valid():
            table = Abiturient.objects.all().filter(fio=form.cleaned_data['field'])
            return render(request, 'search.html', {'need': True, 'table': table, 'form': AbiturientSearchForm})

    else:
        return render(request, 'search.html', {'need': False, 'form': AbiturientSearchForm})
