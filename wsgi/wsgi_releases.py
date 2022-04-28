"""
WSGI config for license_protected_downloads project.

This file configures WSGI for releases.test.co.kr
"""
import os
import sys
sys.path.append("/usr/lib/python2.7/dist-packages")
sys.path.append("/usr/lib/pymodules/python2.7")
sys.path.append("/usr/lib/python2.7")

sys.path.append("/srv/releases.test.co.kr")
sys.path.append("/srv/releases.test.co.kr/linaro-license-protection")
sys.path.append("/srv/releases.test.co.kr/configs/django")

os.environ["DJANGO_SETTINGS_MODULE"] = "settings_releases"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
