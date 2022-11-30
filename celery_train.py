from celery import Celery
import trainer

app = Celery('celery_train')
default_config = 'celery_train_config'
app.config_from_object(default_config)

# calls a learning function
@app.task()
def train_model(str):
    return trainer.run_training(str)


