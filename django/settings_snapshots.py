# Settings for snapshots.linaro.org.

from settings import *

DEBUG = False

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/snapshots.nexell.co.kr/db/licenses.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates_snapshots" ),
    os.path.join(PROJECT_ROOT, "templates" ),
    )

SERVED_PATHS = ['/srv/snapshots.nexell.co.kr/www']
UPLOAD_PATH = '/srv/snapshots.nexell.co.kr/uploads'
