from Pyro4 import expose
from functools import reduce


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers
        print("Inited")

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))
        arr = self.read_input()
        step = len(arr) / len(self.workers)

        # map
        mapped = []
        for i in xrange(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(arr[i * step : i * step + step]))

        print 'Map finished: ', mapped

        mapped_values = [result.value for result in mapped]
        
        map_result = self.merge_sorted_arrays(mapped_values)

        #self.write_output(mapped_values)
        
        self.write_output(map_result)
        print("Job Finished")

    @staticmethod
    @expose
    def mymap(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return Solver.mymap(left) + middle + Solver.mymap(right)

    def read_input(self):
        f = open(self.input_file_name, 'r')
        lines = [int(line.rstrip('\n')) for line in f]
        f.close()
        return lines
    
   # def write_output(self, output):
   #     with open(self.output_file_name, 'w') as f:
   #         for sublist in output:
   #             f.write(' '.join(str(num) for num in sublist) + '\n')

    def merge_sorted_arrays(self, arrays):
        merged_array = []
        pointers = [0] * len(arrays)

        while True:
            min_val = float('inf')
            min_index = -1
            for i, arr in enumerate(arrays):
                if pointers[i] < len(arr) and arr[pointers[i]] < min_val:
                    min_val = arr[pointers[i]]
                    min_index = i

            if min_index == -1:
                break

            merged_array.append(min_val)
            pointers[min_index] += 1

        return merged_array



    def write_output(self, output):
        with open(self.output_file_name, 'w') as f:
            f.write(' '.join(str(num) for num in output) + '\n')



    
        