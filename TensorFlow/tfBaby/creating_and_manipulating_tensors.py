from __future__ import print_function
import tensorflow as tf

with tf.Graph().as_default():
    # Create a six element vector(1D tensor)
    primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

    # Create another six element vector. Each element in the vector will
    # initialized to 1. The first argument is the shape of the vector(more on shapes below)
    ones = tf.ones([6], dtype=tf.int32)

    # Add the two vectors. The resulting tensor is a six element vector.
    just_beyond_primes = tf.add(primes, ones)

    # Create a session to run the default graph.
    with tf.Session() as sess:
        print(just_beyond_primes.eval())

with tf.Graph().as_default():
    # A scalar(0D tensor)
    scalar = tf.zeros([])

    # A vector with 3 elements
    vector = tf.zeros([3])

    # A matrix with 2 rows and 3 columns
    matrix = tf.zeros([2, 3])

    with tf.Session() as sess:
        print('scalar has shape', scalar.get_shape(), 'and value:\n', scalar.eval())
        print('vector has shape', vector.get_shape(), 'and value:\n', vector.eval())
        print('matrix has shape', matrix.get_shape(), 'and value:\n', matrix.eval())

with tf.Graph().as_default():
    # Create a six element vector(1D tensor)
    primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

    # Create a constant scalar with value 1
    ones = tf.constant(1, dtype=tf.int32)

    # Add the two tensors. The resulting tensor is a six element vector
    just_beyond_primes = tf.add(primes, ones)

    with tf.Session() as sess:
        print(just_beyond_primes.eval())

with tf.Graph().as_default():
    # Create an 8x2 matrix(2D tensor)
    matrix = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8],
                          [9, 10], [11, 12], [13, 14], [15, 16]], dtype=tf.int32)

    # Reshape the 8x2 matrix into a 2x8 matrix
    reshaped_2x8_matrix = tf.reshape(matrix, [2, 8])

    # Reshape the 8x2 matrix into a 4x4 matrix
    reshaped_4x4_matrix = tf.reshape(matrix, [4, 4])

    with tf.Session() as sess:
        print("Original matrix (8x2):")
        print(matrix.eval())
        print("Reshaped matrix (2x8):")
        print(reshaped_2x8_matrix.eval())
        print("Reshaped matrix (4x4):")
        print(reshaped_4x4_matrix.eval())

with tf.Graph().as_default():
    # Create an 8x2 matrix(2D tensor)
    matrix = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8],
                          [9, 10], [11, 12], [13, 14], [15, 16]], dtype=tf.int32)

    # Reshape the 8x2 matrix into a 3D 2x2x4 tensor
    reshaped_2x2x4_tensor = tf.reshape(matrix, [2, 2, 4])

    # Reshape the 8x2 matrix into a 1D 16 element tensor
    one_dimensional_vector = tf.reshape(matrix, [16])

    with tf.Session() as sess:
        print("Oringinal matrix (8x2)")
        print(matrix.eval())
        print("Reshaped 3D tensor (2x2x4)")
        print(reshaped_2x2x4_tensor.eval())
        print("Reshaped 1D vector")
        print(one_dimensional_vector.eval())

# Exercise 1
with tf.Graph().as_default():
    a = tf.constant([5, 3, 2, 7, 1, 4])
    b = tf.constant([4, 6, 3])

    reshaped_a = tf.reshape(a, [2, 3])
    reshaped_b = tf.reshape(b, [3, 1])

    result = tf.matmul(reshaped_a, reshaped_b)

    with tf.Session() as sess:
        print(result.eval())

print("---------------------------------------")

g = tf.Graph()

with g.as_default():
    # Create a variable with the initial value 3
    v = tf.Variable([3])

    # Create a variable of shape [1], with a random initial value,
    # sampled from a normal distribution with mean 1 and standard deviation 0.35
    w = tf.Variable(tf.random_normal([1], mean=1.0, stddev=0.35))

with g.as_default():
    with tf.Session() as sess:
        try:
            v.eval()
        except tf.errors.FailedPreconditionError as e:
            print("Caught expected error: ", e)

with g.as_default():
    with tf.Session() as sess:
        initialzation = tf.global_variables_initializer()
        sess.run(initialzation)

        # Now variables can be accessed normally, and have values assigned to them
        print(v.eval())
        print(w.eval())

# Another conversation
with g.as_default():
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # These prints will print the same value
        print(w.eval())
        print(w.eval())
        print(w.eval())

with g.as_default():
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # This should print the variable's initial value.
        print(v.eval())

        assignment = tf.assign(v, [7])
        # The variable has not been changed yet
        print(v.eval())

        # Execute the assignment op
        sess.run(assignment)
        # Now the variable is updated
        print(v.eval())

# Exercise 2
with tf.Graph().as_default():
    dialect_1 = tf.Variable(tf.random_uniform([10, 1], minval=1, maxval=7, dtype=tf.int32))
    dialect_2 = tf.Variable(tf.random_uniform([10, 1], minval=1, maxval=7, dtype=tf.int32))

    dialect_sum = tf.add(dialect_1, dialect_2)

    simulator = tf.concat(values=[dialect_1, dialect_2, dialect_sum], axis=1, name='concat')

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print((tf.reshape(dialect_1, [1, 10])).eval())
        print((tf.reshape(dialect_2, [1, 10])).eval())
        print(simulator.eval())
