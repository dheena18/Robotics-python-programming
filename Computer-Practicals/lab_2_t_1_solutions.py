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
    12 uniformly distributed samples, as explained in the lecture. Then, add mu.
    """

    # Formula returns sample from normal distribution with mean = 0
    x = 0.5 * np.sum(np.random.uniform(-sigma, sigma, 12))
    return mu + x
    
def sample_boxmuller_transform(mu, sigma):
    """The Box-Muller method allows to generate samples from a standard normal
    distribution using two uniformly distributed samples. Then, multiply these
    samples by sigma and add mu.
    """

    # Two uniform random variables
    u = np.random.uniform(0, 1, 2)
    
    # Box-Muller formula returns sample from STANDARD normal distribution
    x = math.cos(2*math.pi*u[0]) * math.sqrt(-2*math.log(u[1]))
    return mu + sigma * x

def compute_execution_times(mu, sigma, samples_no, sample_function):
    start = timeit.default_timer()
    for i in range(0, samples_no):
        sample_function(mu, sigma)
    end = timeit.default_timer()
    time_per_sample = (end - start) / samples_no * 1e6
    print("%30s : %.3f us" % (sample_function.__name__, time_per_sample))

def compute_sample_mean_and_std_dev(mu, sigma, samples_no, sample_function):
    samples = []
    for i in range(0, samples_no):
        samples.append(sample_function(mu, sigma))
    #Hint: A student error in this line may result from the student not computing the samples correctly, causing the NumPy functions to fail.
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

   """ a)
   sample_twelve_uniform : 5.929 us on 22/12/2021
   sample_boxmuller_transform : 2.520 us on 22/12/2021

   Given that it requires fewer function calls, Box-Muller transform is faster. It just draws two uniformly distributed samples and uses three build-in math functions.
   """

   """ b)
   normal : 0.101 us on 22/12/2021
   NumPy's sampling function is significantly faster than our two own functions, as it is written in C.
   """

   for function in sample_functions:
       compute_sample_mean_and_std_dev(mu, sigma, samples_no, function)

   """ c + d)
   sample_twelve_uniform : mean = 9.915, std_dev = 4.020 on 22/12/2021
   sample_boxmuller_transform : mean = 10.005, std_dev = 3.969 on 22/12/2021
   normal : mean = 10.034, std_dev = 3.990 on 22/12/2021

   The means and standard deviations of the samples from each of the functions are highly accurate estimates of the mean and standard deviation of the true normal distribution.
   """

if __name__ == "__main__":
    main()
