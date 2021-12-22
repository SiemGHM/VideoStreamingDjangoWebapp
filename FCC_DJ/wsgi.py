"""
WSGI config for FCC_DJ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from static_ranges import Ranges
from dj_static import Cling, MediaCling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FCC_DJ.settings")

application = Ranges(Cling(MediaCling(get_wsgi_application())))

# application = get_wsgi_application()
