from django.urls import path

from portfolio_app import admin
from . import views
from .models import *
from .forms import *


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('students/', views.student_list, name='students'),
path('search_students/', views.search_students, name='search_students'),


path('student/<int:student_id>/', views.student_display, name='student'),

#yay generics :)
path('portfolio/<int:portfolio_id>/', views.portfolio_display, name='portfolio'),
path('portfolio_update/<int:id>/', views.generic_update, {'Model':Portfolio, 'Form': PortfolioForm, 'returnView': 'portfolio/'}, name='portfolio_update'),
path('portfolio_create/<int:id>/<int:studentPK>', views.generic_update, {'Model':Portfolio, 'Form': PortfolioForm, 'returnView': 'student/'}, name='portfolio_create'),
path('portfolio_delete/<int:id>/', views.generic_delete, {'Model':Portfolio}, name='portfolio_delete'),

path('project_display/<int:id>/', views.object_detail, {'Model':Project, "title": "Project Information", "urlBase":"project_update"}, name='ProjectDisplay'),
path('project_update/<int:id>/<int:studentPK>', views.generic_update, {'Model':Project, 'Form': ProjectForm, 'returnView': 'portfolio/', "title": "Project Information", }, name='project_update'),
path('project_update/<int:id>', views.generic_update, {'Model':Project, 'Form': ProjectForm, 'returnView': 'portfolio/', "title": "Project Information", }, name='project_update'),
path('project_delete/<int:id>/<int:backto>', views.generic_delete, {'Model':Project}, name='project_delete'),
path('project_create/<int:id>/<int:studentPK>', views.generic_update, {'Model':Project, 'Form': ProjectForm, 'returnView': 'portfolio/'}, name='project_create'),
]
