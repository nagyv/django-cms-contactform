from django.template import Context
from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from forms import ContactForm
from models import ContactFormPlugin

class ContactFormPlugin(CMSPluginBase):
    model = ContactFormPlugin
    name = _('Contact Form')
    render_template = 'cmsplugin_contactform/contactform.html'

    def render(self, context, instance, placeholder):
        contactForm = ContactForm(initial={'group': instance.group})
        return Context({
            'csrf_token': context['csrf_token'],
            'form': contactForm
            })
plugin_pool.register_plugin(ContactFormPlugin)
