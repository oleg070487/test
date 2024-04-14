# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, '/home/o/ogmed/ogmed.beget.tech/taskmanager')
sys.path.insert(1, '/home/o/ogmed/ogmed.beget.tech/venv_django/lib/python3.12/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'taskmanager.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# import os, sys
# sys.path.insert(0, '/home/o/ogmed/ogmed.beget.tech/taskmanager')
# sys.path.insert(1, '/home/o/ogmed/.local/lib/python3.12/site-packages')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'taskmanager.settings'
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
