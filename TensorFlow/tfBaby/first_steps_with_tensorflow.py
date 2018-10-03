from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
from sklearn import metrics

import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")

#california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0
print(california_housing_dataframe)

print(california_housing_dataframe.describe())

# Step 1
# Define the input feature: total rooms
my_feature = california_housing_dataframe[["total_rooms"]]

# Configure a numeric feature column for total_rooms
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

# Step 2
# Define the label
targets = california_housing_dataframe["median_house_value"]

# Step 3
# Use gradient descent as the optimizer for training the model
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

# Configure the linear regression model with our feature columns and optimizer.
# Set a learning rate of 0.0000001 for Gradient Descent.

linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns, optimizer=my_optimizer)

def my_input_fn(features, tatgets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model of one feature

    Args:
        features: pandas DataFrame of features
        targets: pandas Dataframe of targets
        batch_size: Size of batches to be passed to the model
        shuffle: True or False. Whether to shuffle the data
        num_epochs: Number of epochs for which data shoule be repeated. None = repeat indenfinitely
    Returns:
        Tuple of (features, labels) for next data batch
    """
    # Convert pandas data into a dict of np arrays.
    features = {key:np.array(value) for key, value in dict(features).items()}

    # Construcht a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if sppeified
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # Return the next batch of data
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

_ = linear_regressor.train(input_fn=lambda :my_input_fn(my_feature, targets),
                           steps=100)
