"""
WSGI config for segura2021 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/html/PS2021/segura2021')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "segura2021.settings")

application = get_wsgi_application()
