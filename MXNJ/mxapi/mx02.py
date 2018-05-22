import mxnet as mx
import numpy as np

a = mx.symbol.Variable('A')
b = mx.symbol.Variable('B')
c = mx.symbol.Variable('C')
d = mx.symbol.Variable('D')
e = (a * b) + (c * d)

print(a, b, c, d)
print(e, type(e))
print(e.list_arguments())
print(e.list_outputs())
print(e.get_internals().list_outputs())


a_data = mx.ndarray.array([1], dtype=np.int32)
b_data = mx.ndarray.array([2], dtype=np.int32)
c_data = mx.ndarray.array([3], dtype=np.int32)
d_data = mx.ndarray.array([4], dtype=np.int32)

executor = e.bind(mx.cpu(), {'A':a_data, 'B':b_data, 'C':c_data, 'D':d_data})
print(executor)
print(executor.forward())
print(executor.forward()[0].asnumpy())

f_data = mx.ndarray.uniform(low=0, high=1, shape=(1000,1000))
g_data = mx.ndarray.uniform(low=0, high=1, shape=(1000,1000))
h_data = mx.ndarray.uniform(low=0, high=1, shape=(1000,1000))
i_data = mx.ndarray.uniform(low=0, high=1, shape=(1000,1000))

executor_ = e.bind(mx.cpu(), {'A':f_data, 'B':g_data, 'C':h_data, 'D':i_data})
print(executor_)
print(executor_.forward())
print(executor_.forward()[0].asnumpy())
