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
    #Initialize new belief with zeros.
    bel_prime = np.zeros(bel.shape[0])

    #True, if the robot executed "move forward" action
    if d=="f":
        #Update the old belief for all cells
        for x in range(bel.shape[0]):
            #Cache old belief two cells backward relative to the robot
            if x >= 2:
                bel2 = bel[x-2]
            #Zero padding if the robot is located at the second cell
            else:
                bel2 = 0
            #Cache old belief in the last cell relative to the robot
            if x >= 1:
                bel1 = bel[x-1]
            #Zero padding if the robot is located at the first cell             
            else:
                bel1 = 0
            #Cache old belief in the cell where the robot is located
            bel0 = bel[x]

            #True, if the robot is not located at the last cell
            if x < bel.shape[0]-1:
                #Compute new belief by convolving the old belief with the regular motion model
                bel_prime[x] = 0.20 * bel2 + 0.60 * bel1 + 0.20 * bel0
            #True, if the robot is located at the last cell
            elif x == bel.shape[0]-1:
                #Compute new belief by convolving the old belief with the regular motion model and the special motion models for the last two cells
                bel_prime[x] = 0.20 * bel2 + 0.80 * bel1 + 1.00 * bel0

    #True, if the robot executed "move backward" action
    if d=="b":
        #Update the old belief for all cells
        for x in range(bel.shape[0]):
            #Cache old belief two cells forward relative to the robot
            if x < bel.shape[0]-2:
                bel2 = bel[x+2]
            #Zero padding if the robot is located at the second to last cell
            else:
                bel2 = 0
            #Cache old belief in the next cell relative to the robot
            if x < bel.shape[0]-1:
                bel1 = bel[x+1]
            #Zero padding if the robot is located at the last cell             
            else:
                bel1 = 0
            #Cache old belief in the cell where the robot is located                
            bel0 = bel[x]

            #True, if the robot is not located at the first cell
            if x > 0:
                #Compute new belief by convolving the old belief with the motion model
                bel_prime[x] = 0.20 * bel2 + 0.60 * bel1 + 0.20 * bel0
            #True, if the robot is located at the first cell
            elif x == 0:
                #Compute new belief by convolving the old belief with the regular motion model and the special motion models for the first two cells
                bel_prime[x] = 0.20 * bel2 + 0.80 * bel1 + 1.00 * bel0

    #Return the belief that results from the prediction step
    return bel_prime

""" b)
The first prediction step shifts the peak of the distribution one cell to the right and spreads out its width one cell on each side.
"""

def plot_and_save(bel, i):
    plt.cla()
    plt.bar(range(0,bel.shape[0]),bel,width=1.0)
    plt.axis([0,bel.shape[0],0,1])
    plt.draw()
    plt.savefig("belief_at_time_step_" + str(i) + ".pdf")
    plt.pause(1)

""" c)
During this period, the peak of the distribution shifts from left to right. The spread of the distribution to the left of the peak increases, while more and more probability mass to the right of the peak is accumulates in the last cell. The reason for this accumulation is that the world is bounded.
"""

""" d)
During this period, the peak of the distribution shifts from right to left. The spread of the distribution increases on both sides of the peak. The reason for this is that the robot is geared away from the boundaries of the world.
"""
    
""" e)
Changing the errors increases the "smoothing" effect of convolving the belief with the motion model.
"""
    
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
