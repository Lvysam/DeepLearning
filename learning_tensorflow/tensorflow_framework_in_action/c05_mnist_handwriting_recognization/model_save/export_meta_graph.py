"""
    An example model saving
    @author: Liu Weijie
    @date: 2018-04-09
    @reference: <Tensorflow: Deeplearning framework in Action>/Chapter5.4
"""
import tensorflow as tf

v1 = tf.get_variable("v1", shape=[1], initializer=tf.random_normal_initializer(mean=0.0, stddev=1.0), dtype=tf.float32)
v2 = tf.get_variable("v2", shape=[1], initializer=tf.random_normal_initializer(mean=0.0, stddev=1.0), dtype=tf.float32)
result = v1 + v2

saver = tf.train.Saver()
saver.export_meta_graph("/home/jagger/workspace/tmp/model.ckpt.meta", as_text=True)
