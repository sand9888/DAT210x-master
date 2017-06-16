import tensorflow as tf
import pandas as pd

df = pd.read_csv('pizza_all_users.csv')
df.drop(['revenue', 'transactions', 'conv_rate'], axis=1, inplace=True)
n = df.shape[1]
m = df.shape[0]
epoch_n = 100
ys = df['users_tablet'].as_matrix()
xs = df.drop(['users_tablet'], axis=1).as_matrix()


W = tf.Variable(tf.zeros([n-1, 1], tf.float64))
b = tf.Variable(tf.zeros([1,], tf.float64))
X = tf.placeholder(tf.float64, [m, n-1])
Y = tf.placeholder(tf.float64)

Y_ = tf.add(tf.matmul(X, W), b)

cost = tf.reduce_mean(tf.square(Y_ - Y))
optimize = tf.train.GradientDescentOptimizer(0.001).minimize(cost)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for epoch in range(epoch_n):
		sess.run(optimize, feed_dict={X:xs, Y:ys})
		training_cost = sess.run(cost, feed_dict={X:xs, Y:ys})
		print(training_cost)

