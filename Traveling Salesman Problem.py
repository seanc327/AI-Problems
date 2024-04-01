import math
import itertools

def euclid_dist(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tsp(cities):
    # variable initialization
    p_shortest = None #path
    d_shortest = float('inf') #lowest cost (distance)
    perm = itertools.permutations(cities)

    # all possible permutations for input list
    for path in perm:
        dist = 0
        for i in range(len(path) - 1):
            dist += euclid_dist(path[i], path[i+1])
        dist += euclid_dist(path[-1], path[0])
        # distance comparison
        if d_shortest > dist:
            d_shortest = dist
            p_shortest = path

    return p_shortest, d_shortest

if __name__ == "__main__":
    # swapped cities (3, 1) swapped with (6, 5):
    cities = [(8,6), (6,5), (3,6), (7,0), (3,1), (7,2)]
    p_shortest, d_shortest = tsp(cities)
    print("optimal order of traversal:", p_shortest)
    print("cost: {:.2f} ".format(d_shortest))

    #expected output:
    # optimal order of traversal: ((8, 6), (6, 5), (3, 6), (3, 1), (7, 0), (7, 2))
    # cost: 20.64



