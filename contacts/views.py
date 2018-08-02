from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import Contact
from forms import ContactForm

class ContactDetail(DetailView):
    model = Contact
    template_name = 'mycontacts/contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        return context

class ContactCreate(CreateView):
    model = Contact
    template_name = 'mycontacts/form.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContactCreate, self).form_valid(form)
