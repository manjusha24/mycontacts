from django.conf.urls import url
from django.views.generic import ListView
from models import Contact
from views import ContactCreate

urlpatterns = [
    # List of all contacts: /contacts/
    url(r'^$',
        ListView.as_view(
            queryset=Contact.objects.filter().order_by('name')[:],
            context_object_name='latest_contacts_list',
            template_name='mycontacts/contacts_list.html'),
        name='contacts_list'),

    # Create a contact, /contacts/create/
    url(r'^create/$',
        ContactCreate.as_view(),
        name='contact_create'),
]
