import random, math, matplotlib.pyplot as plt, numpy as np

def dartboard(throws):
    hits = 0

    for _ in range(throws):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x ** 2 + y ** 2)

        if distance <= 1/4:
            if np.abs(x) / 2 <= 0.2:
                hits += 1

    probability = hits / throws
    return probability

if __name__ == "__main__":
    print(dartboard(10000))