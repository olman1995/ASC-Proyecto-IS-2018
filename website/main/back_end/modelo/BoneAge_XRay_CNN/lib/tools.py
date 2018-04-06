import os
import numpy as np
from keras.applications.vgg16 import VGG16


def features_shape(base_model):
    return((base_model.layers[len(base_model.layers)-1]).output_shape[1:])



def instantiate_base_model(model_name, input_dim, top=False):
    if model_name == 'InceptionV3':
        model = InceptionV3(include_top=top, weights='imagenet', input_shape=input_dim + (3,))
    elif model_name == 'VGG16':
        model = VGG16(include_top=top, weights='imagenet', input_shape=input_dim + (3,))
    elif model_name == 'VGG19':
        model = VGG19(include_top=top, weights='imagenet', input_shape=input_dim + (3,))
    elif model_name == 'ResNet50':
        model = ResNet50(include_top=top, weights='imagenet', input_shape=input_dim + (3,))
    elif model_name == 'Xception':
        model = Xception(include_top=top, weights='imagenet', input_shape=input_dim + (3,))
    elif model_name == 'MobileNet':
        model = MobileNet(include_top=top, weights='imagenet', input_shape=input_dim + (3,))
    else:
        raise ValueError('Model name is case-sensitive. Choose from: InceptionV3, '
                         'VGG16, VGG19, ResNet50, Xception, MobileNet')
    return(model)


def format_x(x, image_shape, gender=''):
    if not gender in ['', 'M', 'F']:
        raise ValueError('gender must be one of '', M, F')
    unscaled = np.array(np.array(list(x.values()))[:,0].tolist(), dtype='uint8').reshape(len(x), image_shape[0], image_shape[1]).astype('float16')
    ids = np.array(list(x.keys()))
    gen = np.array(list(x.values()))[:,1]

    for i in range(len(unscaled)):
        unscaled[i] = np.multiply(unscaled[i], 1/255)
    stacked = np.stack([unscaled, unscaled, unscaled], axis=3)

    if gender == 'M':
        stacked = stacked[gen == 1]
        ids = ids[gen == 1]
    elif gender == 'F':
        stacked = stacked[gen == 0]
        ids = ids[gen == 0]
    return(stacked, ids)

