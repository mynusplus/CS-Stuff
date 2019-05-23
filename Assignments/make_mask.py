import matplotlib.pyplot as plt
import numpy as np
import PIL

    

def spiral(rows, columns):
    '''def fill(point1, point2, point3, point4):
        x_values = [point1[0], point2[0], point3[0], point4[0]]
        y_values = [point1[1], point2[1], point3[1], point4[1]]
        max_x = max_y = 0
        min_x = columns
        min_y = rows
        for x in x_values:
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
        for y in y_values:
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
        for column in range(min_x+1, max_x-1):
            for row in range(min_y+1, max_y-1):
                if (column-min_x)/2 > m'''
                
        
    
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    a = np.matrix('.6 .81; -.81 .6')
    init_cond1 = np.matrix([[1], [1]])
    init_cond2 = np.matrix([[-1], [-1]])
    last1 = init_cond1
    last2 = init_cond2
    for i in range(1000):
        b = np.linalg.matrix_power(a, i)
        result1 = b * init_cond1
        result2 = b * init_cond2
        try:
            # fill([int(result1[0])+ int(rows/2), int(result1[1])+int(columns/2)],[int(result2[0])+ int(rows/2), int(result2[1])+int(columns/2)],[int(last1[0])+ int(rows/2), int(last1[1])+int(columns/2)],[int(last2[0])+ int(rows/2), int(last2[1])+int(columns/2)])

            image[int(result1[0])+ int(rows/2)][int(result1[1])+int(columns/2)] = [255, 0, 0, 100]
            image[int(result2[0])+ int(rows/2)][int(result2[1])+int(columns/2)] = [0, 255, 0, 100]
        except:
            print('broke')
            break
        last1 = result1
        last2 = result2
    return image
    
if __name__ == "__main__":
    image = spiral(200,200)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()            
              
