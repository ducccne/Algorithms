'''
    Particle Swarm Optimization (PSO) Algorithm Implementation
1. Overview
    PSO is a population-based optimization algorithm inspired by how birds or fish move together to find food.
    Each particle represents a possible solution.
    Particles move through the search space using their own experience and the experience of the entire swarm.
    Goal: Find the best solution to a given optimization problem.
2. Algorithm Steps
    a. Initialize a swarm of particles with random positions and velocities.
    b. Evaluate the objective function for each particle.
    c. Update:
       - Personal best position (pbest) for each particle.
       - Global best position (gbest) for the entire swarm.
    d. Update velocities and positions of particles based on pbest and gbest:
            v[i] = w * v[i] + c1 * r1 * (pbest[i] - x[i]) + c2 * r2 * (gbest - x[i])
            x[i] = x[i] + v[i]
         where:
            v[i]: velocity of particle i
            x[i]: position of particle i
            w: inertia weight
            c1, c2: cognitive and social coefficients
            r1, r2: random numbers in [0, 1]
    e. Repeat steps b-d until a stopping criterion is met (e.g., max iterations or acceptable error).

3. Example Usage
    We will minimize the function f(x, y) = x^2 + y^2.
    which has a global minimum at (0, 0) with f(0, 0) = 0.
'''

import numpy as np
import matplotlib.pyplot as plt

# objective function to minimize
def objective_function(x, y):
    return x**2 + y**2

# PSO parameters
num_particles = 30 # number of particles in the swarm
num_iterations = 100 # number of iterations
w = 0.7 # inertia weight
c1 = 1.5 # cognitive coefficient (self)
c2 = 1.5 # social coefficient (swarm)
bounds = (-10, 10) # search space bounds for x and y

# Initialize particles
np.random.seed(42) 
X = np.random.uniform(bounds[0], bounds[1], (num_particles, 2)) # positions
V = np.random.uniform(-1, 1, (num_particles, 2)) # velocities

# Initialize pbest and gbest
pbest_positions = np.copy(X)
pbest_values = objective_function(X[:, 0], X[:, 1])

gbest_position = pbest_positions[np.argmin(pbest_values)]
gbest_value = np.min(pbest_values)

history = []

# PSO main loop
for iteration in range(num_iterations):
    r1, r2 = np.random.rand(2, num_particles, 1)
    V = (w * V + 
         c1 * r1 * (pbest_positions - X) + 
         c2 * r2 * (gbest_position - X))
    X = X + V
    X = np.clip(X, bounds[0], bounds[1]) # keep within bounds

    # Evaluate fitness
    fitness_values = objective_function(X[:, 0], X[:, 1])
    # Update pbest
    better_mask = fitness_values < pbest_values
    pbest_positions[better_mask] = X[better_mask]
    pbest_values[better_mask] = fitness_values[better_mask]
    # Update gbest
    if np.min(fitness_values) < gbest_value:
        gbest_position = X[np.argmin(fitness_values)]
        gbest_value = np.min(fitness_values)
    history.append(gbest_value)
    print(f"Iteration {iteration+1}/{num_iterations}, Best Value: {gbest_value}")

# Plot convergence
plt.plot(history)
plt.title("PSO Convergence")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness Value")
plt.grid()
plt.show()