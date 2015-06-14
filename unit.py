import random
import util
import numpy as np

class Unit:
    def __init__(self, inputs, outputs, hidden_width, hidden_depth, memory_n):
        self.values = np.zeros((hidden_width, hidden_depth))
        self.hidden_depth = hidden_depth
        self.hidden_width = hidden_width
        self.inputs = inputs
        self.outputs = outputs
    #    self.memory = np.zeros(memory_n)
        self.randomize()

    def reset_hidden(self):
        self.values = np.zeros((self.hidden_width, self.hidden_depth))

    def run_hidden(self):
        for i in range(0, self.hidden_depth-1):
            layer = self.values[:, i]
            next_layer = self.values[:, i+1]
            new_values = np.dot(layer, self.hidden_axons[i, :, :])
            self.values[:, i + 1] = np.add(self.values[:, i+1], new_values)
            for a in range(0, self.hidden_width):
                self.values[a, i + 1] = util.logistic(self.values[a, i+1])

    # def hidden_to_memory(self):
    #     for i in range(0, self.hidden_depth-1):
    #         layer = self.values[:, i]
    #         axons = self.hidden_memory_axons[:, :, i]
    #         new_values = np.dot(layer, axons)
    #         self.memory = np.add(self.memory, new_values)

  #  def memory_to_hidden(self):

    def randomize(self):
        self.input_hidden_axons = util.random_array_range(self.inputs, self.hidden_width)   #input_n X hiddeN_width
        self.hidden_axons = util.random_array3d_sum(self.hidden_depth - 1, self.hidden_width, self.hidden_width, self.hidden_width)  # hidden_width X hidden_depth
          #  self.hidden_memory_axons = util.random_array_range(hidden_width, memory_n, hidden_depth)    # hidden_width X outputs
         #  self.memory_hidden_axons = util.random_array_range3d(hidden_width, memory_n, hidden_depth)    # hidden_width X memory_n X hidden_depth
        self.hidden_output_axons = util.random_array_range(self.hidden_width, self.outputs)    # hidden_width X outputs

    def serialize(self):
        

    def read_serialize(self):


    def feed_inputs(self, input_data):
        r = np.dot(input_data, self.input_hidden_axons)[0]
        r = util.logisticize_array(r)
        self.values[:, 0] = r

    def read_outputs(self):
        last = self.values.shape[1] - 1
        r = np.dot(self.values[:, last], self.hidden_output_axons)
        r = util.logisticize_array(r)
        for i in range(0, self.outputs):
            r[i] = util.logistic(r[i])
        return r

    def run(self, input_data):
        self.feed_inputs(input_data)
        self.run_hidden()
        a = self.read_outputs()
        self.reset_hidden()
        return a


a=Unit(3,5,20,3,10)
i = np.ones((1,3))

b=a.run(i)
