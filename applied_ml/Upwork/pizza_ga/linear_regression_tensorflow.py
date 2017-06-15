import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def generate_dataset():
	x_batch = np.linspace(-1, 1, 101)
	y_batch = 2 * x_batch + np.random.randn(*x_batch.shape)*0.3
	print(np.random.randn(*x_batch.shape))
	return x_batch, y_batch

def linear_regression():
	x = tf.placeholder(tf.float32, shape=(None,), name='x')
	y = tf.placeholder(tf.float32, shape=(None,), name='y')
	
	with tf.variable_scope('lreg') as scope:
		w = tf.Variable(np.random.normal(), name='W')
		y_pred = tf.multiply(w, x)
		loss = tf.reduce_mean(tf.square(y_pred-y))
		return x, y, y_pred, loss

def run():
	x_batch, y_batch = generate_dataset()
	x, y, y_pred, loss = linear_regression()
	optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
	init = tf.global_variables_initializer()
	with tf.Session() as session:
		session.run(init)
		feed_dict = {x: x_batch, y: y_batch}
		for _ in range(30):
			loss_value, _ = session.run([loss, optimizer], feed_dict)
			print('loss value: ', loss_value.mean())
		y_pred_batch = session.run(y_pred, {x: x_batch})
	plt.figure(1)
	plt.scatter(x_batch, y_batch)
	plt.plot(x_batch, y_pred_batch)
	plt.show()

run()
		
	

		
		