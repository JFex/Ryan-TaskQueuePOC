from celery import Celery
import datetime
import report

def my_monitor(app):
    state = app.events.State()

    def announce_received_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print('TASK RECEIVED: %s[%s] %s Log info stored in DB.' % (
            task.name, task.uuid, task.info(),))
        report.insert_log(task.uuid, task.name, task.state, task, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def announce_failed_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s Log info stored in DB.' % (
            task.name, task.uuid, task.info(),))
        report.insert_log(task.uuid, task.name, task.state, task, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    def announce_succeeded_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print('TASK SUCCESS: %s[%s] %s Log info stored in DB.' % (
            task.name, task.uuid, task.info(),))
        report.insert_log(task.uuid, task.name, task.state, task, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def worker_online_handler(event):
        state.event(event)
        
        print('WORKER ONLINE: %s, %s, %s, %s' % (
            event['hostname'], event['timestamp'], event['freq'], event['sw_ver']))

    def worker_offline_handler(event):
        state.event(event)
        
        print('WORKER OFFLINE: %s, %s, %s, %s' % (
            event['hostname'], event['timestamp'], event['freq'], event['sw_ver']))

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-received': announce_received_tasks,
                'task-failed': announce_failed_tasks,
                'task-succeeded': announce_succeeded_tasks,
                'worker-online': worker_online_handler,
                'worker-offline': worker_offline_handler,

        })
        recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
    app = Celery(broker='rediss://:zhA9JaIKhLYtIRYiyhSewZ8StYRDc6+Yy2UHf9on1BQ=@ascend-dev-redis.redis.cache.windows.net:6380/0?ssl_cert_reqs=required',
                )
    my_monitor(app)