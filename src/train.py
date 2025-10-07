from model import covid_model

def train_model(train_data, test_data, epochs=100, steps_per_epoch=8, validation_steps=2):
    model = covid_model()
    
    history = model.fit(
        train_data,
        steps_per_epoch=steps_per_epoch,
        epochs=epochs,
        validation_data=test_data,
        validation_steps=validation_steps
    )
    
    return model, history
