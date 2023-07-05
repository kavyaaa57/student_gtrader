from django import forms
from django.core.validators import RegexValidator
from django.forms.models import BaseModelForm
from .models import Course


class CourseAddForm(BaseModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateForm(forms.Form):
    course_id_1 = forms.CharField(
        max_length=10,
        validators=[RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')],
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        label="Course ID 1",
    )
    course_id_2 = forms.CharField(
        max_length=10,
        validators=[RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')],
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        label="Course ID 2",
    )
    course_id_3 = forms.CharField(
        max_length=10,
        validators=[RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')],
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        label="Course ID 3",
    )
    course_id_4 = forms.CharField(
        max_length=10,
        validators=[RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')],
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        label="Course ID 4",
    )
    course_id_5 = forms.CharField(
        max_length=10,
        validators=[RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')],
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        label="Course ID 5",
    )
    course_id_6 = forms.CharField(
        max_length=10,
        validators=[RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')],
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        label="Course ID 6",
    )
