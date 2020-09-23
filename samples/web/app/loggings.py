import os


def default_base():
    base = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base, 'logs')


def get_logfile(name):
    base = os.environ.get('DJ_LOGDIR', default_base())
    if not os.path.isdir(base):
        os.makedirs(base)
    return os.path.join(base, name)


def handler_file(name, level='DEBUG'):
    return {
        # 'level': level,
        'class': 'logging.FileHandler',
        'filename': get_logfile(name),
        'formatter': 'verbose',
    }



FORMATTERS = {
    'verbose': {
        'format': '\n{levelname} {asctime} {module} {process} {thread} \n{filename} {funcName} {lineno} {message}\n',
        'style': '{',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': FORMATTERS, 
    'root': {'level': 'DEBUG', 'handlers': ['file'], },
    'handlers': {
        'file': handler_file('app.log', level='DEBUG'),
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    # 'loggers': {
    #     'authx.client.middleware': {
    #         # 'level': 'INFO', 
    #         'level': 'DEBUG', 
    #         'handlers': ['file','console'],
    #     }
    #}
}

