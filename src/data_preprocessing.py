from keras.preprocessing import image

def get_train_data(directory, target_size=(256,256), batch_size=16):
    train_datagen = image.ImageDataGenerator(
        rescale=1/255,
        horizontal_flip=True,
        zoom_range=0.2,
        shear_range=0.2
    )
    train_data = train_datagen.flow_from_directory(
        directory=directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary'
    )
    return train_data

def get_test_data(directory, target_size=(256,256), batch_size=16):
    test_datagen = image.ImageDataGenerator(rescale=1/255)
    test_data = test_datagen.flow_from_directory(
        directory=directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary'
    )
    return test_data
