import numpy as np
import matplotlib.pyplot as plt


def genereate_matrix(n):
    arr = np.random.choice([-1, 1], size=(n * n), p=[1 / 2, 1 / 2])
    # print(arr)
    arr = arr.reshape((n, n))
    # arr2 = np.ones((4, 4))
    # print(arr)
    return arr


def get_neighbours(input_matrix, i, j):
    if i == -1 or j == -1 or i == L or j == L:
        return 0
    else:
        return input_matrix[i][j]


def calculate_energy(input_matrix):
    # print(input_matrix, "\n")
    energy_array = []
    for i in range(0, 4):
        for j in range(0, 4):
            a = get_neighbours(input_matrix, i - 1, j)
            b = get_neighbours(input_matrix, i + 1, j)
            c = get_neighbours(input_matrix, i, j - 1)
            d = get_neighbours(input_matrix, i, j + 1)
            energy_array.append((-0.5) * input_matrix[i][j] * (a + b + c + d))

    # print(np.array(energy_array).reshape((4, 4)))


def calculate_specific_energy(input_matrix, i, j):
    a = get_neighbours(input_matrix, i - 1, j)
    b = get_neighbours(input_matrix, i + 1, j)
    c = get_neighbours(input_matrix, i, j - 1)
    d = get_neighbours(input_matrix, i, j + 1)
    energy = (-0.5) * input_matrix[i][j] * (a + b + c + d)
    return energy


# calculate_energy(matrix)


def monte_carlo(n, l, input_matrix, beta):
    # print(input_matrix, "\n")
    spinned_matrix = np.copy(input_matrix)
    l2 = l * l
    # monte carlo
    ls = []

    for x in range(0, n):
        for y in range(0, l2):
            i = np.random.randint(l)
            j = np.random.randint(l)

            spin = -spinned_matrix[i][j]
            spinned_matrix[i][j] = spin

            delta = calculate_specific_energy(spinned_matrix, i, j)
            # print(energy)
            if delta < 0:
                continue
                # spinned_matrix = input_matrix

            else:
                r = np.random.random_sample()
                p = np.exp(-1 * beta * delta)

                if r <= p:
                    continue
                else:
                    spinned_matrix[i][j] = -spinned_matrix[i][j]

        if n % 100 == 0:
            ls.append(np.mean(spinned_matrix))

    # print(ls)
    return np.mean(ls)


# monte_carlo(matrix, 1)


L = 5
N = 100
matrix = genereate_matrix(L)


def prepare(n, l, generated_matrix):
    result = []
    for i in range(0, 100):
        result.append(monte_carlo(n, l, generated_matrix, (1 * i) / 100))

    # print(result)
    return result


results = prepare(N, L, matrix)

plt.plot(results)
plt.show()
plt.close()

plt.plot(np.array(range(100))/100, np.abs(np.array(results)))
plt.show()
plt.close()

plt.plot(np.array(range(100))/100, np.array(results))
plt.show()
plt.close()

#           x   x   x   x
#           x   x   x   x
#           x   x   1   x
#           x   x   x   x
