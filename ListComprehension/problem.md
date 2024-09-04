Given the dimensions of a cuboid (x, y, z) and a value n, generate a list of all possible coordinates (i, j, k) within that cuboid, excluding those where i + j + k equals n.

Example:

If x = 2, y = 1, z = 2, and n = 3, the output should be:

```
 [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2],
 [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
 [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
 [2, 2, 0], [2, 2, 1], [2, 2, 2]]
