"""
TSP algo
"""
import random
import logging
import sys
from math import sqrt, inf


 
        

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


def nearest_node(index, dictionary, visited_list):
    """ returns the nearest node to the dictionary[index] in the
        dictionary avoiding the nodes from the visited_list
    """
    min_dis = inf
    closest_node = index
    for d_node in dictionary:
        if d_node == index:
            continue
        elif d_node in visited_list:
            continue
        
        current_distance = distance(dictionary[index], dictionary[d_node])
        if 0 < current_distance < min_dis:
            min_dis = current_distance
            closest_node = d_node
    
    return min_dis, closest_node

        


def tsp_impl(input_dir, output_list, start=1):
    """ takes input_dir, and gives a sorted list with the nodes visited in 
    order """
    
    logging.info("tsp_impl with starts")
    output_list.append(start)
    cycle_lenght = 0
    o_point = start
    
    while(len(output_list) < len(input_dir)):
        
        distance, index = nearest_node(o_point, input_dir, output_list)
       
        output_list.append(index)
        cycle_lenght += distance
        o_point = index
    
    return cycle_lenght

def main(args):
    
    if len(args) < 2:
        print("ERROR, you need 2 arguments")
        print(" you entered {} ".format(len(args)))
        print(args)
        pass
    
    elif len(args) > 2:
        print("WARNING, too many arguments ")

    dir_nodes ={}
    out_list  =[]
    total_dist = 0
    
    load_nodes(args[0], dir_nodes)
    total_dist = tsp_impl(dir_nodes, out_list, start=random.randint(1,len(dir_nodes)))
  
    with open(args[1], 'w') as out:
        out.write('{}\n'.format(total_dist))
        for nd in out_list:
            out.write('{}\n'.format(nd))
    
    print("Done")
    
        
    
    

if __name__ == '__main__':
    main(sys.argv[1:])

