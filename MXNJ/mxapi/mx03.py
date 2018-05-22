import mxnet as mx
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
sample_count = 1000
train_count = 800
valid_count = 200
feature_count = 100
category_count = 10
batch = 10

# Generate data
X = mx.ndarray.uniform(low=0, high=1, shape=(sample_count, feature_count))
Y = mx.ndarray.empty((sample_count,))
for i in range(0, sample_count-1):
  Y[i] = np.random.randint(0, category_count)

# Split data
# Why minus one dim?
X_train = mx.ndarray.crop(X, begin=(0, 0), end=(train_count, feature_count)) # -1
X_valid = mx.ndarray.crop(X, begin=(train_count, 0), end=(sample_count, feature_count))
Y_train = Y[0 : train_count]
Y_valid = Y[train_count : sample_count]

# Prepare network
data = mx.symbol.Variable('data')
fc1 = mx.symbol.FullyConnected(data, name='fc1', num_hidden=64)
relu1 = mx.symbol.Activation(fc1, name='relu1', act_type="relu")
fc2 = mx.symbol.FullyConnected(relu1, name='fc2', num_hidden=category_count)
out = mx.symbol.SoftmaxOutput(fc2, name='softmax')
mod = mx.module.Module(out)


# Prepare training
train_iter = mx.io.NDArrayIter(data=X_train, label=Y_train, batch_size=batch)
# for it in train_iter:
#     print(it.data)
#     print(it.label)
#     break

mod.bind(data_shapes=train_iter.provide_data, label_shapes=train_iter.provide_label)
# Allowed, but not efficient
#mod.init_params()
# Much better
mod.init_params(initializer=mx.init.Xavier(magnitude=2.))
mod.init_optimizer(optimizer='sgd', optimizer_params=(('learning_rate', 0.1), ))

mod.fit(train_iter, num_epoch=50)


# Prepare validation
pred_iter = mx.io.NDArrayIter(data=X_valid, label=Y_valid, batch_size=batch)
pred_count = valid_count
correct_preds = total_correct_preds = 0

for preds, i_batch, batch in mod.iter_predict(pred_iter):
    label = batch.label[0].asnumpy().astype(int)
    pred_label = preds[0].asnumpy().argmax(axis=1)
    print(preds[0].asnumpy().argmax(axis=1))
    correct_preds = np.sum(pred_label==label)
    total_correct_preds += correct_preds

print('Validation accuracy: %2.2f' % (1.0*total_correct_preds/pred_count))
