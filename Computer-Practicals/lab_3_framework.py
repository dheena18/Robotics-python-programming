#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

""" T 1 -- Prediction with a Discrete Bayes Filter
a)
"""

plt.ion()

def discrete_filter(bel, d):
    """ Parameters:
    bel = [cell_0, ... , cell_19]
    d = "f" for move forward and "b" for move backward
    """
    bel_prime = np.zeros(bel.shape[0])

    '''Please insert your code here.'''
    '''***              ***'''




    return bel_prime

def plot_and_save(bel, i):
    plt.cla()
    plt.bar(range(0,bel.shape[0]),bel,width=1.0)
    plt.axis([0,bel.shape[0]-1,0,1])
    plt.draw()
    plt.savefig("belief_at_time_step_" + str(i) + ".pdf")
    plt.pause(1)

def main():
    bel = np.hstack((np.zeros(11),1,np.zeros(8)))
    
    plt.figure()
    plt.ion()
    plt.show()
    
    move_forward_no = 8
    move_backward_no = 3
    
    for i in range(0,move_forward_no):
        plot_and_save(bel, i)
        bel = discrete_filter(bel,"f")
        print("Total belief sums up to", np.sum(bel))
        
    for i in range(0,move_backward_no):
        plot_and_save(bel, move_forward_no + i)
        bel = discrete_filter(bel,"b")
        print("Total belief sums up to", np.sum(bel))

    plot_and_save(bel, move_forward_no + move_backward_no)
        
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
