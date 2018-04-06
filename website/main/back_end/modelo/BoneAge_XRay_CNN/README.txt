The directory tree is organized as follows:

    - ./dataset
    As its name says, the image dataset used for training, validating and testing is stored here in a compressed zip. There's also a csv file for ground-truth data, which specifies the name, sex and age of all the images. You must unzip the dataset in this directory and modify the dataset_path variable in parameters.py

    - ./lib
    This directory is for modules used by the output_predictions.py program. 

    - ./weights
    The trained weights for female and male models are stored here.

    - ./predictions
    The prediction results are stored here with the filename predictions.csv

    - ./output_predictions.py
    This is the main program which loads the image dataset, organizes the datasets and performs the predictions

    - ./parameters.py
    Model architecture, hyperparameters, attributes, and so on.

**Instructions:**

- Set parameters in parameters.py, then run __main__.py.

- Requirments:
  -Python 3.5 with standard modules (numpy, pickle etc)
  -tensorflow
  -keras
  -pillow

- To run use this command:
     python output_predictions.py



