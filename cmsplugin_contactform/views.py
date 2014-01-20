import json
from django.http import HttpResponse
from django.views.generic.base import View

from .forms import ContactForm
from .models import Message


class ContactFormView(View):
	form_class = ContactForm

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			#save message
			data = form.cleaned_data
			message = Message.objects.create(name=data['name'],
				subject=data['subject'],
				email=data['email'],
				message=data['message']
				 )
			#send email
			return HttpResponse(status=201, content_type="application/json")
		# import ipdb;ipdb.set_trace()
		return HttpResponse(content=json.dumps(form.errors), status=400, content_type="application/json")

