from rest_framework.generics import CreateAPIView

from .forms import ContactForm
from .models import Message


class MessageCreateAPIView(CreateAPIView):
    form_class = ContactForm
    model = Message
