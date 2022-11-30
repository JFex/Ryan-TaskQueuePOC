import celery_train
import time

# send a message to celery along with json data to be used for learning
ml_params = {"model_version": 1,"batch_size": 100, "learning_rate": 0.2}

for i in range(1,6):
    ml_params["model_version"] = i
    #time.sleep(5)
    task = celery_train.train_model.delay(ml_params)




