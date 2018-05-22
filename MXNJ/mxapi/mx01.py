import mxnet as mx
import numpy as np

a = mx.ndarray.array([[1,2,3], [4,5,6]])
print(a.size, a.shape, a.dtype)

b = mx.ndarray.array([[1,2,3], [2,3,4]], dtype=np.int32)
print(b.dtype)
print(b.asnumpy())

c = mx.ndarray.array([[1,2,3], [4,5,6]])
d = c*c
print(d.asnumpy())

e = a.T
print(e.shape)
f = mx.ndarray.dot(a, e)
print(f.asnumpy())

g = mx.ndarray.uniform(low=0, high=1, shape=(1000, 1000), ctx="cpu(0)")
h = mx.ndarray.normal(loc=1, scale=2, shape=(1000, 1000), ctx="cpu(0)")

i = mx.ndarray.dot(g, h)
print(i.asnumpy())