from .base import *


ENV_NAME = config('ENV_NAME')

if ENV_NAME == 'dev':
    from .dev import *
elif ENV_NAME == 'prod':
    from .prod import *
