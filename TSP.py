"""
TSP algo
"""

"""
w(u, v) = nint( sqrt( (x(u) -x(v))^2 + (y(u) -y(v))^2) )
"""
import logging
        

def load_nodes(text_file, list_nodes):
    """Given a text_file where the first line is the number of nodes, load
    a list of tuples in list_nodes.
    There is no exception, so it assumes correct file format
    TODO: add error handling
    """
    logging.info("load_nodes starts with ", [text_file, list_nodes])
    with open(text_file)  as fl:
        size = int(next(fl))
        for n in range(size):
            i , x, y = next(fl).split(' ')
            list_nodes.append((int(x),int(y)))
    return len(list_nodes)


        
