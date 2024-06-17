import random

# Función de activación escalón
def step_function(x):
    return 1 if x >= 0 else 0

# Clase Neurona
class Neuron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)

    def activate(self, inputs):
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return step_function(weighted_sum)

# Clase Capa
class Layer:
    def __init__(self, num_neurons, num_inputs_per_neuron):
        self.neurons = [Neuron(num_inputs_per_neuron) for _ in range(num_neurons)]

    def forward(self, inputs):
        return [neuron.activate(inputs) for neuron in self.neurons]

# Clase Red Neuronal
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.hidden_layer = Layer(hidden_size, input_size)
        self.output_layer = Layer(output_size, hidden_size)
        self.learning_rate = 0.2

    def forward(self, inputs):
        hidden_output = self.hidden_layer.forward(inputs)
        final_output = self.output_layer.forward(hidden_output)
        return final_output

    def train(self, training_inputs, training_outputs):
        # Paso hacia adelante
        hidden_output = self.hidden_layer.forward(training_inputs)
        output = self.output_layer.forward(hidden_output)

        # Calcular error de salida (capa de salida)
        output_errors = [target - out for target, out in zip(training_outputs, output)]

        # Propagar errores hacia la capa oculta
        hidden_errors = [0] * len(self.hidden_layer.neurons)
        for i, neuron in enumerate(self.output_layer.neurons):
            for j in range(len(neuron.weights)):
                hidden_errors[j] += output_errors[i] * neuron.weights[j]

        # Actualizar pesos y sesgos para la capa de salida
        for i, neuron in enumerate(self.output_layer.neurons):
            for j in range(len(neuron.weights)):
                neuron.weights[j] += self.learning_rate * output_errors[i] * hidden_output[j]
            neuron.bias += self.learning_rate * output_errors[i]

        # Actualizar pesos y sesgos para la capa oculta
        for i, neuron in enumerate(self.hidden_layer.neurons):
            for j in range(len(neuron.weights)):
                neuron.weights[j] += self.learning_rate * hidden_errors[i] * training_inputs[j]
            neuron.bias += self.learning_rate * hidden_errors[i]

# Ejemplo de datos de entrenamiento
training_data = [
    ([0, 0], [0]),
    ([0, 1], [1]),
    ([1, 0], [1]),
    ([1, 1], [0])
]

# Inicializar la red neuronal
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Entrenar la red neuronal
for epoch in range(10000):  # Entrenar por 10000 épocas
    for inputs, target in training_data:
        nn.train(inputs, target)

# Probar la red neuronal
for inputs, target in training_data:
    output = nn.forward(inputs)
    print(f"Entrada: {inputs}, Esperado: {target}, Predicho: {output}")
