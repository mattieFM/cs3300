from django.db import models
from django.urls import reverse

# Create your models here.


class BaseModel(models.Model):
    """A base model to bwe inherited from. reassign absUrlDesc with the name of the model that should display in get absolute url"""
    absUrlDesc="baseModel"
    
    #Define default String to return the name for representing the Model object."
    def __str__(self):
        if(hasattr(self, 'name')):
            return self.name
        elif(hasattr(self, 'title')):
            return self.title
        else:
            return "base-model"


    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse(self.absUrlDesc, args=[str(self.id)])


class Student(BaseModel):
    #updating get_absulute_url override
    absUrlDesc="student-detail"
    #List of choices for major value in database, human readable name
    MAJOR = (
    ('CSCI-BS', 'BS in Computer Science'),
    ('CPEN-BS', 'BS in Computer Engineering'),
    ('BIGD-BI', 'BI in Game Design and Development'),
    ('BICS-BI', 'BI in Computer Science'),
    ('BISC-BI', 'BI in Computer Security'),
    ('CSCI-BA', 'BA in Computer Science'),
    ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )
    
    """the name of the student"""
    name = models.CharField(max_length=200)
    
    """the student's email"""
    email = models.CharField("UCCS Email", max_length=200)
    
    """the student's major. This is a categorical var"""
    major = models.CharField(max_length=200, choices=MAJOR, blank = True)
    
    studentPortfolio = models.OneToOneField("portfolio_app.Portfolio", on_delete=models.DO_NOTHING)
    
    

class Portfolio(BaseModel):
    #updating get_absulute_url override
    absUrlDesc="portfolio-detail"
    title = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    is_active = models.BooleanField()
    
    #using blank=true to ensure all fourms generated from this model will have this as optional
    about = models.TextField(blank=True)
    projects = models.ForeignKey('portfolio_app.Project', on_delete=models.DO_NOTHING, related_name='studentProjects')
    
    studentReference = models.OneToOneField("portfolio_app.Student", on_delete=models.CASCADE, null=True)
    
class Project(BaseModel):
    #updating get_absulute_url override
    absUrlDesc="project-detail"
    title= models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    studentReference = models.OneToOneField("portfolio_app.Student", on_delete=models.CASCADE, null=True)