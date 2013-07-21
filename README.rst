Contact form plugin/app for django-cms

installation:

add to INSTALLED_APPS and to urlsconf with the contactform namespace

url(r'contactform', include('cmsplugin_contactform.urls', namespace='contactform')),