# Settings for staging.snapshots.linaro.org.

from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/staging.snapshots.linaro.org/db/licenses.db',
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

SERVED_PATHS = ['/srv/staging.snapshots.linaro.org/www']
UPLOAD_PATH = '/srv/staging.snapshots.linaro.org/uploads'
