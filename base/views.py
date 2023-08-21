from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Phone

# Create your views here.

def design(request):
    return HttpResponse("Welcome to Design Selection ")


class PhoneSelection(CreateView):
    model=Phone
    fields = ['phone']
    template_name='base/phone.html'

    def get_success_url(self):
        return reverse_lazy('design_select')
    
