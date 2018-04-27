import sys
import os
import numpy as np
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
    # project root directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    # id must be in first column, followed by output variable, then any additional inputs in csv
    gt_columns = ['id', 'male']
    image_paths = [root_dir + '/dataset/preprocessed_best/*.png']
    # path to ground truth csvs (specify delimiters)
    gt_paths = {root_dir + '/dataset/train.csv': ','}
    # filename to save and load parsed data
    pickled_path = root_dir + '/pickled_data/val_data.p'
    # root_dir + 'results/top_model_training/2017-12-11_20-03-14/top_model_weights.h5' ## Leave blank ('') when training top model
    pretrained_tm = ''
    # root_dir + '/results/retraining/Inception_M/retrained_model_weights.h5' ## Resume training
    trained_weights = ''
    # Replicate train_test split (male)
    train_test_image_ids_M = root_dir + '/image_id.csv'
    # Replicate train_test split (female)
    train_test_image_ids_F = root_dir + '/image_id.csv'
    paths = [root_dir, gt_columns, image_paths, gt_paths, pickled_path, pretrained_tm,
             trained_weights, train_test_image_ids_M, train_test_image_ids_F]
    model_attributes = {'base_model': 'VGG16',
                        'image_size': (256, 256),
                        'epochs': 50,
                        'batch_size': 16,
                        # 'F' or 'M'
                        'gender': '',
                        'top_model_loss': mean_absolute_error,
                        'retraining_loss': mean_absolute_error,
                        'top_model_optimizer': Adam(lr=0.001),
                        'retraining_optimizer': RMSprop(lr=0.0001),
                        'train_test_split': (0.7, 0.15, 0.15),
                        'trainable_layers': list(range(19)),
                        'metrics': ['mse', 'mae']
                        }
    training_scope = {'base_model_summary_only': False,
                      'data_from_scratch': False,
                      'generate_bottleneck_features': True,
                      'train_top_model': True,
                      'tweak_cnn': True}
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
    tm.compile(optimizer=model_attributes['top_model_optimizer'],
               loss=model_attributes['top_model_loss'], metrics=model_attributes['metrics'])
    return(model_attributes, training_scope, paths, preprocessing, tm)
