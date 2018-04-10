"""
WSGI config for lmn_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

#from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lmn_project.settings")

# https://stackoverflow.com/questions/27630155/appregistrynotready-the-translation-infrastructure-cannot-be-initialized
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
