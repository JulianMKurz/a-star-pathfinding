#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:05:42 2017

@author: julian kurz
"""

import heapq
import random

class ActionsLookedAt:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def leng(self):
        return len(self.elements)
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
        
    def get(self):
        return heapq.heappop(self.elements)[1]
    

    

heuristic_1 = lambda x,y: abs(y[0]-x[0])+abs(y[1]-x[1])


def get_neighbours(d2space, node):
    result = []
    if(node[0] + 1 < 20 and d2space[node[0]+1][node[1]] != "O"):
        result.append((node[0]+1, node[1]))
        
    if(node[0] - 1 >= 0 and d2space[node[0]-1][node[1]] != "O"):
        result.append((node[0]-1, node[1]))
        
    if(node[1] + 1 < 20 and d2space[node[0]][node[1]+1] != "O"):
        result.append((node[0], node[1]+1))
        
    if(node[1] - 1 >= 0 and d2space[node[0]][node[1]-1] != "O"):
        result.append((node[0], node[1]-1))
        
    return result
            

        

def a_star(d2space, start, goal, heuristic):
    nodes_opened = ActionsLookedAt()
    start_node = start
    nodes_opened.put(start_node, heuristic(start_node, goal))
    precessor = {}
    cost_so_far = {}
    precessor[start_node] = []
    cost_so_far[start_node] = 0
    all_nodes = []
    
    d2space[start[0]][start[1]] = "S"
    
    while not nodes_opened.empty():
        current_node = nodes_opened.get()
        
        if current_node == goal:
            result = []
            precessing_node = current_node
            while True:
                result.insert(0, precessing_node)
                
                precessing_node = precessor[precessing_node]
                
                if precessing_node == []:
                    break
            d2space[goal[0]][goal[1]] = "G"
            print("-------------------------------------------------")
            for i in range(0,20):
                print(d2space[i])
            print("Best Path: ")
            print(result)
            print("All Nodes looked at: ")
            print(all_nodes)
            break
        
        for neighbour_node in get_neighbours(d2space,current_node):
            new_cost = cost_so_far[current_node] + 1
            
           
            if (neighbour_node not in cost_so_far or new_cost < cost_so_far[neighbour_node]):
               cost_so_far[neighbour_node] = new_cost
               priority = new_cost + heuristic(neighbour_node, goal)
               nodes_opened.put(neighbour_node, priority)
               precessor[neighbour_node] = current_node
               d2space[neighbour_node[0]][neighbour_node[1]] = str(new_cost)
               all_nodes.append(neighbour_node)
    
    return precessor, cost_so_far


randomArtifacts = []

for i in range (0,80):
    randomArtifacts.extend("O")

for i in range(0,320):
    randomArtifacts.extend("f")
    
random.shuffle(randomArtifacts)

d2space = [];
counter = 0;

for i in range(0,20):
    temp = []
    for n in range(0,20):
        temp.extend(randomArtifacts[counter])
        counter += 1
        
    d2space.append(temp)
    
    
for i in range(0,20):
    print(d2space[i])
    
a_star(d2space, (1,1), (13,17), heuristic_1)