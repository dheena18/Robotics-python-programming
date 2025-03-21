#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt

#global variable counter
counter = 1

""" T 2 -- Sample Odometry Motion Model
a)
"""

def sample_odometry_motion_model(x, u, a):
    """ Parameters:
    [x[0],x[1],x[2]] = [x, y, theta]
    [u[0],u[1],u[2]] = [rot1, trans, rot2]
    [a[0],a[1],a[2],a[3]] = [a1, a2, a3, a4]
    """
    #Compute "corrupted" initial rotation
    delta_hat_r1 = u[0] + np.random.normal(0, a[0]*abs(u[0]) + a[1]*abs(u[1]))
    #Compute "corrupted" forward movement
    delta_hat_t = u[1] + np.random.normal(0, a[2]*abs(u[1]) + a[3]*(abs(u[0])+abs(u[2])))
    #Compute "corrupted" final rotation
    delta_hat_r2 = u[2] + np.random.normal(0, a[0]*abs(u[2]) + a[1]*abs(u[1]))

    #Predict new x-position of robot
    x_prime = x[0] + delta_hat_t * math.cos(x[2] + delta_hat_r1)
    #Predict new y-position of robot
    y_prime = x[1] + delta_hat_t * math.sin(x[2] + delta_hat_r1)
    #Predict new orientation of robot
    theta_prime = x[2] + delta_hat_r1 + delta_hat_r2

    #Return sampled new pose of robot
    return np.array([x_prime, y_prime, theta_prime])

# b)

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

""" c)
Each evaluation will returns a different value because the model corrupts the odometry readings with random numbers (noise)
"""

""" d)
Changing the noise parameters increases the rotational uncertainty in the robot's movement
"""
    
""" e)
Changing the noise parameters increases the translational uncertainty in the robot's movement (and decreases the uncertainty in the direction of the robot's movement)
"""
    
def main():
    x = [2, 4, 0]
    u = [np.pi/2, 1, 0]
    a = [0.05, 0.05, 0.01, 0.01]
    
    samples_no = 5000
    x_prime = np.zeros([samples_no, 3])

    for i in range(0, samples_no):
        x_prime[i,:] = sample_odometry_motion_model(x,u,a)
    plot_and_save(x, x_prime)

    a = [0.1, 0.1, 0.01, 0.01]

    for i in range(0, samples_no):
        x_prime[i,:] = sample_odometry_motion_model(x,u,a)
    plot_and_save(x, x_prime)

    a = [0.01, 0.01, 0.05, 0.05]

    for i in range(0, samples_no):
        x_prime[i,:] = sample_odometry_motion_model(x,u,a)
    plot_and_save(x, x_prime)
    
if __name__ == "__main__":
    main()
