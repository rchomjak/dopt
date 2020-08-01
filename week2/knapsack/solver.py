#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    ### important start
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity_in = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    ### important end
    tab = [ [0] * (item_count + 1) for i in range(0, capacity_in + 1)]
    
    def O(k, j):

        if (j == 0):
            tab[k][j] = 0

        elif items[j - 1].weight <= k:

            tab[k][j] = max(tab[k][j-1], items[j-1].value + tab[k - items[j-1].weight][j-1])
        else:
            tab[k][j] = tab[k][j-1] 
    
    for j in range(0, len(items)+1):
        for k in range(0, capacity_in + 1):
            O(k, j)
        #print(items[j-1])
    """
    for idx, j in enumerate(tab):
        print(idx, j)
    print("----------")
    """

    """
    for item in items:
        for capacity in range(0, capacity_in + 1):

            if  capacity < item.weight:
                tab[capacity][item.index + 1] = tab[capacity][item.index]
            else:
                #print (capacity, capacity - item.weight)
                if (tab[capacity - item.weight][item.index] + item.value > 
                    tab[capacity][item.index]):
                        tab[capacity][item.index  + 1] =  tab[capacity - item.weight][item.index] + item.value
                else:
                    tab[capacity][item.index + 1] = tab[capacity][item.index]
    """
    """
    for idx, j in enumerate(tab):
        print(idx, j)
    print("----------")
    """

    taken = [0] * len(items)
    value = 0
    row = capacity_in
    col = len(items) 
    while row != 0 and col != 0:
        #print(row, col)
        #print(items[col-1])
        if tab[row][col] == tab[row][col - 1]:
            col -= 1
        else:
            
            value = value + items[col-1].value
            taken[items[col - 1].index]= 1
            row -= items[col - 1].weight 
            col -= 1
            
    #print(taken)


    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    """
    value = 0
    weight = 0
    taken = [0]*len(items)
    items.sort(key=lambda x: x.value/x.weight)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    """
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

