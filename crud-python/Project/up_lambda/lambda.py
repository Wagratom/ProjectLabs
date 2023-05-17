import logging
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def handler(event, context):
	logging.info('Hands-on-cloud')
	return {
		"message": "Hello User!"
	}

