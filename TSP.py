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
    

