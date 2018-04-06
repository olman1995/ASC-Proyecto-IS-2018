# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:05:23 2017

@author: MedImaging7271
"""

import numpy as np
import os
import datetime
import csv
import operator
from keras import backend as K
from keras.layers import GlobalAveragePooling1D, GlobalAveragePooling2D, Dense, Dropout, Flatten
from keras.models import Model, Sequential
from keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam
from keras.losses import mean_absolute_error, mean_squared_error
from lib.parse_images import read_images, train_test_ids, unpickle
from lib.tools import  format_x, instantiate_base_model, features_shape 
from parameters import initialize_parameters

model_attributes, training_scope, paths, datagen, tm = initialize_parameters()


def make_predictions(attributes, paths, tm, subset=['train', 'val', 'test']):
    os.chdir(paths[0])
    
    model_attributes = attributes
    gt_columns = paths[1]
    image_paths = paths[2]
    gt_paths = paths[3]
    pickle_path = paths[4]
    pretrained_tm_path = paths[5]
    weights = paths[6]
    ids_male = paths[7]
    ids_female = paths[8]
    
    if attributes['gender'] == 'M':
        train_test_labels = ids_male
    elif attributes['gender'] == 'F':
        train_test_labels = ids_female
    
    bone_age_data = unpickle(pickle_path)
    all_x = {**bone_age_data[0], **bone_age_data[2], **bone_age_data[4]}
    all_y = {**bone_age_data[1], **bone_age_data[3], **bone_age_data[5]}
    all_ids = list(all_x.keys())
    id_train = train_test_ids(train_test_labels)[0]
    id_val = train_test_ids(train_test_labels)[1]
    id_test = []
    for i in all_ids:
        if not i in id_train:
            if not i in id_val:
                if model_attributes['gender'] == 'M':
                    if all_x[i][1] == 1:
                        id_test.append(i)
                elif model_attributes['gender'] == 'F':
                    if all_x[i][1] == 0:
                        id_test.append(i)
    
    x_train_full = {key : all_x[key] for key in id_train}
    y_train_full = {key : all_y[key] for key in id_train}
    x_val_full = {key : all_x[key] for key in id_val}
    y_val_full = {key : all_y[key] for key in id_val}
    x_test_full = {key : all_x[key] for key in id_test}
    y_test_full = {key : all_y[key] for key in id_test}
    del bone_age_data
    ## Format data
    if model_attributes['gender'] == '':
        x_train, id_train = format_x(x=x_train_full, image_shape=model_attributes['image_size'])
        y_train = np.array(list(y_train_full.values()),  dtype='float')
        x_val, id_val = format_x(x=x_val_full, image_shape=model_attributes['image_size'])
        y_val = np.array(list(y_val_full.values()),  dtype='float')
        x_test, id_test = format_x(x=x_test_full, image_shape=model_attributes['image_size'])
        y_test = np.array(list(y_test_full.values()),  dtype='float')
        
    elif model_attributes['gender'] == 'M':
        x_train, id_train = format_x(x=x_train_full, image_shape=model_attributes['image_size'], gender='M')
        y_train = np.array([y_train_full[i] for i in id_train], dtype='float')
        x_val, id_val = format_x(x=x_val_full, image_shape=model_attributes['image_size'], gender='M')
        y_val = np.array([y_val_full[i] for i in id_val], dtype='float')
        x_test, id_test = format_x(x=x_test_full, image_shape=model_attributes['image_size'], gender='M')
        y_test = np.array(list(y_test_full.values()),  dtype='float')
    elif model_attributes['gender'] == 'F':
        x_train, id_train = format_x(x=x_train_full, image_shape=model_attributes['image_size'], gender='F')
        y_train = np.array([y_train_full[i] for i in id_train], dtype='float')
        x_val, id_val = format_x(x=x_val_full, image_shape=model_attributes['image_size'], gender='F')
        y_val = np.array([y_val_full[i] for i in id_val], dtype='float')
        x_test, id_test = format_x(x=x_test_full, image_shape=model_attributes['image_size'], gender='F')
        y_test = np.array(list(y_test_full.values()),  dtype='float')
    del x_train_full, x_val_full, x_test_full ## Free up some memory


    print(x_val.shape)
    print(y_val.shape)
    print(x_test.shape)
    print(y_test.shape)
    bm = instantiate_base_model(model_name=model_attributes['base_model'],
                                input_dim=model_attributes['image_size'])


    full_model = Model(inputs=bm.input, outputs=tm(bm.output))
    full_model.load_weights(weights)
    full_model.compile(loss=attributes['retraining_loss'],
                  optimizer=attributes['retraining_optimizer'],
                  metrics=attributes['metrics'])
    
    all_predictions = []
    result_metric = dict()
    if 'train' in subset:
        print(full_model.evaluate(x_train, y_train, batch_size=32))
        train_pred = full_model.predict(x_train)
        train_predictions = dict()
        for i in range(len(x_train)):
            train_predictions[id_train[i]] = train_pred[i]
        all_predictions.append(train_predictions)
        train_mae = 0
        train_mse = 0
        for k in train_predictions.keys():
            train_mae += np.abs(train_predictions[k] - y_train_full[k])
            train_mse += np.square(train_predictions[k] - y_train_full[k])
        train_mae /= len(y_train)
        train_mse /= len(y_train)
        result_metric['mae'] = train_mae
        result_metric['mse'] = train_mse
        print('Train MAE: ' + str(train_mae) + '    ' + 'n=' + str(len(train_predictions)))
    if 'val' in subset:
        print(full_model.evaluate(x_val, y_val, batch_size=32))
        val_pred = full_model.predict(x_val)
        val_predictions = dict()
        for i in range(len(x_val)):
            val_predictions[id_val[i]] = val_pred[i]
        all_predictions.append(val_predictions)
        val_mae = 0
        val_mse = 0
        for k in val_predictions.keys():
            val_mae += np.abs(val_predictions[k] - y_val_full[k])
            val_mse += np.square(val_predictions[k] - y_val_full[k])
        val_mae /= len(y_val)
        val_mse /= len(y_val)
        result_metric['mae'] = val_mae
        result_metric['mse'] = val_mse
        print('Validation MAE: ' + str(val_mae) + '    ' + 'n=' + str(len(val_predictions)))
    if 'test' in subset:
        print(full_model.evaluate(x_test, y_test, batch_size=32))
        test_pred = full_model.predict(x_test)
        test_predictions = dict()
        for i in range(len(x_test)):
            test_predictions[id_test[i]] = test_pred[i]
        all_predictions.append(test_predictions)
        test_mae = 0
        test_mse = 0
        for k in test_predictions.keys():
            test_mae += np.abs(test_predictions[k] - y_test_full[k])
            test_mse += np.square(test_predictions[k] - y_test_full[k])
        test_mae /= len(y_test)
        test_mse /= len(y_test)
        result_metric['mae'] = test_mae
        result_metric['mse'] = test_mse
        print('Test MAE: ' + str(test_mae) + '    ' + 'n=' + str(len(test_predictions)))
    

    full_pred = dict()
    for i in all_predictions:
        for key in list(i.keys()):
            full_pred[key] = i[key] 

    sorted_pred = dict(sorted(full_pred.items(), key=operator.itemgetter(0)))
    #return(sorted_pred)
    return([sorted_pred, result_metric])


if __name__ == '__main__':
   #First organize and dump dataset to file, input parameters are image_size, train_test_split, gt_columns, image_path, gt_paths, picke_path.
    read_images(model_attributes['image_size'], model_attributes['train_test_split'],
                                        paths[1], paths[2], paths[3], paths[4])
    #Using female samples
    model_attributes['gender'] = 'F'
    #path to saved weights
    paths[6] = paths[0] + '/weights/best_female_model.h5'
    result_female = make_predictions(model_attributes, paths, tm, [ 'test'])
   
    #Using male samples
    model_attributes['gender'] = 'M' ## change gender
    #path to saved weights
    paths[6] = paths[0] + '/weights/best_male_model.h5'
    result_male = make_predictions(model_attributes, paths, tm, ['test'])
   
    pred_male= result_male[0]
    pred_female= result_female[0]
    ## Combine gender predictions
    pred = dict()
    for i in list(pred_male.keys()):
        pred[i] = pred_male[i]
    for i in list(pred_female.keys()):
        pred[i] = pred_female[i]
    sorted_predictions = dict(sorted(pred.items(), key=operator.itemgetter(0)))
   
    ## Write predictions to csv
    f = open(paths[0] + '/predictions/predictions.csv', 'w')
    try:
        writer = csv.writer(f, lineterminator = '\n')
        writer.writerow(['id', 'boneage'])
        for key in list(sorted_predictions.keys()):
            writer.writerow([key, float(sorted_predictions[key])])
    finally:
        f.close()




