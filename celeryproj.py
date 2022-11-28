from celery import Celery
import trainer
import report

app = Celery('celeryproj')
default_config = 'celeryconfig'
app.config_from_object(default_config)

# calls the learning function
@app.task()
def train_model(str):
    return trainer.run_training(str)

@app.task()
def insert_log(task_id,task_name,result,info,run_date):
    return report.insert_log(task_id,task_name,result,info,run_date)

