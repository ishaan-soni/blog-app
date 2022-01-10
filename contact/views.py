from django.shortcuts import render, reverse, HttpResponse
from .models import Contact
from .forms import ContactModelForm
from django.views import generic   
from django.core.mail import send_mail
import mimetypes

#TODO: send automated emails after form is filled to both

class ContactView(generic.CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactModelForm

    def get_success_url(self): #after form saved successfully 
        return reverse('home-page')

    def form_valid(self, form):
        # send_mail(
        #     subject="Contact Me form filled",
        # )
        return super(ContactView, self).form_valid(form)

    


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class ProjectView(generic.TemplateView):
    template_name = 'projects.html'


def download_resume(request):
    file_path = "static/RESUME_ISHAANSONI.pdf"
    file_name = "RESUME_ISHAANSONI.pdf"
    f1 = open(file_path, 'r')
    mime_type = mimetypes.guess_type(file_path)
    response = HttpResponse(f1, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response

