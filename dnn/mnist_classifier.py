
import math
import random
import numpy as np


class NeuronLayer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))

    def forward(self, inputs):
        return np.dot(inputs, self.weights) + self.biases
        
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNet:
    def __init__(self, input_size, hidden_size, output_size):
        self.hiddenLayer = NeuronLayer(input_size, hidden_size)
        self.outputLayer = NeuronLayer(hidden_size, output_size)
    
    def forward(self, X):
        self.hidden = sigmoid(self.hidden_layer.forward(X))
        self.output = sigmoid(self.outputLayer.foward(self.hidden))
        return self.output

    def backward(self, X, y, output, learning_rate):
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        hidden_error = np.dot(output_delta, self.output_layer.weights.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden)

        self.output_layer.weights += learning_rate * np.dot(self.hidden.T, output_delta)
        self.output_layer.biases += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
        self.hidden_layer.weights += learning_rate * np.dot(X.T, hidden_delta)
        self.hidden_layer.biases += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

        
    # Add this to the end of your existing code

# Load and preprocess datafrom tensorflow.keras.datasets import mnist
import numpy as np
from tensorflow import keras
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()


X_train = np.array(X_train) / 255.0
X_test = np.array(X_test) / 255.0

# Convert labels to one-hot encoding
def to_one_hot(y, num_classes):
    return np.eye(num_classes)[y]

y_train = to_one_hot(y_train, 10)
y_test = to_one_hot(y_test, 10)

# Initialize the network
input_size = 784  # 28x28 pixels
hidden_size = 128
output_size = 10  # 10 digits
nn = NeuralNet(input_size, hidden_size, output_size)

# Training
epochs = 50
batch_size = 32
learning_rate = 0.1

for epoch in range(epochs):
    for i in range(0, len(X_train), batch_size):
        X_batch = X_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]
        
        output = nn.forward(X_batch)
        nn.backward(X_batch, y_batch, output, learning_rate)
    
    # Evaluate on test set
    test_output = nn.forward(X_test)
    accuracy = np.mean(np.argmax(test_output, axis=1) == np.argmax(y_test, axis=1))
    print(f"Epoch {epoch+1}/{epochs}, Test Accuracy: {accuracy:.4f}")

# Final evaluation
final_output = nn.forward(X_test)
final_accuracy = np.mean(np.argmax(final_output, axis=1) == np.argmax(y_test, axis=1))
print(f"Final Test Accuracy: {final_accuracy:.4f}")