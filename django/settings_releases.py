# Settings for releases.linaro.org.

from settings import *

DEBUG = False

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/releases.linaro.org/db/licenses.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates_releases" ),
    os.path.join(PROJECT_ROOT, "templates" ),
    )

SERVED_PATHS = ['/srv/releases.linaro.org/www']
UPLOAD_PATH = '/srv/releases.linaro.org/uploads'
