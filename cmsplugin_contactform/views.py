from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Message


def contact_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			#send email
			return HTTPResponse(status_code=201, content_type='application/json')
		else:
			return HTTPResponse(content="Error", status_code=400, content_type='application/json')




