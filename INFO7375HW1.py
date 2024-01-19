class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))
        output = 1 if weighted_sum >= self.threshold else 0
        return output


def main():
    neuron_weights = [0.9, -0.7, 0.2]
    neuron_threshold = 0.3

    neuron = McCullochPittsNeuron(neuron_weights, neuron_threshold)

    input_values_list = [[1, 0, 1],[0,1,0]]


    for input_values in input_values_list:
        output = neuron.activate(input_values)
        print("Input Values:", input_values)
        print("Weights:", neuron_weights)
        print("Treshold:",neuron_threshold)
        print("Output:", output)


if __name__ == "__main__":
    main()
