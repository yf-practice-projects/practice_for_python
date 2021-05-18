from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',os.environ.get('ALLOWED_HOSTS')]

LOGGING = {
	'version':1,
	'disable_existing_loggers':False,
	
	'loggers':{
		'django':{
			'handlers':['file'],
			'level':'INFO',
		},

		'which_one':{
			'handlers':['file'],
			'level':'INFO',
		}
	},

	'handlers':{
		'console':{
			'level':'INFO',
			'class':'logging.handlers.TimedRotatingFileHandler',
			'filename':os.path.join(BASE_DIR,'logs/django.log'),
			'formatter':'pro',
			'when':'D',
			'interval':1,
			'backupcount':7,
		}
	},

	'formatters':{
		'pro':{
			'format':'\t'.join([
				'%(asctime)s',
				'[%(levelname)s]',
				'%(pathname)s(Line:%(lineno)d)',
				'%(message)s'
			])
		}
	}
}