from django import forms
from models import Message
from django.utils.translation import ugettext as _


class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=255, required=True, error_messages={'required': 'Please enter your name!'})
    # email = forms.EmailField(required=True, error_messages={'required': 'Please enter your email address!', 'invalid': 'The provided email address is invalid!'})
    # subject = forms.CharField(max_length=255, required=False, error_messages={'required': 'Please enter a subject!'})
    # message = forms.CharField(widget=forms.Textarea, required=False, error_messages={'required': "You didn't provide a message!"})
    # contact_type = forms.CharField(max_length=20, required=True)
    # contact_type = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Message
        error_messages = {
            'name': {
                'required': _('Please enter your name!'),
            },
            'email': {
                'required': _('Please enter your email address!'), 
                'invalid': _('The provided email address is invalid!'),
            },
            'subject': {'required': _('Please enter a subject!')},
            'message': {'required': _("You didn't provide a message!")},
        }
        widgets = {
            'group': forms.HiddenInput
        }
        