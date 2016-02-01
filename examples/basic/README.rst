To run a task worker:

    celery -A basic worker --loglevel=info

Manually running tasks from a python prompt:

    import basic
    basic.task1.delay()
    basic.say_hello.delay(name='kashif')

