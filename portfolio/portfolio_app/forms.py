from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "major"]


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title", "contact_email", "about", "is_active"]
        
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]