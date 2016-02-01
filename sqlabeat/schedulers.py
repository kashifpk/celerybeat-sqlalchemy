from celery import schedules, current_app
from celery.beat import Scheduler, ScheduleEntry
from celery.utils.log import get_logger

# This scheduler must wake up more frequently than the
# regular of 5 minutes because it needs to take external
# changes to the schedule into account.
DEFAULT_MAX_INTERVAL = 5  # seconds

log = get_logger(__name__)


class SQLAlchemyScheduler(Scheduler):
    """
    Celery beat scheduler class that uses SQLAlchemy to store schedules in relational databases
    """

    def __init__(self, *args, **kwargs):
        self._dirty = set()
        Scheduler.__init__(self, *args, **kwargs)
        self.max_interval = (
            kwargs.get('max_interval') or
            self.app.conf.CELERYBEAT_MAX_LOOP_INTERVAL or
            DEFAULT_MAX_INTERVAL)

    @property
    def schedule(self):
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
        return {}
