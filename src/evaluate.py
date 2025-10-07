import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

def evaluate_model(model, test_data):
    predictions = model.predict(test_data, steps=len(test_data))
    predicted_classes = np.round(predictions).astype(int).flatten()
    true_classes = test_data.classes[:len(predicted_classes)]
    print("Confusion Matrix:")
    print(confusion_matrix(true_classes, predicted_classes))
    print("Classification Report:")
    print(classification_report(true_classes, predicted_classes))
    
    return predicted_classes
