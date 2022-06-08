from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html');



def about(request):
    return render(request,'about.html');


def staff(requset):
    return render(requset,'staff.html');


def lib(request):
    return render(request,'Library.html');


def gallery(request):
    return render(request,'gallery.html');


def library(request):
    return render(request,'library.html');

def course(request):
    return render(request,'course.html');

def placementCell(request):
    return render(request,'placement call.html');


def facultylogin(request):
    return render(request,'facultylogin.html')


def studentlogin(request):
    return render(request,'studentlogin.html')



def contact(request):
    return render(request,'contact.html')

def result(request):
    return render(request,'result.html')    
    
def studentnav(request):
    return render(request,'studentnav.html')


def universityNominee(request):
    return render(request,'universityNominee.html')


def vision(request):
    return render(request,'vision.html')


def chairmanDesk(request):
    return render(request,'chairman desk.html');


def directorDesk(request):
    return render(request,'Director Desk.html');


def principal(request):
    return render(request,'principal desk.html');


def studentRegistration(request):
    return render(request,'studentRegistrationFrom.html');


def aicte(request):
    return render(request, 'aicte.html');


def computerLab(request):
    return render(request,'labs/computerLab.html');


def ELCSAndALCLab(request):
    return render(request,'labs/ELCSAndALCLab.html');

def EngineeringWorkshop(request):
    return render(request ,'labs/EngineeringWorkshop.html');

def BEELab(request):
    return render(request, 'labs/BEELab.html')


def ChemistryLab(request):
    return render(request,'labs/ChemistryLab.html')

def PhysicsLab(request):
    return render(request,'labs/PhysicsLab.html')

def ITWorkshop(request):
    return  render(request,'labs/ITWorkshop.html')



