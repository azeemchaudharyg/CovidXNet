import matplotlib.pyplot as plt

def plot_history(history):
    h = history.history
    plt.plot(h['acc'], label='Accuracy')
    plt.plot(h['val_acc'], label='Validation Accuracy', color='red')
    plt.title("Accuracy vs Validation Accuracy")
    plt.legend()
    plt.show()
    
    plt.plot(h['loss'], label='Loss')
    plt.plot(h['val_loss'], label='Validation Loss', color='red')
    plt.title("Loss vs Validation Loss")
    plt.legend()
    plt.show()
