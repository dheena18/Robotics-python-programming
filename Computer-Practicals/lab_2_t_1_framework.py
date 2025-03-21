#!/usr/bin/env python

import numpy as np
import math
import timeit

"""
T 1 -- Sample From a Normal Distribution
mu -- mean of the normal distribution
sigma -- std_dev of the normal distribution
"""

def sample_twelve_uniform(mu, sigma):
    """Generate samples from a zero-centered normal distribution by summing up
    12 uniform distributed samples, as explained in the lecture. Then, add mu.
    """

    '''Please insert your code here and remove pass.'''
    '''***              ***'''
    pass

def sample_boxmuller_transform(mu, sigma):
    """The Box-Muller method allows to generate samples from a standard normal
    distribution using two uniformly distributed samples. Then, multiply these
    samples by sigma and add mu.
    """

    '''Please insert your code here and remove pass.'''
    '''***              ***'''
    pass
    
def compute_execution_times(mu, sigma, samples_no, sample_function):
    start = timeit.default_timer()
    for i in range(samples_no):
        sample_function(mu, sigma)
    end = timeit.default_timer()
    time_per_sample = (end - start) / samples_no * 1e6
    print("%30s : %.3f us" % (sample_function.__name__, time_per_sample))

def compute_sample_mean_and_std_dev(mu, sigma, samples_no, sample_function):
    samples = []
    for i in range(samples_no):
        samples.append(sample_function(mu, sigma))
    print("%30s : mean = %.3f, std_dev = %.3f" % (sample_function.__name__, np.mean(samples), np.std(samples)))

def main():
   mu, sigma = 10.0, 4.0

   samples_no = 10000

   sample_functions = [
       sample_twelve_uniform,
       sample_boxmuller_transform,
       np.random.normal
       ]

   print("Computing execution times as well as sample means and std_devs with:" )
   print(" mean :", mu)
   print(" std_dev :", sigma)
   print(" samples no:", samples_no)
   
   for function in sample_functions:
       compute_execution_times(mu, sigma, samples_no, function)

   for function in sample_functions:
       compute_sample_mean_and_std_dev(mu, sigma, samples_no, function)

if __name__ == "__main__":
    main()

