import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = np.shape(X)[0]
  num_class = W.shape[1]
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run int(o numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(num_train):
    scores = X[i].dot(W)
    tmp = np.sum(np.exp(scores))
    for j in range(num_class):
      if y[i] == j:
        loss -= scores[j]
        dW[:,j] += -X[i] + X[i] * np.exp(scores[j]) / tmp
      else:
        dW[:,j] += X[i] * np.exp(scores[j]) / tmp
    loss += np.log(tmp)
  loss /= num_train
  loss += reg * np.sum(W * W)
  dW /= num_train
  dW += 2 * reg * W
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################


  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W) # N x C
  tmp = np.sum(np.exp(scores),1) # N x 1
  loss += np.sum(np.log(tmp))
  loss -= np.sum(scores[range(0,num_train),y])
  loss /= num_train
  loss += reg * np.sum(W * W)
  tmp = np.exp(scores) / tmp.reshape((num_train,1))
  tmp[range(0,num_train),y] -= 1
  dW += np.dot(X.T, tmp)
  dW /= num_train
  dW += 2 * reg * W
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

