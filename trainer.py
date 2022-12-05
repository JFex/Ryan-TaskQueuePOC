import time

# simulates training the model here
def run_training(model_data):
    print("Training model " + str(model_data["model_version"]) + " with batch size of " + 
        str(model_data["batch_size"]) + " and learning rate of " + str(model_data["learning_rate"]))
    time.sleep(10)
    return 'Model' + str(model_data["model_version"]) + 'trained successfully'
