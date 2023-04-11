import pandas as pd 

# Import comet_ml at the top of your file
# from comet_ml import Experiment

import numpy as np
import tensorflow as tf
import time
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class CVAE(tf.keras.Model):
  """Convolutional variational autoencoder."""

  def __init__(self, latent_dim):
    super(CVAE, self).__init__()
    self.latent_dim = latent_dim
    self.encoder = tf.keras.Sequential(
        [
            tf.keras.layers.InputLayer(input_shape=(13,)),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.5, name = 'dropout1'),
            tf.keras.layers.Dense(32, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.5, name = 'dropout2'),
            tf.keras.layers.Dense(latent_dim*2),
        ]
    )

    self.decoder = tf.keras.Sequential(
        [
            tf.keras.layers.InputLayer(input_shape=(latent_dim,)),
            tf.keras.layers.Dense(32, activation=tf.nn.relu),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(13)
        ]
    )

  @tf.function
  def sample(self, eps=None):
    if eps is None:
      eps = tf.random.normal(shape=(100, self.latent_dim))
    return self.decode(eps, apply_sigmoid=True)

  def encode(self, x):
    mean, logvar = tf.split(self.encoder(x), num_or_size_splits=2, axis=1)
    return mean, logvar
  
  def set_encrypt_params(self, names=None, dicts=None):
    """
    names -- names of features
    dicts -- dicts with {'feature': normalized_value}
    set self.names and self.feature_dicts
    """
    self.names = names
    self.feature_dicts = dicts
  
  def encrypt(self, data):
    """
    return 2 neighbors with their possibilities
    """
    mean, logvar = self.encode(data)
    z = self.reparameterize(mean, logvar)
    predictions = self.sample(z)
    encrypt_res = [] # [[{neighbor1}, {neighbor1}], ...]
    possibilities = []
    for predict in predictions:
      features, p = [], []
      for n, feature in enumerate(predict):
        feature1, val1 = min(self.feature_dicts[n].items(), key=lambda x: abs(feature - x[1]))
        feature2, val2 = min(self.feature_dicts[n].items().copy().pop(feature1), key=lambda x: abs(feature - x[1]))
        features.append([feature1, feature2])
        p.append([val1*100/abs(val2 - val1), val2*100/abs(val2 - val1)])
      encrypt_res.append(features)
      possibilities.append(p)
    return encrypt_res, possibilities


  def reparameterize(self, mean, logvar):
    eps = tf.random.normal(shape=mean.shape)
    return eps * tf.exp(logvar * .5) + mean

  def decode(self, z, apply_sigmoid=False):
    logits = self.decoder(z)
    if apply_sigmoid:
      probs = tf.sigmoid(logits)
      return probs
    return logits