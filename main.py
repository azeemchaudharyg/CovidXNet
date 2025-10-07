from src.data_preprocessing import get_train_data, get_test_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_history

train_data = get_train_data('data/Train')
test_data = get_test_data('data/Test')

model, history = train_model(train_data, test_data, epochs=10)

# Save model
model.save("outputs/models/covid_model.h5")

plot_history(history)
evaluate_model(model, test_data)
