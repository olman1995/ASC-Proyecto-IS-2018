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
from .lib.parse_images import read_images, train_test_ids, unpickle
from .lib.tools import Tools
from .parameters import initialize_parameters


class Predict:
    def __init__(self):
        self.tool = Tools()

    def make_predictions(self, attributes, paths, tm, subset=['train', 'val', 'test']):
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
        all_x = {**bone_age_data[0]}
        all_y = {**bone_age_data[1]}
        all_ids = list(all_x.keys())
        id_predict = []
        for i in all_ids:
            id_predict.append(i)
        x_predict_full = {key: all_x[key] for key in id_predict}
        y_predict_full = {key: all_y[key] for key in id_predict}
        if model_attributes['gender'] == '':
            x_predict, id_predict = self.tool.format_x(x=x_predict_full, image_shape=model_attributes['image_size'])
            y_predict = np.array(list(y_predict_full.values()),  dtype='float')
        elif model_attributes['gender'] == 'M':
            x_predict, id_predict = self.tool.format_x(x=x_predict_full, image_shape=model_attributes['image_size'])
            y_predict = np.array(list(y_predict_full.values()),  dtype='float')
        elif model_attributes['gender'] == 'F':
            x_predict, id_predict = self.tool.format_x(x=x_predict_full, image_shape=model_attributes['image_size'])
            y_predict = np.array(list(y_predict_full.values()),  dtype='float')
        del x_predict_full
        bm = self.tool.instantiate_base_model(model_name=model_attributes['base_model'],
                                              input_dim=model_attributes['image_size'])
        full_model = Model(inputs=bm.input, outputs=tm(bm.output))
        full_model.load_weights(weights)
        full_model.compile(loss=attributes['retraining_loss'],
                           optimizer=attributes['retraining_optimizer'],
                           metrics=attributes['metrics'])
        if 'predict' in subset:
            full_model.evaluate(x_predict, y_predict, batch_size=32)
            predict_pred = full_model.predict(x_predict)
        del full_model
        return(predict_pred)

    def star(self):
        self.model_attributes, self.training_scope, self.paths, self.datagen, self.tm = initialize_parameters(self.tool)

    def predict(self, sexo):
        self.paths[2] = [self.paths[0]+'/dataset/test/*.png']
        read_images(self.model_attributes['image_size'], self.model_attributes['train_test_split'],
                    self.paths[1], self.paths[2], self.paths[3], self.paths[4])
        if sexo == "F":
            self.model_attributes['gender'] = 'F'
            self.paths[6] = self.paths[0] + '/weights/best_female_model.h5'
            result_female = self.make_predictions(self.model_attributes, self.paths, self.tm, ['predict'])
            K.clear_session()
            return result_female
        else:
            self.model_attributes['gender'] = 'M'
            self.paths[6] = self.paths[0] + '/weights/best_male_model.h5'
            result_male = self.make_predictions(self.model_attributes, self.paths, self.tm, ['predict'])
            K.clear_session()
            return result_male
        
    def predict_1(self, data,sex):
        result=[]
       
        for i in range(len(data)) : 
            
            self.paths[2] = [self.paths[0]+'../../../../media/test/'+str(data[i])+'.png']
            read_images(self.model_attributes['image_size'], self.model_attributes['train_test_split'],
                        self.paths[1], self.paths[2], self.paths[3], self.paths[4])
            
            if "F" == sex[i]:
                self.model_attributes['gender'] = 'F'
                self.paths[6] = self.paths[0] + '/weights/best_female_model.h5'
                result.append( self.make_predictions(self.model_attributes, self.paths, self.tm, ['predict'])[0][0])
            else:
                self.model_attributes['gender'] = 'M'
                self.paths[6] = self.paths[0] + '/weights/best_male_model.h5'
                result.append( self.make_predictions(self.model_attributes, self.paths, self.tm, ['predict'])[0][0])
            
        K.clear_session()
            
        return result
    
