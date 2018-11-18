# TSPTW
Travelling Salesman Problem with time windows
The code here uses a metaheuristic to come up with a solution to an NP-hard problem
The code tries to solve the travelling salesman problem with time windows using the iterated greedy algorithm. 
The proposed algorithm makes use of the Variable Neighborhood Search (VNS) method to get a list of neighborhood solutions through destruction and construction of solution components. 
The problem described here refers to a salesman visiting different customers on his route in a particular order to optimize the cost of travel as well as minimize the loss due to seeing the customers outside the time windows described for each customer. The salesman must visit the customers inside the time windows or else bear the penalty associated with it.
The algorithm consists of random parameters like NFT0, lambda and number of nodes
cij is a matrix of distances between the i and j nodes in the salesman's path
ei represents the upper limit of the time window
li represents the lower limit of the time window

Initially an infeasible solution is generated randomly and then the greedy algorithm is applied to the solution in order to get a feasible solution in the end.
