
import sys
import os
import numpy as np
## Import layers, losses, optimizers, metrics, etc. All native keras losses and optimizers supported (see keras docs)
##   Custom losses, optimizers, and metrics can be written using keras backend
from keras import backend as K
from keras.layers import GlobalAveragePooling1D, GlobalAveragePooling2D, Dense, Dropout, Flatten
from keras.models import Model, Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam
from keras.losses import mean_absolute_error, mean_squared_error
from keras.applications.vgg16 import VGG16
from .lib.tools import Tools

def initialize_parameters(tools):
    '''
    Paths to save data, logs, etc.
    '''
    root_dir = os.path.dirname(os.path.abspath(__file__)) ## project root directory
    gt_columns = ['id', 'male'] ## id must be in first column, followed by output variable, then any additional inputs in csv
    image_paths = [root_dir + '/dataset/preprocessed_best/*.png'] 
    gt_paths = {root_dir + '/dataset/train.csv': ','} ## path to ground truth csvs (specify delimiters)
    pickled_path = root_dir + '/pickled_data/val_data.p' ## filename to save and load parsed data
    pretrained_tm = ''#root_dir + 'results/top_model_training/2017-12-11_20-03-14/top_model_weights.h5' ## Leave blank ('') when training top model
    trained_weights = ''#root_dir + '/results/retraining/Inception_M/retrained_model_weights.h5' ## Resume training
    train_test_image_ids_M = root_dir + '/image_id.csv' ## Replicate train_test split (male)
    train_test_image_ids_F = root_dir + '/image_id.csv' ## Replicate train_test split (female)
    
    paths = [root_dir, gt_columns, image_paths, gt_paths, pickled_path, pretrained_tm,
             trained_weights, train_test_image_ids_M, train_test_image_ids_F] ## Do not modify
    #print(paths)
    
    '''
    Define some model attributes. 
        base_model (string): A pretrained model to load weights and architecture from.
                                Values: InceptionV3, VGG16, VGG19, ResNet50, Xception, MobileNet
        image_size (tuple): Pixel dimensions to resize images to 
                                Values: Bear in mind necessary image dimensions for selected pre-trained model
        epochs (int): Number of epochs for training
        batch_size (int): Batch size for training
        gender (string): Filter data by gender
                                Values: '', 'M', 'F'
        top_model_loss (keras.losses): A keras loss function for top model
        retraining_loss (keras.losses): A keras loss function for retraining the full base model + top model
        top_model_optimizer (keras.optimizers): A keras optimizer for top model
        retraining_optimizer (keras.optimizers): A keras optimizer for retraining the full base model + top model
        train_test_split (tuple): Two or three values on [0,1] specifying the cutoff points for splitting the data.
                                    IMPORTANT: Values must sum to 1
                                    Examples: (0.5, 0.5), (0.85, 0.15), (0.5, 0.3, 0.2), (0.7, 0.15, 0.15)
        trainable_layers (list): A list of integers specifying layers to train. To determine this for a given base model,
                                    run with training scope property 'base_model_summary_only' set to true. This will just
                                    print out the model architecture, which can be used to determine trainable layers.
        metrics (list, optional): A list containing any of:
                                            -keras metrics or string specifying supported metric name (eg. mae, mse)
                                            -keras losses
                                            -custom metrics written with keras backend
    '''
    model_attributes = {'base_model' : 'VGG16',  
                        'image_size' : (256, 256),
                        'epochs' : 50,
                        'batch_size' : 16,
                        'gender' : '',#'F' or 'M',
                        'top_model_loss' : mean_absolute_error,
                        'retraining_loss' : mean_absolute_error,
                        'top_model_optimizer' : Adam(lr=0.001),
                        'retraining_optimizer' : RMSprop(lr=0.0001),
                        'train_test_split' : (0.7,0.15,0.15),
                        'trainable_layers' : list(range(19)),
                        'metrics' : ['mse', 'mae']
                        }

    '''
    Some settings to determine the scope of training. Setting some of these to false reduces redundancy with multiple training runs
        base_model_summary_only (boolean): When set to true, does not train at all. Only base model architecture is printed. This should be done
                                    when running for the first time to determine which layers to freeze
        data_from_scratch (boolean): When running for the first time, set to True to read the raw data. The data will then be pickled in the 
                                    specified directory. On subsequent runs, set to False to unpickle the saved data (much faster)
        generate_bottleneck_features (boolean): Whether to generate bottleneck features via the pre-trained model. If set to false, previously
                                    generated features are loaded from the specified directory
        train_top_model (boolean): When set to False, top model weights are loaded from specified path (required)
        tweak_cnn (boolean): When set to true, feature extraction cnn tweaked
    '''
    training_scope = {'base_model_summary_only' : False,
                      'data_from_scratch' : False,#True,
                      'generate_bottleneck_features' : True,
                      'train_top_model' : True,
                      'tweak_cnn' : True}
    
    
    
    preprocessing = ImageDataGenerator(featurewise_center=True,
                 samplewise_center=False,
                 featurewise_std_normalization=True,
                 samplewise_std_normalization=False,
                 zca_whitening=False,
                 zca_epsilon=1e-6,
                 rotation_range=20,
                 width_shift_range=0.2,
                 height_shift_range=0.2,
                 shear_range=0.,
                 zoom_range=0.2,
                 channel_shift_range=0.,
                 fill_mode='nearest',
                 cval=0.,
                 horizontal_flip=True,
                 vertical_flip=False,
                 rescale=None,
                 preprocessing_function=None,
                 data_format=None)
    
    
    tm = Sequential()
    tm.add(GlobalAveragePooling2D(input_shape=tools.features_shape(tools.instantiate_base_model(model_name=model_attributes['base_model'],
                                                                     input_dim=model_attributes['image_size']))))
    tm.add(Dense(1024, activation='linear'))
    tm.add(Dropout(0.5))
    tm.add(Dense(1024, activation='linear'))
    tm.add(Dropout(0.5))
    tm.add(Dense(128, activation='linear'))
    tm.add(Dense(1, activation='linear'))
    
#    tm = Sequential()
#    tm.add(Flatten(input_shape=features_shape(instantiate_base_model(model_name=model_attributes['base_model'],
#                                                                     input_dim=model_attributes['image_size']))))
#    tm.add(Dense(4096, activation='linear'))
#    tm.add(Dropout(0.5))
#    tm.add(Dense(4096, activation='linear'))
#    tm.add(Dropout(0.5))
#    tm.add(Dense(1000, activation='linear'))
#    tm.add(Dropout(0.5))
#    tm.add(Dense(1, activation='linear'))
    
    tm.compile(optimizer=model_attributes['top_model_optimizer'],
                  loss=model_attributes['top_model_loss'], metrics=model_attributes['metrics'])
    
    
    
    return(model_attributes, training_scope, paths, preprocessing, tm)

    
