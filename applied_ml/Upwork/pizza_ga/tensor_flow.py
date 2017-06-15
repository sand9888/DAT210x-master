import tensorflow as tf

W = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)
x = tf.placeholder(tf.float32)

# model
linear_model = W*x + b

# init
init = tf.global_variables_initializer()

sess = tf.Session()
#sess.run(init)

#res = sess.run(linear_model, {x: [0,1,2,3]})
#print(res)

y = tf.placeholder(tf.float32)
squared_error = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_error)
# print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)
fit = optimizer.minimize(loss)
sess.run(init)
for i in range(100000):
	sess.run(fit, {x:[1,2,3,4], y:[0,-1,-2,-3]})
print(sess.run([W, b]))
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


