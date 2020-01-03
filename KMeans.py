# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:11:00 2019

@author: Toprak
"""

import numpy as np
import pandas as pd
import random


def center_init(n,X):
    rand_point = random.sample(range(0, len(X)), n)    
    centers = []    
    for i in rand_point:
        centers.append(X[i])
    return centers

def find_cluster(a):
    return a.index(min(a))
 
def new_center(clusters,X,n):
    sums = np.zeros((n, len(X[0])))
    
    for i,j in zip(clusters,X):
        sums[i] += j
    return sums / len(X)

def center_distance(X,centers):
    all_dist = []
    tmp_dist = []
    for i in range(len(X)):
        for j in range(n):
            dist = np.linalg.norm(centers[j]-X[i])
            tmp_dist.append(dist)
        all_dist.append(tmp_dist)
        tmp_dist = []
    return all_dist

def append_cluster(all_dist):
    clusters = []    
    for i in all_dist:
        clusters.append(find_cluster(i))
    return clusters

def KMeans(n,X,iter_count):
    centers = center_init(n,X)
    for i in range(iter_count):
        all_dist = center_distance(X,centers)
        clusters = append_cluster(all_dist)        
        centers = new_center(clusters,X,n)        
    return clusters


n = 2

A = np.asarray([[0,0],[1,1],[1,2],[1.5,1.5],[10,0],[7,8],[5,5],[5,4]])

Clusters = KMeans(n,A,25)

print(Clusters)             # [1, 1, 1, 1, 0, 0, 0, 0]
