#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:32:18 2019

@author: juanflorez
"""
import TSP

the_dir = {}

def test_read_from_file():
     assert(TSP.load_nodes("test.tsp", the_dir) == 5)
     assert(the_dir[5]==(2,3))
        

def test_distance_from_origen():
    assert(TSP.distance((0,0), (5,0))==5)
    assert(TSP.distance((0,0), (0,5))==5)

def test_dstance_big_numbers():
    origen = (793699,274913)
    destination = (981665,218777)
    assert(TSP.distance(origen, destination) == 196169)
    
def test_nearest_node():
    input_dir = {1:(0,0),2:(20,0),3:(20,10),4:(0,10)}
    distance, node = TSP.nearest_node(3,input_dir,[4])
    assert(2 == node)
    assert(10 == distance)




def test_tsp_impl():
    input_dir = {1:(0,0),2:(20,0),3:(20,10),4:(0,10)}
    output_list = []
    total_dist = TSP.tsp_impl(input_dir, output_list, start=1)
    assert(output_list == [1, 4, 3, 2])

    
test_tsp_impl()
