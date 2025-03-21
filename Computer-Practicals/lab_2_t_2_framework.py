#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt

#global variable counter
counter = 1

""" T 2 -- Sample Odometry Motion Model
"""

def sample_odometry_motion_model(x, u, a):
    """ Parameters:
    [x[0],x[1],x[2]] = [x, y, theta]
    [u[0],u[1],u[2]] = [rot1, trans, rot2]
    [a[0],a[1],a[2],a[3]] = [a1, a2, a3, a4]
    """

    '''Please insert your code here and remove pass.'''
    '''***              ***'''
    pass

def plot_and_save(x, x_prime):
    global counter
    plt.plot(x[0], x[1], "bo")
    plt.plot(x_prime[:,0], x_prime[:,1], "r,")
    plt.xlim([1, 3])
    plt.ylim([3.75, 5.25])
    axes = plt.gca()
    axes.set_aspect('equal')
    plt.xlabel("x-position")
    plt.ylabel("y-position")
    plt.savefig("samples_from_odometry_" + str(counter) + ".pdf")
    counter += 1
    plt.show()
    
def main():
    x = [0, 0, 0]
    u = [0, 0, 0]
    a = [0, 0, 0, 0]
    
    samples_no = 0
    
    x_prime = np.zeros([samples_no, 3])
    for i in range(0, samples_no):
        x_prime[i,:] = sample_odometry_motion_model(x,u,a)

    plot_and_save(x, x_prime)

if __name__ == "__main__":
    main()
