from django.http.response import HttpResponseRedirect
from app.forms import PersonForm
from .models import Person
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PersonForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.template import RequestContext, context
#from django.views.generic import WelcomeView

# Create your views here.

class RegisterView(TemplateView):
    template_name = 'register.html'

class CreateModelView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "app/home.html"

def RegisterFormView(request):
    registerform = PersonForm()
    if request.method == 'POST':
        registerform = PersonForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return redirect(WelcomeView)
    context = {
        'registerform' : registerform
    }
    return render(request, 'register.html',context)

def WelcomeView(request):
    result = Person.objects.all()
    context = {
        'result' : result
    }
     
    return render(request,'home.html',context)



