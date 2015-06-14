import random
import util
import numpy as np

class Unit:
    def __init__(self, inputs, outputs, hidden_width, hidden_depth, memory_n):
        self.values = np.zeros((hidden_width, hidden_depth))
        self.hidden_depth = hidden_depth
    #    self.memory = np.zeros(memory_n)

        self.input_hidden_axons = util.random_array_range(inputs, hidden_width)   #input_n X hiddeN_width
        self.hidden_axons = util.random_array3d_sum(hidden_depth - 1, hidden_width, hidden_width, hidden_width)  # hidden_width X hidden_depth
      #  self.hidden_memory_axons = util.random_array_range(hidden_width, memory_n, hidden_depth)    # hidden_width X outputs
      #  self.memory_hidden_axons = util.random_array_range3d(hidden_width, memory_n, hidden_depth)    # hidden_width X memory_n X hidden_depth
        self.hidden_output_axons = util.random_array_range(hidden_width, outputs)    # hidden_width X outputs

    def reset_hidden(self+):
        self.values = np.zeros((hidden_width, hidden_depth))


    def run_hidden(self):
        for i in range(0, self.hidden_depth-1):
            print i
            layer = self.values[:, i]
            print layer
            next_layer = self.values[:, i+1]
            new_values = np.dot(layer, self.hidden_axons[i, :, :])
            self.values[:, i + 1] = np.add(self.values[:, i+1], new_values)

    # def hidden_to_memory(self):
    #     for i in range(0, self.hidden_depth-1):
    #         layer = self.values[:, i]
    #         axons = self.hidden_memory_axons[:, :, i]
    #         new_values = np.dot(layer, axons)
    #         self.memory = np.add(self.memory, new_values)


  #  def memory_to_hidden(self):

    def feed_inputs(self, input_data):
        r = np.dot(input_data, self.input_hidden_axons)
        self.values[:, 0] = r

    def read_outputs(self):
        last = self.values.shape[1] - 1
        r = np.dot(self.values[:, last], self.hidden_output_axons)
        return r

a=Unit(3,5,20,3,10)
i = np.ones((1,3))
a.feed_inputs(i)
a.run_hidden()
