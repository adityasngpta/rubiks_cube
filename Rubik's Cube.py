import numpy as np
import copy

# front, back, top, bottom, right, left

rubiks_cube = np.array([[[0, 0, 0],
                        [0, 0, 0],  # Yellow
                        [0, 0, 0]],
    
                        [[1, 1, 1],
                        [1, 1, 1],  # Orange
                        [1, 1, 1]],

                        [[2, 2, 2],
                        [2, 2, 2],  # Red
                        [2, 2, 2]],

                        [[3, 3, 3],
                        [3, 3, 3], # Blue
                        [3, 3, 3]],
                        
                        [[4, 4, 4],
                        [4, 4, 4], # Green
                        [4, 4, 4]],
                        
                        [[5, 5, 5],
                         [5, 5, 5], # White
                         [5, 5, 5]]])

rubiks_cube = np.array([[[4, 3, 4],
                        [2, 0, 0],  
                        [0, 0, 0]],
    
                        [[5, 2, 5],
                        [1, 1, 5],  
                        [2, 3, 2]],

                        [[3, 1, 2],
                        [0, 2, 1],  
                        [1, 5, 4]],

                        [[1, 4, 1],
                        [3, 3, 4], 
                        [5, 2, 5]],
                        
                        [[4, 2, 2],
                        [3, 4, 5], 
                        [0, 1, 0]],

                        [[3, 4, 1],
                         [5, 5, 4],
                         [3, 0, 3]]])


def rotate_face(direction, cube):
    '''
    (spin face)
    s (clockwise)
    
    (bottom)
    b (clockwise)

    ^ Rotating right ^

    (right)
    r
    
    (left)
    l

    ^ Rotating up ^
    '''
    if direction == "s":
        cube[0] = np.rot90(cube[0], 3)
        cache = copy.copy(cube[2, 0])
        cube[2, 0] = cube[4, 0]
        cube[4, 0] = cube[1, 0]
        cube[1, 0] = cube[3, 0]
        cube[3, 0] = cache
        
    elif direction == "b":
        cube[2] = np.rot90(cube[2], 3)
        cache1 = copy.copy(cube[0, 2, 0])
        cache2 = copy.copy(cube[0, 2, 1])
        cache3 = copy.copy(cube[0, 2, 2])

        cube[0, 2, 0] = cube[3, 2, 2]
        cube[0, 2, 1] = cube[3, 1, 2]
        cube[0, 2, 2] = cube[3, 0, 2]

        cube[3, 2, 2] = cube[5, 2, 2]
        cube[3, 1, 2] = cube[5, 1, 2]
        cube[3, 0, 2] = cube[5, 0, 2]

        cube[5, 2, 2] = cube[3, 0, 0]
        cube[5, 1, 2] = cube[3, 1, 0]
        cube[5, 0, 2] = cube[3, 2, 0]

        cube[3, 0, 0] = cache1
        cube[3, 1, 0] = cache2
        cube[3, 2, 0] = cache3   

        
    return cube

output = (rotate_face("none", rubiks_cube))

while True:
    output = (rotate_face(str(input()), output))
    print(output)

    

        

        




