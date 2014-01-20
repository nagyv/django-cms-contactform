from django.conf.urls import patterns, url
from .views import ContactFormView


urlpatterns = patterns('contactform',
    url(r'$', ContactFormView.as_view(), name='contactform'),
)
