from django.http import HttpResponse
from django.views.generic.base import View

from .forms import ContactForm
from .models import Message


class ContactFormView(View):
	form_class = ContactForm

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			#send email
			return HttpResponse(status_code=201, content_type="application/json")
		return HttpResponse(content="error", status_code=400, content_type="application/json")

