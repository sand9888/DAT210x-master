import tensorflow as tf

X = tf.placeholder(tf.float32,[None, 28, 28, 1])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

init = tf.global_variables_initializer()

