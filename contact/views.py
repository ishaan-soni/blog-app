from django.shortcuts import render, reverse
from .models import Contact
from .forms import ContactModelForm
from django.views import generic   

#TODO: send automated emails after form is filled to both

class ContactView(generic.CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactModelForm

    def get_success_url(self): #after form saved successfully 
        return reverse('home-page')

    def form_valid(self, form):
        return super(ContactView, self).form_valid(form)

    


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class ProjectView(generic.TemplateView):
    template_name = 'projects.html'
