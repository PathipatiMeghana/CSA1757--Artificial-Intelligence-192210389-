import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights1 = [[random.random() for _ in range(self.hidden_size)] for _ in range(self.input_size)]
        self.bias1 = [0 for _ in range(self.hidden_size)]
        
        self.weights2 = [[random.random() for _ in range(self.output_size)] for _ in range(self.hidden_size)]
        self.bias2 = [0 for _ in range(self.output_size)]
    
    def forward(self, X):
        self.a1 = []
        for i in range(self.hidden_size):
            self.a1.append(sigmoid(sum(X[j] * self.weights1[j][i] for j in range(self.input_size)) + self.bias1[i]))
        
        self.output = []
        for i in range(self.output_size):
            self.output.append(sigmoid(sum(self.a1[j] * self.weights2[j][i] for j in range(self.hidden_size)) + self.bias2[i]))
        
        return self.output
    
    def backward(self, X, y, learning_rate):
        output_error = [y[i] - self.output[i] for i in range(self.output_size)]
        d_output = [output_error[i] * sigmoid_derivative(self.output[i]) for i in range(self.output_size)]
        
        hidden_error = [sum(d_output[i] * self.weights2[j][i] for i in range(self.output_size)) for j in range(self.hidden_size)]
        d_hidden = [hidden_error[i] * sigmoid_derivative(self.a1[i]) for i in range(self.hidden_size)]
        
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                self.weights2[j][i] += self.a1[j] * d_output[i] * learning_rate
            self.bias2[i] += d_output[i] * learning_rate
        
        for i in range(self.hidden_size):
            for j in range(self.input_size):
                self.weights1[j][i] += X[j] * d_hidden[i] * learning_rate
            self.bias1[i] += d_hidden[i] * learning_rate
    
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
            if epoch % 1000 == 0:
                loss = sum((y[i] - self.output[i]) ** 2 for i in range(self.output_size)) / len(y)
                print(f'Epoch {epoch} Loss: {loss}')

X = [0, 0]
y = [0]

nn = NeuralNetwork(2, 4, 1)
nn.train(X, y, epochs=10000, learning_rate=0.1)
