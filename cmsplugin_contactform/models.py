from django.conf import settings
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel


def validate_email_list(value):
    """Validates that value is a comma/space separated list of e-mail addresses"""
    for v1 in value.split(','):
        validate_email(v1.replace(' ' , ''))


class Group(models.Model):
    name = models.CharField(max_length=255)
    forward_to = models.CharField(max_length=255, validators=[validate_email_list], blank=True)

    def __unicode__(self):
        return self.name


class Message(TimeStampedModel):

    name = models.CharField(_('Name'), max_length=255)
    email = models.EmailField(_('E-mail'), max_length=75)
    subject = models.CharField(_('Subject') , max_length=255)
    message = models.TextField(_('Message'), max_length=255)
    group = models.ForeignKey(Group, null=True, blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.subject, self.name)

def send_mails(sender, created, instance, **kwargs):
    if created and instance.group and instance.group.forward_to:
        send_mail(instance.subject, instance.message, instance.email, instance.group.forward_to.split(','), fail_silently=True)
models.signals.post_save.connect(send_mails, sender=Message)

if 'cms' in settings.INSTALLED_APPS:
    from cms.models import CMSPlugin
    class ContactFormPlugin(CMSPlugin):
        group = models.ForeignKey(Group, null=True, blank=True)

        def __unicode__(self):
            return self.group.name
