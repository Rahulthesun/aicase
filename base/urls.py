from django.urls import path
from .views import PhoneSelection
from . import views

urlpatterns=[
    path('model_select/', PhoneSelection.as_view() , name='phoneselection'),
    path('design_select/',views.design , name='design_select')
]