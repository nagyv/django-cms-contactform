from django.core import mail
from django.test import TestCase 
from ..models import Message, Group


class MessageTest(TestCase):
    
    def test_new_message_forwarded(self):
        group = Group.objects.create(name='test', forward_to='me@example.com, you@example.com')
        message = Message.objects.create(name='sender', email='sender@example.com', message='my message', group=group)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(len(mail.outbox[0].to), 2)

    def test_validate_forward_to(self):
        Group.objects.create(name='test', forward_to='me@example.com, you_example.com')
        self.assertRaises(ValueError, Group.objects.create, name='test', forward_to='me@example.com, you_invalid_example.com')
