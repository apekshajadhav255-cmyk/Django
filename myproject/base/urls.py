from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),#complete page
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('completeh/<int:id>',completeh,name='completeh'),#home page complete button
    path('deleteh/<int:id>',deleteh,name='deleteh'),
    path('complete_allh',complete_allh,name='complete_allh'),
    path('update/<int:id>',update,name='update'),
    path('restore_c/<int:id>',restore_c,name='restore_c'),
    path('restore_allc/',restore_allc,name='restore_allc')
]

#ASSIGNMENT
#DELETE ALL IN HOME PAGE
#DELETE , DELETE ALL IN COMPLETE PAGE - MOVE TO TrashModel
#DELETE, DELETE ALL IN TRASH PAGE - delete it from TrashModel