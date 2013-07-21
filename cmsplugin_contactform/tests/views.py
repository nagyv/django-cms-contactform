from django.test import TestCase


class MessageCreateAPIViewTest(TestCase):

    def test_post_new(self):
        data = {
            'name': 'Me',
            'email': 'me@example.com',
            'subject': 'subject',
            'message': 'message'
            }
        resp = self.client.post('/', data)
        self.assertEqual(resp.status_code, 201)
