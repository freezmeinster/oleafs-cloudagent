from __future__ import absolute_import

from celery import Celery

celery = Celery('cloudagent.celery' , 
		 broker="amqp://192.168.1.1", 
		 backend="amqp://192.168.1.1", 
		 include=['cloudagent.tasks'])

celery.conf.update(
	CELERY_TASK_RESULT_EXPIRES = 3600,
	#CELERYD_CONCURRENCY=1
)

if __name__ == "__main__" :
    celery.start()
