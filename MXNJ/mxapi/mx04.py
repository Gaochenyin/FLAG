import mxnet as mx
import numpy as np
from collections import namedtuple

import cv2

sym, arg_params, aux_params = mx.model.load_checkpoint('Inception-BN', 0)

mod = mx.module.Module(symbol=sym)

mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))])

mod.set_params(arg_params, aux_params)

# Prepare picture
img = cv2.imread('cat.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224, 224,))
img = np.swapaxes(img, 0, 2)
img = np.swapaxes(img, 1, 2)
img = img[np.newaxis, :]
array = mx.nd.array(img) # batch*rgb*h*w
print(array.shape)


Batch = namedtuple('Batch', ['data'])
mod.forward(Batch([array]))
prob = mod.get_outputs()[0].asnumpy()
print(prob.shape) # prob.sum() = 1
prob = np.squeeze(prob)
print(prob.shape)
sortedprob = np.argsort(prob)[::-1] # [::-1]reverse
#print(sortedprob)

synsetfile = open('synset.txt', 'r')
categorylist = []
for line in synsetfile:
  categorylist.append(line.rstrip())

print('Classify 1st:', categorylist[sortedprob[0]])
print('Classify 2nd:', categorylist[sortedprob[1]])
print('Classify 3rd:', categorylist[sortedprob[2]])
