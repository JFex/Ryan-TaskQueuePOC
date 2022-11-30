from celery import Celery
import report

app = Celery('celery_log')
default_config = 'celery_log_config'
app.config_from_object(default_config)

# log task result into mssql db
@app.task()
def insert_log(task_id,task_name,result,info,run_date):
    return report.insert_log(task_id,task_name,result,info,run_date)