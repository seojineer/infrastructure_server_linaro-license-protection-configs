# Settings for releases.linaro.org.

from settings import *

DEBUG = False

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/releases.nexell.co.kr/db/licenses.db',
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

SERVED_PATHS = ['/srv/releases.nexell.co.kr/www']
UPLOAD_PATH = '/srv/releases.nexell.co.kr/uploads'
