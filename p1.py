import csv
import random
import math

# Función para cargar el dataset Iris
def load_iris_dataset(filename):
    X = []
    y = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Saltar la cabecera
        for row in csvreader:
            X.append([float(x) for x in row[:-1]])
            if row[-1] == 'Iris-setosa':
                y.append([1, 0, 0])
            elif row[-1] == 'Iris-versicolor':
                y.append([0, 1, 0])
            else:
                y.append([0, 0, 1])
    return X, y

# Función de activación sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la función sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Función softmax
def softmax(x):
    exp_x = [math.exp(i) for i in x]
    sum_exp_x = sum(exp_x)
    return [i / sum_exp_x for i in exp_x]

# Función de pérdida de entropía cruzada
def cross_entropy_loss(y_pred, y_true):
    return -sum([y_true[i] * math.log(y_pred[i]) for i in range(len(y_true))])

# Inicialización de pesos y sesgos
def initialize_weights(n_inputs, n_hidden, n_outputs):
    W1 = [[random.uniform(-1, 1) for _ in range(n_hidden)] for _ in range(n_inputs)]
    b1 = [0 for _ in range(n_hidden)]
    W2 = [[random.uniform(-1, 1) for _ in range(n_outputs)] for _ in range(n_hidden)]
    b2 = [0 for _ in range(n_outputs)]
    return W1, b1, W2, b2

# Propagación hacia adelante
def forward_propagation(X, W1, b1, W2, b2):
    z1 = [sum(X[i] * W1[i][j] for i in range(len(X))) + b1[j] for j in range(len(b1))]
    a1 = [sigmoid(z) for z in z1]
    z2 = [sum(a1[j] * W2[j][k] for j in range(len(a1))) + b2[k] for k in range(len(b2))]
    a2 = softmax(z2)
    return a1, a2

# Propagación hacia atrás y actualización de pesos y sesgos
def backpropagation(X, y, a1, a2, W1, b1, W2, b2, learning_rate):
    dz2 = [a2[i] - y[i] for i in range(len(y))]
    dW2 = [[a1[j] * dz2[k] for k in range(len(dz2))] for j in range(len(a1))]
    db2 = dz2
    dz1 = [sum(dz2[k] * W2[j][k] for k in range(len(dz2))) * sigmoid_derivative(a1[j]) for j in range(len(a1))]
    dW1 = [[X[i] * dz1[j] for j in range(len(dz1))] for i in range(len(X))]
    db1 = dz1

    # Actualización de pesos y sesgos
    W1 = [[W1[i][j] - learning_rate * dW1[i][j] for j in range(len(W1[0]))] for i in range(len(W1))]
    b1 = [b1[j] - learning_rate * db1[j] for j in range(len(b1))]
    W2 = [[W2[j][k] - learning_rate * dW2[j][k] for k in range(len(W2[0]))] for j in range(len(W2))]
    b2 = [b2[k] - learning_rate * db2[k] for k in range(len(b2))]

    return W1, b1, W2, b2

# Función de entrenamiento
def train(X, y, epochs, learning_rate):
    n_inputs = len(X[0])
    n_hidden = 4
    n_outputs = 3
    W1, b1, W2, b2 = initialize_weights(n_inputs, n_hidden, n_outputs)

    for epoch in range(epochs):
        total_loss = 0
        for i in range(len(X)):
            a1, a2 = forward_propagation(X[i], W1, b1, W2, b2)
            total_loss += cross_entropy_loss(a2, y[i])
            W1, b1, W2, b2 = backpropagation(X[i], y[i], a1, a2, W1, b1, W2, b2, learning_rate)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {total_loss / len(X)}")

    return W1, b1, W2, b2, epoch

# Cargar y preparar el dataset
X, y = load_iris_dataset('Iris.csv')

# Entrenar la red neuronal
W1, b1, W2, b2, epochs = train(X, y, epochs=1000, learning_rate=0.4)

print(f"La red neuronal requirió {epochs} épocas para entrenar.")
