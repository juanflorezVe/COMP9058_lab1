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
    

    
 