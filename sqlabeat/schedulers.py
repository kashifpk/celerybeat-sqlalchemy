from celery import schedules, current_app
from celery.beat import Scheduler, ScheduleEntry
from celery.utils.log import get_logger
from celery.schedules import crontab


# This scheduler must wake up more frequently than the
# regular of 5 minutes because it needs to take external
# changes to the schedule into account.
DEFAULT_MAX_INTERVAL = 5  # seconds

log = get_logger(__name__)


class SQLAlchemyScheduler(Scheduler):
    """
    Celery beat scheduler class that uses SQLAlchemy to store schedules in relational databases
    """

    _schedule = {}

    def __init__(self, *args, **kwargs):

        log.info("SQLAlchemyScheduler.__init__ called")

        self._dirty = set()
        Scheduler.__init__(self, *args, **kwargs)
        self.max_interval = (
            kwargs.get('max_interval') or
            self.app.conf.CELERYBEAT_MAX_LOOP_INTERVAL or
            DEFAULT_MAX_INTERVAL)

    def setup_schedule(self):
        "Called when schedule is intialized. Fetch schedules from DB etc here"

        log.info("SQLAlchemyScheduler.setup_schedule called")

        if 'celery.backend_cleanup' not in self._schedule:
            self._schedule['celery.backend_cleanup'] = ScheduleEntry(
                name='celery.backend_cleanup',
                task='celery.backend_cleanup',
                schedule=crontab('0', '4', '*'),
                options= {'expires': 12 * 3600}
            )

        #self.update_from_dict(entries)

    def sync(self):
        "Called when schedule needs to be save to the DB etc"
        log.info("SQLAlchemyScheduler.sync called")

    def get_schedule(self):
        # update = False
        # if not self._initial_read:
        #     debug('DatabaseScheduler: intial read')
        #     update = True
        #     self._initial_read = True
        # elif self.schedule_changed():
        #     info('DatabaseScheduler: Schedule changed.')
        #     update = True
        # 
        # if update:
        #     self.sync()
        #     self._schedule = self.all_as_schedule()
        # 
        # return self._schedule
        log.info("SQLAlchemyScheduler.get_schedule called")
        log.info(self._schedule)
        return self._schedule

    def set_schedule(self, schedule):
        log.info("SQLAlchemyScheduler.get_schedule called with data {}".format(schedule))
        self._schedule = schedule
    schedule = property(get_schedule, set_schedule)
