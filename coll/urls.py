from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

from coll import views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from college import settings


urlpatterns = [

    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('library/', views.library, name='library'),
     path('course/', views.course, name='course'),
    path('staff/', views.staff, name='staff'),
    path('placementCell/', views.placementCell, name='placementCell'),
    path('facultylogin/', views.facultylogin, name='facultylogin'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('contact/', views.contact, name='contact'),
    path('universityNominee/',views.universityNominee,name='universityNominee'),
    path('vision/', views.vision, name='vision'),
    path('chairmanDesk/', views.chairmanDesk,name='chairmanDesk'),
    path('directordesk/',views.directorDesk,name='directorDesk'),
    path('principal/',views.principal,name='principal'),
    path('aicte/',views.aicte,name='aicte'),
    path('studentRegistration',views.studentRegistration,name='studentRegistration'),
    path('studentnav',views.studentnav,name='studentnav'),
     path('result',views.result,name='result'),
    #labs urls
    path('computerLab', views.computerLab, name='computerLab'),
    path('ELCSAndALCLab', views.ELCSAndALCLab, name='ELCSAndALCLab'),
    path('EngineeringWorkshop', views.EngineeringWorkshop, name='EngineeringWorkshop'),
    path('BEELab',views.BEELab,name='BEELab'),
    path('ChemistryLab',views.ChemistryLab,name='ChemistryLab'),
    path('PhysicsLab',views.PhysicsLab, name='PhysicsLab'),
    path('ITWorkshop',views.ITWorkshop, name='ITWorkshop'),



]

