from PIL import Image
import numpy as np
import math

# Open the image file
image = [[7,5,0,5,0],
         [3,8,7,11,3],
         [6,1,3,9,8],
         [0,6,4,0,5],
         [2,5,0,8,7]]

def bi_linear(x,y) :
    #find corner colors
    xfloor=int(math.floor(x))
    yfloor=int(math.floor(y))
    xceil=int(math.ceil(x))
    yceil=int(math.ceil(y))

    #put corner colors in array
    corners= [image[xfloor][ yfloor],image[xfloor][yceil],image[xceil][yfloor],image[xceil][yceil]]
    # F(x,y)=ax+by+cxy+d is the Patern
    equations =[[xfloor,yfloor,xfloor*yfloor,1],[xfloor,yceil,xfloor*yceil,1],[xceil,yfloor,xceil*yfloor,1],[xceil,yceil,xceil*yceil,1]]
    
    # four unknown equation solver
    A = np.array(equations)
    B = np.array(corners)
    # 4 unknown a,b,c,d
    X = np.linalg.inv(A).dot(B)

    # F(x,y)=ax+by+cxy+d 
    result=(X[0]*x)+(X[1]*y)+(X[2]*x*y)+X[3]
    print(result)

x = float(input("Enter x:"))
y = float(input("Enter y:"))
bi_linear(x,y)    