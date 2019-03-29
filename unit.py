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
        self.memory = memory_n
        #self.memory_values = np.zeros(memory_n)
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
        self.hidden_axons = util.random_array_range3d(self.hidden_depth - 1, self.hidden_width, self.hidden_width)  # hidden_width X hidden_depth
          #  self.hidden_memory_axons = util.random_array_range(hidden_width, memory_n, hidden_depth)    # hidden_width X outputs
         #  self.memory_hidden_axons = util.random_array_range3d(hidden_width, memory_n, hidden_depth)    # hidden_width X memory_n X hidden_depth
        self.hidden_output_axons = util.random_array_range(self.hidden_width, self.outputs)    # hidden_width X outputs

    def serialize(self):
        r = 64
        io_digits = 2
        hidden_digits = 3
        memory_digits = 2
        g = {}
        g['inputs'] = util.change_base(self.inputs, io_digits, r)
        g['outputs'] = util.change_base(self.outputs, io_digits, r)
        g['hidden_width'] = util.change_base(self.hidden_width, hidden_digits, r)
        g['hidden_depth'] = util.change_base(self.hidden_depth, 1, r)
        g['memory'] = util.change_base(self.memory, memory_digits, r)
        g['hidden_axon_weights'] = np.rint( 2d_neg_array_to_pos_1d(self.hidden_axons, r) )
        g['hidden_axon_weights'] = np.rint(np.multiply(self.hidden_axons.flatten(), r*2))
        g['input_hidden_weights'] = np.rint(np.multiply(self.input_hidden_axons.flatten(), r*2))
        g['hidden_output_weights'] = np.rint(np.multiply(self.hidden_output_axons.flatten(), r*2))
        b = np.append(g['hidden_axon_weights'], g['input_hidden_weights'])
        b = np.append(b, g['hidden_output_weights'])
        return b

    def read_serialize(self, genome):
        r = 64
        io_digits = 2
        hidden_digits = 3
        memory_digits = 2

        self.inputs = util.base_to_n(genome[0:io_digits], r)
        self.outputs = util.base_to_n(genome[io_digits: io_digits * 2], r)
        self.hidden_width = util.base_to_n(genome[io_digits*2 : hidden_digits + io_digits*2 ], r)
        self.hidden_depth = genome[io_digits*2 + hidden_digits]
        self.memory = uti.base_to_n(genome[ io_digits * 2 + 1 + hidden_digits: io_digits * 2 + 1 + hidden_digits * 2], r)
        self.hidden_axons =
        self.input_hidden_axons =
        self.hidden_output_axons = 


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


a=Unit(3, 5, 20, 3, 10)
i = np.ones((1, 3))
c = a.serialize()
#b=a.run(i)
