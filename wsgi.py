import os
from django.core.wsgi import get_wsgi_application
os.enviroment.setdefault('DJANGO_SETTINGS_MODULE', 'linkr/settings')
applictaion = get_wsgi_application()
