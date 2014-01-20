from django.conf.urls import patterns, url
from .views import contact_view


urlpatterns = patterns('contactform',
    url(r'$', contact_view, name='contactform'),
)
