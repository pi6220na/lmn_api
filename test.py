import django
from django.core import management
from django.core.management.commands import loaddata



import os

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# needs environment variable for database password set:  LMN_DB_Pw=xxxx
#print(os.environ['LMN_DB_PW'])


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lmn_project.settings")
#settings.configure(default_settings=settings, DEBUG=True)
django.setup()


# need to load JSON files in this order for foreign key dependencies
# user artist venue show note
# set verbosity=0 (no displays) for production deployment
management.call_command(loaddata.Command(), 'user', verbosity=1)
management.call_command(loaddata.Command(), 'artist', verbosity=1)
management.call_command(loaddata.Command(), 'venue', verbosity=1)
management.call_command(loaddata.Command(), 'show', verbosity=1)
management.call_command(loaddata.Command(), 'note', verbosity=1)



