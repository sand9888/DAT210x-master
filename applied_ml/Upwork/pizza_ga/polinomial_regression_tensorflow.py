import tensorflow as tf
import numpy as np
import  matplotlib.pyplot as plt

n_observations = 100
fig, ax = plt.subplots(1, 1)
xs = np.linspace(-3, 3, n_observations)
ys = np.sin(xs) + np.random.uniform(-0.5, 0.5, n_observations)
ax.scatter(xs, ys)
# plt.show()

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

Y_pred = tf.Variable(tf.random_normal([1], seed=1234))
for pow_i in range(1,5):
	W = tf.Variable(tf.random_normal([1], seed=1234))
	Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)

cost = tf.reduce_sum(tf.pow(Y_pred - Y, 2)) / (n_observations - 1)
learning_rate = 0.01
optimize = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

n_epochs = 20
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	prev_cost = 0
	for epoch in range(n_epochs):
		for (x, y) in zip(xs, ys):
			sess.run(optimize, feed_dict={X:x, Y:y})
		
		training_cost = sess.run(cost, feed_dict={X:xs, Y:ys})
		print(training_cost)
		if epoch % 100 == 0:
			ax.plot(xs, Y_pred.eval(
				feed_dict={X: xs}, session=sess),
					'k', alpha=epoch / n_epochs)
			plt.show()
		
		# Allow the training to quit if we've reached a minimum
		if np.abs(prev_cost - training_cost) < 0.000001:
			break
		prev_cost = training_cost
	ax.set_ylim([-3, 3])
	plt.show()
	
	
	
