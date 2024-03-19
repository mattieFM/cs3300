from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import Student, Portfolio
from django.http import HttpResponseRedirect

# Create your views here.


#home page
def index(request):
    active_portfolios = Portfolio.objects.filter(is_active=True)
    # Render index.html
    return render( request, 'portfolio_app/index.html', {'active_portfolios':active_portfolios})

#student list page
def student_list(request):
    students = Student.objects.all()
    return render(request, 'portfolio_app/student_list.html', {'students': students})

#querried student list page
def search_students(request):
    query = request.GET.get('q')
    #name__icontains is case insenstitive containment test see: https://docs.djangoproject.com/en/2.1/ref/models/querysets/#icontains
    students = Student.objects.filter(name__icontains=query)
    return render(request, 'portfolio_app/student_list.html', {'students': students})

#page to display single portfolio
def portfolio_display(request, portfolio_id):
    # Retrieve the portfolio object using the provided ID
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    return render(request, 'portfolio_app/portfolio_details.html', {'portfolio': portfolio})


def generic_update(request, id, Model, Form, returnView, title="portfolio", studentPK=None):
    form = None
    model = None
    if(id==0):
        form = Form()
    else:
        model = Model.objects.get(pk=id)
        form = Form(instance=model)
       
    # Retrieve the portfolio object using the provided ID
    
    # create a form instance and populate it with data from the request:
    if request.method == "POST":
        form = Form(request.POST, instance=model)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            model = form.save()
            
            if(isinstance(studentPK, int)):
                try:
                    student=Student.objects.get(pk=studentPK)
                    student.studentPortfolio = model
                    student.save()
                except:
                    try:
                        port=Portfolio.objects.get(pk=studentPK)
                        port.projects.add(model)
                        port.save()
                    except:
                        pass
                
                
            returnid=str(model.pk)
            
            if(studentPK!=None):
                returnid=str(studentPK)
            
            return HttpResponseRedirect("/"+returnView+returnid+'/')
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'portfolio_app/genericFormUpdate.html', {"form": form, "title": title, "model":model})

def generic_delete(request, id, Model, backto=None, confirmed=False):
    # Retrieve the portfolio object using the provided ID
    model = Model.objects.get(pk=id)
    if request.method == "POST":
        model.delete()
        if(backto != None):
            return HttpResponseRedirect('/portfolio/'+str(backto)+"/")
        else:
            return render(request, 'portfolio_app/deleted.html')

#page to display single student
def student_display(request, student_id):
    # Retrieve the portfolio object using the provided ID
    student = Student.objects.get(pk=student_id)
    
    return render(request, 'portfolio_app/student_details.html', {'student': student})

    
def object_detail(request, id, Model, urlBase, title="genericObjDisplay"):
    obj = Model.objects.get(pk=id)  # Fetch the object using the primary key
    attributes = {}
    
    model_fields = obj._meta.fields
    for field in model_fields:
        val = getattr(obj, field.name)
        if("title" in field.name):
            title = val
        elif(val != None and (isinstance(val, (str, int)) and field.name !='id')):
            attributes[field.name] = val

    return render(request, 'portfolio_app/object_details.html', {'attributes': attributes, "title":title, "model":obj, 'urlBase':urlBase})
    