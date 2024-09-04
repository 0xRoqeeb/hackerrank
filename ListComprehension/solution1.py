#solving the problem using multiple loops

  def generate_coordinates(x, y, z, n):
    #function to generate all possible co-ordinates in a cubiod exluding those that sum to n
#args x, y, z, n
    return [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]


x = int(input())
y = int(input())
z = int(input())
n = int(input())
#collect input from user

coordinates = generate_coordinates(x, y, z, n)
print(coordinates)
