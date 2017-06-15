import tensorflow as tf
import matplotlib.pyplot as plt

num_val = 32
x = tf.linspace(-3., 3., num_val)

sess = tf.Session()
# res = sess.run(x)
# print(res)
#print(x.eval(session = sess))
sess.close()
sess = tf.InteractiveSession()
x.eval()

sigma = 1.0
mean = 0.0
z = (tf.exp(tf.negative(tf.pow(x - mean, 2.0) /
                   (2.0 * tf.pow(sigma, 2.0)))) *
     (1.0 / (sigma * tf.sqrt(2.0 * 3.1415))))

# assert z.graph is tf.get_default_graph()

plt.plot(x.eval(), z.eval())
# plt.show()
#print(z.eval(), z.get_shape())
# print(tf.stack([tf.shape(z), tf.shape(z), [3], [4]]).eval())
z2d = tf.matmul(tf.reshape(z, [num_val, 1]), tf.reshape(z, [1, num_val]))
# plt.imshow(z2d.eval())
# plt.show()
ops = tf.get_default_graph().get_operations()
print([op.name for op in ops])