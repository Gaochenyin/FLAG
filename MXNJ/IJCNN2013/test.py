#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# S0
import csv

def read_csv_signnames():
    traffic_labels_dict={}
    with open('data/signnames.csv') as f:
        signnames = csv.reader(f)
        for signname in signnames:
            traffic_labels_dict[signname[0]] = signname[1]
    return traffic_labels_dict

traffic_labels_dict = read_csv_signnames()

# S1 Load model checkpoint
import mxnet as mx
sym, arg_params, aux_params = mx.model.load_checkpoint('model/IJCNN-alexnet', 1000)

model = mx.module.Module(symbol=sym, context=mx.cpu())
model.bind(for_training=False, data_shapes=[('data', (1,3,32,32))])
model.set_params(arg_params, aux_params)


# S2 Pridect image
from collections import namedtuple
from matplotlib import pyplot as plt
import cv2
import numpy as np

Batch = namedtuple('Batch', ['data'])

def get_image(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to (batch, RGB, width, height)
    img = cv2.resize(img, (32,32))
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2)
    img = img[np.newaxis, :]

    return img

def predict(file):
    img = get_image(file)

    model.forward(Batch([mx.ndarray.array(img)]))
    prob = model.get_outputs()[0].asnumpy()
    prob = np.squeeze(prob)
    prob = np.argsort(prob)[::-1]

    for i in prob[0:5]:
        print('%d' %i, '%s' %(traffic_labels_dict[str(i)]))

predict('data/stop.jpg')
