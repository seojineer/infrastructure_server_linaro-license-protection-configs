# Settings for staging.releases.linaro.org.

from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/staging.releases.linaro.org/db/licenses.db',
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

SERVED_PATHS = ['/srv/staging.releases.linaro.org/www']
UPLOAD_PATH = '/srv/staging.releases.linaro.org/uploads'
