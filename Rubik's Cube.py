import numpy as np
import copy

# front, back, top, bottom, right, left

rubiks_cube = np.array([[[0, 0], # White
                        [0, 0]],
    
                        [[1, 1], # Blue
                        [1, 1]],

                        [[2, 2], # Green
                        [2, 2]],

                        [[3, 3], # Orange
                        [3, 3]],
                        
                        [[4, 4], # Red
                        [4, 4]],
                        
                        [[5, 5], # Yellow
                         [5, 5]]])

rubiks_cube = np.array([[[0, 2],
                        [1, 2]],
    
                        [[4, 1],
                        [5, 4]],

                        [[5, 3],
                        [1, 3]],

                        [[3, 5],
                        [2, 0]],
                        
                        [[5, 5],
                        [0, 3]],
                        
                        [[4, 2],
                         [0, 1]]])


def rotate_face(direction, cube):
    '''
    up (u) (clockwise)
    
    right (r) (clockwise)
    
    spin (s) (clockwise)
    '''

    if direction == "s":
        cube[0] = np.rot90(cube[0], 3)
        cache = copy.copy(cube[2, 0])
        cube[2, 0] = cube[4, 0]
        cube[4, 0] = cube[1, 0]
        cube[1, 0] = cube[3, 0]
        cube[3, 0] = cache

    elif direction == "r":
        cube[1] = np.rot90(cube[1], 3)
        cache0 = copy.copy(cube[0, 1, 0])
        cache1 = copy.copy(cube[0, 1, 1])
        cube[0, 1, 0] = cube[3, 1, 0]
        cube[0, 1, 1] = cube[3, 1, 1]
        cube[3, 1, 0] = cube[5, 1, 0]
        cube[3, 1, 1] = cube[5, 1, 1]
        cube[5, 1, 0] = cube[4, 1, 0]
        cube[5, 1, 1] = cube[4, 1, 1]
        cube[4, 1, 0] = cache0
        cube[4, 1, 1] = cache1


    elif direction == "u":
        cube[4] = np.rot90(cube[4], 3)
        cache0 = copy.copy(cube[0, 0, 1])
        cache1 = copy.copy(cube[0, 1, 1])
        cube[0, 0, 1] = cube[2, 0, 1]
        cube[0, 1, 1] = cube[2, 1, 1]
        cube[2, 0, 1] = cube[5, 0, 1] 
        cube[2, 1, 1] = cube[5, 1, 1]
        cube[5, 0, 1] = cube[1, 0, 1]
        cube[5, 1, 1] = cube[1, 1, 1]
        cube[1, 0, 1] = cache0
        cube[1, 1, 1] = cache1
        
    return cube

output = (rotate_face("none", rubiks_cube))

X = output - output
Y = np.array([])

while True:
    X += output
    y = str(input())

    if y == "s":
        Y += np.array([3])

    elif y == "r":
        Y += np.array([1])

    elif y == "u":
        Y += np.array([2])

    output = (rotate_face(y, output))
    np.save('X.npy', X)
    np.save('Y.npy', Y)
    print(output)
    


    

        

        




