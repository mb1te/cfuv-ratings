from django import forms
from .models import Abiturient, FieldOfStudy


class AbiturientBachelorForm(forms.Form):
    names = [i.name for i in FieldOfStudy.objects.filter(type="бакалавриат")]
    names.sort()
    field = forms.ChoiceField(label="Направление подготовки", choices=[(i, i) for i in names])
    frms = ["очная бюджетная", "очная целевая", "очная платная", "заочная бюджетная", "заочная платная"]
    form = forms.ChoiceField(label="форма обучения", choices=[(i, i) for i in frms])


class AbiturientSpecialtyForm(forms.Form):
    names = [i.name for i in FieldOfStudy.objects.filter(type="специалитет")]
    names.sort()
    field = forms.ChoiceField(label="Направление подготовки", choices=[(i, i) for i in names])
    frms = ["очная бюджетная", "очная целевая", "очная платная", "заочная бюджетная", "заочная платная"]
    form = forms.ChoiceField(label="форма обучения", choices=[(i, i) for i in frms])


class AbiturientMagisterForm(forms.Form):
    names = [i.name for i in FieldOfStudy.objects.filter(type="магистратура")]
    names.sort()
    field = forms.ChoiceField(label="Направление подготовки", choices=[(i, i) for i in names])
    frms = ["очная бюджетная", "очная целевая", "очная платная", "заочная бюджетная", "заочная платная"]
    form = forms.ChoiceField(label="форма обучения", choices=[(i, i) for i in frms])


class AbiturientGraduateForm(forms.Form):
    names = [i.name for i in FieldOfStudy.objects.filter(type="аспирантура")]
    names.sort()
    field = forms.ChoiceField(label="Направление подготовки", choices=[(i, i) for i in names])
    frms = ["очная бюджетная", "очная целевая", "очная платная", "заочная бюджетная", "заочная платная"]
    form = forms.ChoiceField(label="форма обучения", choices=[(i, i) for i in frms])


class AbiturientOrdinateForm(forms.Form):
    names = [i.name for i in FieldOfStudy.objects.filter(type="ординатура")]
    names.sort()
    field = forms.ChoiceField(label="Направление подготовки", choices=[(i, i) for i in names])
    frms = ["очная бюджетная", "очная целевая", "очная платная", "заочная бюджетная", "заочная платная"]
    form = forms.ChoiceField(label="форма обучения", choices=[(i, i) for i in frms])


class AbiturientSearchForm(forms.Form):
    field = forms.CharField(label="ФИО", max_length=255)

