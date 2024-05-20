from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *
from contact.models import Contact as ContactWithHealthService
from contact.forms import ContactForm

class IndexView(View):
    """
    Clase para renderizar la página de inicio
    """
    def get(self, request):
        return render(request, 'index.html', {})
    
class PageNotFoundView(View):
    """
    Clase para renderizar la página de error 404
    """
    def get(self, request):
        return render(request, '404.html', {})

class CreatePacientView(View):
    """
    Clase para crear un paciente
    """
    def get(self, request):
        pacient_form = PacientForm()
        contact_form = ContactForm()
        return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})

    def post(self, request):
        pacient_form = PacientForm(request.POST)
        contact_form = ContactForm(request.POST)
        if pacient_form.is_valid():
            pacient = pacient_form.save()
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.id_contact = pacient
                contact.save()
                return redirect('pacient')
        return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})

class EditPatientView(View):
    """
    Clase para editar un paciente
    """
    def get(self, request, id):
        try:
            pacient = Person.objects.get(id_history=id)
            contact = ContactWithHealthService.objects.get(id_contact=id)
        except (Person.DoesNotExist, ContactWithHealthService.DoesNotExist):
            return redirect('not_found')

        pacient_form = PacientForm(instance=pacient)
        contact_form = ContactForm(instance=contact)
        return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})

    def post(self, request, id):
        try:
            pacient = Person.objects.get(id_history=id)
            contact = ContactWithHealthService.objects.get(id_contact=id)
        except (Person.DoesNotExist, ContactWithHealthService.DoesNotExist):
            return redirect('not_found')

        pacient_form = PacientForm(request.POST, instance=pacient)
        contact_form = ContactForm(request.POST, instance=contact)
        if pacient_form.is_valid():
            pacient = pacient_form.save()
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.id_contact = pacient
                contact.save()
                return redirect('index')
        return render(request, 'pacient.html', {'pacient_form': pacient_form, 'contact_form': contact_form})