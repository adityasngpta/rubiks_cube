import numpy as np
import copy

# front, back, top, bottom, right, left

rubiks_cube = np.array([[[0, 0, 0],
                        [0, 0, 0],  # Yellow
                        [0, 0, 0]],
    
                        [[1, 1, 1],
                        [1, 1, 1],  # White
                        [1, 1, 1]],

                        [[2, 2, 2],
                        [2, 2, 2],  # Orange
                        [2, 2, 2]],

                        [[3, 3, 3],
                        [3, 3, 3], # Red
                        [3, 3, 3]],
                        
                        [[4, 4, 4],
                        [4, 4, 4], # Blue
                        [4, 4, 4]],

                        [[5, 5, 5],
                        [5, 5, 5], # Green
                        [5, 5, 5]]])


def rotate_face(direction, cube):
    '''
    (spin face)
    s_1
    s_2
    s_3
    
    (bottom)
    b_1
    b_2
    b_3

    ^ Rotating right ^

    (right)
    r_1
    r_2
    r_3
    
    (left)
    l_1
    l_2
    l_3

    ^ Rotating up ^
    '''

    if direction == "b_1":
        cache = copy.copy(cube[0,2])
        cube[0,2] = cube[4,2]
        cube[4,2] = cube[1,2]
        cube[1,2] = cube[5,2]
        cube[5,2] = cache

    if direction == "b_2":
        cache = cube[0,2]
        cube[0,2] = cube[2,2]
        cube[2,2] = cache
        cube[4,2] = cube[5,2]
        cube[5,2] = cube[4,2]

    if direction == "b_3":
        cache = cube[0,2]
        cube[0,2] = cube[5,2]
        cube[5,2] = cube[2,2]
        cube[2,2] = cube[4,2]
        cube[4,2] = cache

    if direction == "s_1":
        cube[0] = np.rot90(cube[0])
        cache = cube[3,0]

        cube[5,0,0] = cache[0]
        cube[5,1,0] = cache[1]
        cube[5,2,0] = cache[2]
        
        cube[2,2] = [cube[5,0,0], cube[5,1,0], cube[5,2,0]]

        cube[4,0,2] = cube[2,2,0]
        cube[4,1,2] = cache[2,2,1]
        cube[4,2,2] = cache[2,2,2]

        cube[3,0] = [cube[4,0,2], cube[4,1,2], cube[4,2,2]]

    if direction == "s_2":
        cube[0] = np.rot90(cube[0])
        cube[0] = np.rot90(cube[0])
        cache = cube[3,0]

        cache1 = cube[5,0,0]
        cache2 = cube[5,1,0] 
        cache3 = cube[5,2,0]

        cube[5,0,0] = cube[4,2,2]
        cube[5,1,0] = cube[4,1,2]
        cube[5,2,0] = cube[4,0,2]
        
        cube[3,0] = cube[2,2]

        cube[2,2] = cache

        cube[4,2,2] = cache1
        cube[4,1,2] = cache2
        cube[4,0,2] = cache3

    if direction == "s_3":
        cube[0] = np.rot90(cube[0])
        cube[0] = np.rot90(cube[0])
        cube[0] = np.rot90(cube[0])
        cache = cube[3,0]

        cube[5,0,0] = cube[2,2,0]
        cube[5,1,0] = cache[2,2,1]
        cube[5,2,0] = cache[2,2,2]
        
        cube[2,2] = [cube[4,0,2], cube[4,1,2], cube[4,2,2]]

        cube[4,0,2] = cache[0]
        cube[4,1,2] = cache[1]
        cube[4,2,2] = cache[2]

        cube[3,0] = [cube[5,0,0], cube[5,1,0], cube[5,2,0]]

    if direction == "r_1":
        cache = cube[1,2]
        cube[1,2] = cube[4,2]
        cube[4,2] = cube[3,2]
        cube[3,2] = cube[5,2]
        cube[5,2] = cache

    if direction == "r_2":
        cache = cube[1,2]
        cube[1,2] = cube[3,2]
        cube[3,2] = cache
        cube[4,2] = cube[5,2]
        cube[5,2] = cube[4,2]

    if direction == "r_3":
        cache = cube[1,2]
        cube[1,2] = cube[5,2]
        cube[5,2] = cube[3,2]
        cube[3,2] = cube[4,2]
        cube[4,2] = cache

    if direction == "l_1":
        cache = cube[1,0]
        cube[1,0] = cube[5,0]
        cube[5,0] = cube[3,0]
        cube[3,0] = cube[4,0]
        cube[4,0] = cache

    if direction == "l_2":
        cache = cube[1,0]
        cube[1,0] = cube[3,0]
        cube[3,0] = cache
        cube[4,0] = cube[5,0]
        cube[5,0] = cube[4,0]

    if direction == "l_3":
        cache = cube[1,0]
        cube[1,0] = cube[4,0]
        cube[4,0] = cube[3,0]
        cube[3,0] = cube[5,0]
        cube[5,0] = cache

    return cube

    
print(rotate_face("b_1", rubiks_cube))

    

        

        




