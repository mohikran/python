from numpy import exp, array, random, dot


class NeuronalNetwork(): 
	def __init__ (self):
		random.seed(1) #fixe les aleatoires
		self.synaptic_weights = 4 * random.random((3, 1)) - 1 #acune idee du pourquoi du *

	def __sigmoid (self, x):
		return 1 / (1 + exp(-x))

	def __derivate(self, x):
		return x * (1-x)

	def training (self, neuralinputs, neuraloutputs, numberofvalues ):
		for iteration in xrange(numberofvalues):
			outputCalc = self.think(neuralinputs)       
			error = neuraloutputs - outputCalc
			adjustment = dot(neuralinputs.T, error * self.__derivate(outputCalc))
			self.synaptic_weights += adjustment

    # The neural network thinks.
	def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
		return self.__sigmoid(dot(inputs, self.synaptic_weights))




if __name__ == "__main__":
	neural_network = NeuronalNetwork()
	print "Random starting synaptic weights: "
	print neural_network.synaptic_weights
	input2 = array([[1, 1, 1], [1, 1, 0], [0, 0, 0], [0, 1, 0]])
	output2 = array([[0,0,0,1]]).T #Penser a la transposee la dessus sinon ne passe pas
	neural_network.training(input2, output2, 10000)
	print "New synaptic weights after training: "
	print neural_network.synaptic_weights

	print "Considering new situation [1, 1, 1] -> ?: "
	print neural_network.think(array([1, 1, 1]))

	