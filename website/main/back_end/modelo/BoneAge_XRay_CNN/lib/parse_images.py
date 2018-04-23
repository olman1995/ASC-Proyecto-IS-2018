# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 10:53:53 2017

@author: MedImaging7271
"""

import numpy as np
import os
from PIL import Image
import glob
import csv
import pickle


'''
ARGUMENTS
image_size: Tuple of image dimensions for resizing
train_test_split: Tuple of length 2 or 3. A length of 2 splits into train and validation sets, while
                        a length of 3 splits into train, validation, and test sets. Valued should be specified 
                        as proprortions that sum to one. e.g. (0.5, 0.5) or (0.7, 0.2, 0.1)
gt_columns: List of column header names specifying columns to read from a ground truth csv (syntax/case-sensitive)
                        Important: First column name should represent the id, followed by the response (if labels=True).
                                   Any additional columns will be provided as inputs
image_paths: List of paths to raw images with appropriate file format specfied  e.g. C:\\path_to_image\\*.png
gt_paths: Dictionary with key-value pairs of ground_truth_path : delimiter. gt file should be in csv format.
pickle_dir: (Optional) String specifying directory to save pickled data
labels: (Optional) Boolean specifying whether labels are included in ground truth file.
                     When set to False, first column should represent id and any further columns represent additional inputs

RETURNS
A list containing 4 or 6 dictionaries:
    inputs_train, outputs_train, inputs_val, outputs_val (and optionally inputs_test, outputs_test)
Dictionaries map image id's to inputs and outputs
Input dictionaries contain the flattened images along with any extra input data
Output dictionaries contain the output variable (categorical or continuous)

'''
def read_images(image_size, train_test_split, gt_columns, image_paths, gt_paths, pickle_dir='', labels=True):
    
    ## Some error handling
    if len(train_test_split) < 1 or len(train_test_split) > 3:
        raise ValueError('train_test_split must be a tuple of length 2 or 3')
    if sum(train_test_split) != 1:
        raise ValueError('train_test_split values must sum to 1')
    
    ## Read images from directory
    #print('Reading images from directory...')
    raw = dict()
    for path in image_paths:
        for filename in glob.glob(path): 
            name = os.path.basename(filename)[:-4]
            if not name in list(raw.keys()):
                try:
                    im = Image.open(filename)
                    im = im.convert('L')     # Convert all images to greyscale in case of alternative channel specs
                    im = im.resize(image_size)  #Resize all images to standard sizing
                    raw[int(name)] = np.array(list(im.getdata()))
                    im.close()
                except IOError:
                    print('Error loading image ', filename)

    ## Read image id's and class labels from csv, with dictionary mapping ids to ground truth data
    #print('Reading ground truth data...')
    name_to_output = dict()
    name_to_additional_inputs = dict()
    for path in list(gt_paths.keys()):
        delim = gt_paths[path]
        with open(path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=delim)
            headers = next(readCSV)
            
            ## Handle column labels that are not found in csv
            if not set(gt_columns).issubset(headers):
                raise ValueError('Unknown column name passed. Insure that case-sensitive column names match csv.')

                
            for row in readCSV:
                try:
                    name_to_output[int(row[0])] = int(row[1])
                    name_to_additional_inputs[int(row[0])] = row[1:]
                except ValueError as error:
                    print('Issue reading csv... please review format' + repr(error))
           
            
    ## Check for mismatched images and ground truth pairs
    for gt_data in [name_to_output, name_to_additional_inputs]:    
        ## Delete any image_id - ground truth pairs for which there is no corresponding image            
        for key in list(gt_data.keys()):
            if not key in list(raw.keys()):
                #print('WARNING: ground truth value ' + str(key) + 
                #      ' has no corresponding image! This ground truth value will be deleted')
                del gt_data[key]
        
        #Delete any images for which there is no corresponding class label
        for key in list(raw.keys()):
            if not key in list(gt_data.keys()):
                print('WARNING: image id ' + str(key) +
                      ' has no corresponding ground truth data! Image will be deleted')
                del raw[key]

    ## Check that no repeated images and that each single image maps to a single class label
    for gt_data in [name_to_output, name_to_additional_inputs]:  
        raw_keys = list(gt_data.keys())
        gt_keys = list(raw.keys())
        num_matching_keys = sum(np.sort(raw_keys) == np.sort(gt_keys))
        if not num_matching_keys == len(raw_keys):
            raise ValueError('Mismatch between image labels and ground truth labels')
        if not len(np.unique(raw_keys)) == len(raw_keys):
            raise ValueError('There are repeated images! Please delete repeats')
    
    ## Cast data to dictionaries of numpy arrays
    inputs = dict()
    outputs = dict()
    for key in list(raw.keys()):
        in_col = []
        in_col.append(raw[key])
        for col_num in range(1, (len(gt_data[key]))):
            try:
                in_col.append(np.array(gt_data[key][col_num]).astype('float'))
            except ValueError:
                in_col.append(int(gt_data[key][col_num] == 'True'))
        inputs[key] = in_col
        
        try:
            outputs[key] = np.array(gt_data[key][0]).astype('float')
        except ValueError:
            outputs[key] = int(gt_data[key][0] == 'True')
    
    
    ## Randomly shuffle data and split into train and validation (and possibly test) sets
    shuffle_ind = np.random.choice(list(inputs.keys()), size=len(inputs), replace=False)
    cutoffs = np.zeros(len(train_test_split), dtype='uint32')
    for i in range(len(train_test_split)):
        cutoffs[i] = round(np.sum(train_test_split[:i+1]) * len(shuffle_ind))
    
    inputs_train = {k: inputs[k] for k in shuffle_ind[:cutoffs[0]]}
    outputs_train = {k: outputs[k] for k in shuffle_ind[:cutoffs[0]]}
    inputs_val = {k: inputs[k] for k in shuffle_ind[cutoffs[0]:cutoffs[1]]}
    outputs_val = {k: outputs[k] for k in shuffle_ind[cutoffs[0]:cutoffs[1]]}
    full_dataset = [inputs_train, outputs_train, inputs_val, outputs_val]
    if not (train_test_split[0] + train_test_split[1]) == 1:
        inputs_test = {k: inputs[k] for k in shuffle_ind[cutoffs[1]:]}
        full_dataset.append(inputs_test)
        outputs_test = {k: outputs[k] for k in shuffle_ind[cutoffs[1]:]}
        full_dataset.append(outputs_test)
    save_ids('image_id.csv', inputs_train, inputs_val)    
    
    ## Pickle data
    print('Pickling data...')
    if not pickle_dir == '':
        pickle.dump(full_dataset, open(pickle_dir, 'wb'), protocol = 4)
        
    return(full_dataset)
    
'''
Read train and test image ids from csv
'''
def train_test_ids(path_to_csv):
    ## Read image id's to csv
    ids = []
    f = open(path_to_csv, 'r')
    r = csv.reader(f)
    for row in r:
        ids.append(row)
    f.close()
    return([[int(i) for i in ids[1]], [int(i) for i in ids[3]]])

def unpickle(path): 
    return(pickle.load(open(path, 'rb')))

def save_ids(path, id_train, id_val):
    ## Write image id's of data subsets to csv
    f = open(path, 'w', newline='')
    try:
        writer = csv.writer(f)
        writer.writerow(['train image ids'])
        writer.writerow(id_train)
        writer.writerow(['validation image ids'])
        writer.writerow(id_val)
    finally:
        f.close()
