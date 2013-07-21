from django.conf.urls import patterns, url
from .views import MessageCreateAPIView


urlpatterns = patterns('contactform',
    url(r'$', MessageCreateAPIView.as_view(), name='contactform'),
)
