"""
TSP algo
"""

import logging
from math import sqrt
 
        

def load_nodes(text_file, dir_nodes):
    """Given a text_file where the first line is the number of nodes, load
    a list of tuples in list_nodes.
    There is no exception, so it assumes correct file format
    TODO: add error handling
    TODO: use named tuple
    """
    logging.info("load_nodes starts with ", [text_file, dir_nodes])
    with open(text_file)  as fl:
        size = int(next(fl))
        for n in range(size):
            i , x, y = next(fl).split(' ')
            dir_nodes[int(i)]=(float(x),float(y))
    return len(dir_nodes)


        
def distance(origen, destination):
    """ takes two tuplas and calculates the distance using
        w(u, v) = nint( sqrt( (x(u) -x(v))^2 + (y(u) -y(v))^2) )
    """
    return round( sqrt( (origen[0] - destination[0])**2 + 
                     (origen[1] -destination[1])**2) )
    

def tsp_impl(input_dir, output_list, start=1):
    """ takes input_dir, and gives a sorted list with the nodes visited in 
    order """
    
    logging.info("tsp_impl with starts")
    output_list.insert(0,start)
    
        
    
    for point in input_dir:
        min_dist = curr_dis = 598989898
        nearest_node_index = 0
 
        if (point in output_list):
            continue
        for index, node in enumerate(output_list):
            curr_dis = distance(input_dir[node], input_dir[point])
            print("round {} trying node {} ".format(index, node ))
            if curr_dis < min_dist:
                min_dist = curr_dis
                nearest_node_index = index
        output_list.insert(nearest_node_index+1,point)
        
            