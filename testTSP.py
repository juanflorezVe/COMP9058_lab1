#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:32:18 2019

@author: juanflorez
"""
import TSP

def test_read_from_file():
        the_list = []
        assert(TSP.load_nodes("test.tsp", the_list) == 5)
        assert(the_list[-1]==(2,3))