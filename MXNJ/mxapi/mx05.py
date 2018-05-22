import mxnet as mx
import numpy as np
from collections import namedtuple

import cv2
import time

def loadImg(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224,))
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2)
    img = img[np.newaxis, :]
    array = mx.ndarray.array(img)  # batch*rgb*h*w
    return array

def loadModel(modelname):
    sym, arg_params, aux_params = mx.model.load_checkpoint(modelname, 0)
    model = mx.mod.Module(symbol=sym)
    model.bind(for_training=False, data_shapes=[('data', (1, 3, 224, 224))])
    model.set_params(arg_params, aux_params)
    return model

def loadCategories():
    synsetfile = open('synset.txt', 'r')
    categorylist = []
    for line in synsetfile:
        categorylist.append(line.rstrip())
    return categorylist

def init(modelname):
    model = loadModel(modelname)
    category = loadCategories()
    return model, category

def test(times):
    img = loadImg('cat.jpg')
    model, category = init('Inception-BN')

    for i in range(0, times):
        Batch = namedtuple('Batch', ['data'])
        tic = time.time()
        model.forward(Batch([img]))
        toc = time.time()
        t = 1000 * (toc - tic)
        print("Predicted in %2.2f microseconds" % t)

        prob = model.get_outputs()[0].asnumpy()
        prob = np.squeeze(prob)
        sortedprob = np.argsort(prob)[::-1]  # [::-1]reverse

        print('Classify 1st:', category[sortedprob[0]])
        print('Classify 2nd:', category[sortedprob[1]])
        print('Classify 3rd:', category[sortedprob[2]])

if __name__ == '__main__':
    test(3)
