#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# S1 Load dataset from pickle file
import pickle

training_file = 'data/train_set.p'
with open(training_file, 'rb') as t:
    train = pickle.load(t)

validation_file = 'data/valid_set.p'
with open(validation_file, 'rb') as v:
    valid = pickle.load(v)

# train: 34799 + valid: 4410  = total: 39209
X_train, y_train = train['features'], train['labels']
X_valid, y_valid = valid['features'], valid['labels']

print('S1 done.')


# S2 Read sign name csv label mapping
import csv

def read_csv_signnames():
    traffic_labels_dict={}
    with open('data/signnames.csv') as f:
        signnames = csv.reader(f)
        for signname in signnames:
            traffic_labels_dict[signname[0]] = signname[1]
    return traffic_labels_dict

traffic_labels_dict = read_csv_signnames()

print('S2 done.')


# S3 Data visualization
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.figure import Figure

def get_images_to_plot(images, labels):
    image, label = [], []
    for i in range(len(traffic_labels_dict)):
        selected = np.where(i == labels)[0][0]
        image.append(images[selected])
        label.append(selected)

    return image, label

def plot_images(images, index, labels, rows, cols):
    fig, ax = plt.subplots(rows, cols)

    count = 0
    for row in range(rows):
        for col in range(cols):
            if(count < len(images)):
                ax[row,col].imshow(images[count])
                ax[row,col].set_title(traffic_labels_dict[str(labels[index[count]])], fontsize=10)
            ax[row,col].axis('off')
            count += 1
    plt.show()

#images, index = get_images_to_plot(X_train, y_train)
#plot_images(images, index, y_train, 10, 5)

print('S3 done.')


# S4 Training data prepare
from sklearn.model_selection import train_test_split
import mxnet as mx

#X_train_set, X_validation_set, y_train_set, y_validation_set = train_test_split(X_train, y_train, test_size=0.02, random_state=42)
X_train_set, X_valid_set, y_train_set, y_valid_set = X_train, X_valid, y_train, y_valid

X_train_set_reshape = np.transpose(X_train_set, (0,3,1,2))
X_valid_set_reshape = np.transpose(X_valid_set, (0,3,1,2))

print('train set X shape: ', X_train_set_reshape.shape)
print('valid set X shape: ', X_valid_set_reshape.shape)

print('train set y shape: ', y_train_set.shape)
print('valid set y shape: ', y_valid_set.shape)

fuck_size = 64

X_train_set_float = X_train_set_reshape.astype('float32')
X_train_set_norm  = X_train_set_float[:] / 255.0
X_valid_set_float = X_valid_set_reshape.astype('float32')
X_valid_set_norm  = X_valid_set_float[:] / 255.0

train_iter = mx.io.NDArrayIter(X_train_set_norm, y_train_set, batch_size=fuck_size, shuffle=True)
valid_iter = mx.io.NDArrayIter(X_valid_set_norm, y_valid_set, batch_size=fuck_size, shuffle=True)

print('S4 done.')


# S5 Built networks - Alex Net
data = mx.symbol.Variable('data')

# Conv1
conv1 = mx.symbol.Convolution(data=data, kernel=(3,3), pad=(1,1), num_filter=24, name='conv1')
relu1 = mx.symbol.Activation(data=conv1, act_type='relu', name='relu1')
pool1 = mx.symbol.Pooling(data=relu1, pool_type='max', kernel=(2,2), stride=(2,2), name='max_pool1')
# Conv2
conv2 = mx.symbol.Convolution(data=pool1, kernel=(3,3), pad=(1,1), num_filter=48, name='conv2')
relu2 = mx.symbol.Activation(data=conv2, act_type='relu', name='relu2')
pool2 = mx.symbol.Pooling(data=relu2, pool_type='max', kernel=(2,2), stride=(2,2), name='max_pool2')
# Conv3
conv3 = mx.symbol.Convolution(data=pool2, kernel=(5,5), num_filter=64, name='conv3')
relu3 = mx.symbol.Activation(data=conv3, act_type='relu', name='relu3')
pool3 = mx.symbol.Pooling(data=relu3, pool_type='max', kernel=(2,2), stride=(2,2), name='max_pool3')
# FC1
flatten = mx.symbol.Flatten(data=pool3)
fc1 = mx.symbol.FullyConnected(data=flatten, num_hidden=500, name='fc1')
relu4 = mx.symbol.Activation(data=fc1, act_type='relu', name='relu4')
# FC2
fc2 = mx.symbol.FullyConnected(data=relu4, num_hidden=43, name='fc2')
# Softmax
alexnet = mx.symbol.SoftmaxOutput(data=fc2, name='softmax')

print('S5 done.')


# S6 Train networks

# Built adam optimizer
adam = mx.optimizer.create('adam')

model_prefix = 'model/IJCNN-alexnet'
checkpoint = mx.callback.do_checkpoint(model_prefix)

model = mx.module.Module(
    context=mx.cpu(0),
    symbol=alexnet,
    data_names=['data']
)

model.fit(
    train_iter,
    eval_data=valid_iter,
    num_epoch=100,
    eval_metric='acc',
    optimizer=adam,
    batch_end_callback=mx.callback.Speedometer(fuck_size, 64),
    epoch_end_callback=checkpoint
)

print('S6 FUCK!')
