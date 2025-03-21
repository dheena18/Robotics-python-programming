#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
#import pdb


# Task 1

# Function definition 
def normal_distribution(x, mu, sigma):
   out = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )
   return out

""" a) Mean and standard deviation
 Mean: mu = 0.0
 Standard deviation: sigma = 1.0
"""

""" b) Prefactor
 The prefactor \frac{1}{\sigma\sqrt{2\pi}} ensures that the total area under the curve p(x) is equal to one
"""

""" c) Type of probability distribution
 Normal (Gaussian) distribution
"""

# important!
#pdb.set_trace()


# Task 2

#Plot and store helper function
def plot_and_save(x, y, mu, sigma):
    plt.plot(x, y)
    plt.grid()
    plt.ylabel('p(x)')
    plt.xlabel('x')
    plt.savefig('normal_distribution_' + str(int(mu)) + '_' + str(int(sigma)) + '.png')
    plt.show()   

def main():    
    # a) plot function for mu = 0.0 and sigma = 1.0
    mu, sigma = 0.0, 1.0
    
    # create vector for x
    x = np.linspace(-6, 6, 100, endpoint=True)
    print(x)

    # call the function
    y = normal_distribution(x, mu, sigma)

    # plot and store the data
    plot_and_save(x, y, mu, sigma)

    # b) plot function for mu = 0.0 and sigma = 2.0
    mu, sigma = 0.0, 2.0

    x = np.linspace(-6, 6, 100, endpoint=True)
    print(x)

    # call the function
    y = normal_distribution(x, mu, sigma)

    # plot and store the data
    plot_and_save(x, y, mu, sigma)

    # Main effect: changing the standard deviation spreads out the width of the curve p(x) along the x-axis

    # c) Comment on the effect of mu = 2.0 and sigma = 1.0
    mu, sigma = 1.0, 1.0

    x = np.linspace(-6, 6, 100, endpoint=True)
    print(x)

    # call the function
    y = normal_distribution(x, mu, sigma)

    # plot and store the data
    plot_and_save(x, y, mu, sigma)

    # Main effect: changing the mean shifts the entire curve p(x) on the x-axis one to the right

    # Task 3

    """ e) fix random seed
    The generated sample sets are exactly the same each time we call np.random.normal or np.random.uniform
    """
    np.random.seed(123)

    # a) normal distribution
    mu, sigma = 10.0, 4.0
    normal_vector = np.random.normal(mu, sigma, 1000000)

    # b) uniform distribution
    uniform_vector = np.random.uniform(0, 20, 1000000)

    # c) print mean and std. dev.
    print(np.mean(normal_vector), np.std(normal_vector))
    #mean = 10.002518005229152, std_dev = 4.0010342144083895 on 22/12/2021
    print(np.mean(uniform_vector), np.std(uniform_vector))
    #mean = 10.006317464059229, std_dev = 5.7702971905687779 on 22/12/2021
    
    #Both sample sets have the same mean but different standard deviations. Although both samples cover most of the same interval, the samples of the normal distribution cluster around the central peak, which is why their standard deviation is smaller.

    # d) plot
    plt.figure()
    _, bins, _ = plt.hist(uniform_vector, 100, None, True)
    plt.plot(bins, np.ones_like(bins)*0.05, linewidth=2, color='r')

    plt.figure()
    _, bins, _ = plt.hist(normal_vector, 100, None, True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
    plt.show()

if __name__ == "__main__":
    main()

