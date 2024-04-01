import math, matplotlib.pyplot as plt

def euclid_dist(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

coordinates = {
    "A1": (2, 10),
    "A2": (2, 5),
    "A3": (8, 4),
    "B1": (5, 8),
    "B2": (7, 5),
    "B3": (6, 4),
    "C1": (1, 2),
    "C2": (4, 9)
}

cluster_coords = {
    "A": coordinates["A1"],
    "B": coordinates["B1"],
    "C": coordinates["C1"]
}

distances = {}
cluster = {}

for letter, coordinate in coordinates.items():
    distances[coordinate] = {
        "A": euclid_dist(coordinate, cluster_coords["A"]),
        "B": euclid_dist(coordinate, cluster_coords["B"]),
        "C": euclid_dist(coordinate, cluster_coords["C"]),
    }

for letter, distance in distances.items():
    assigned_c = min(distance, key=distance.get)
    cluster[letter] = assigned_c

for letter, cluster_coords in cluster.items():
    print(letter, "is in cluster", cluster_coords)

x = [coordinate[0] for coordinate in coordinates.values()]
y = [coordinate[1] for coordinate in coordinates.values()]

assign_color = {
    "A": "red",
    "B": "green",
    "C": "blue"
}

cluster_color = [assign_color[cluster_coords] for cluster_coords in cluster.values()]

plt.scatter(x, y, c=cluster_color)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
