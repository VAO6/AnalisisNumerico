import os
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/analisis')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/analisis/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analisis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()