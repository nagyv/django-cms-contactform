from django.test import TestCase
from ..models import Message, Group
from ..forms import ContactForm


class ContactFormTest(TestCase):

    def test_no_group(self):
        form = ContactForm({
            'name': 'Me',
            'email': 'me@example.com',
            'subject': 'subject',
            'message': 'message'
            })
        import ipdb; ipdb.set_trace()
        self.assertTrue(form.is_valid())

    def test_with_group(self):
        group = Group.objects.create(name='gr')
        form = ContactForm({
            'name': 'Me',
            'email': 'me@example.com',
            'subject': 'subject',
            'message': 'message',
            'group': group.pk
            })
        self.assertTrue(form.is_valid())
        message = form.save()
        self.assertEqual(message.group, group)