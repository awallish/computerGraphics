import math
import numpy as np


class Point():
    """
    Point class stores data for a three dimensional point and defines computer
    graphics opperations for that point such as translation, rotation, and 
    perspective projection.  All points are stored with homogeneous coordinates
    in numpy matricies.
    """
    
    
    def __init__(self, x, y, z):
        self.data = np.array([[x], [y], [z], [1]])
    

    def translate(self, x, y, z):
        """ Translates point by positive x, y, z"""
        
        self.data = Point.translationMatrix(x, y, z) @ self.data
                         
    
    def rotate(self, d, axis):
        """Rotates the point about the specified axis by d degrees."""
        matrix = None
        if axis.upper() == 'X':
            matrix = np.array([[1, 0, 0, 0],
                               [0, math.cos(d), -math.sin(d), 0],
                               [0, math.sin(d), math.cos(d), 0],
                               [0, 0, 0, 1]])         
        elif axis.upper() == 'Y':
            matrix = np.array([[math.cos(d), 0, math.sin(d), 0],
                               [0, 1, 0, 0],
                               [-math.sin(d), 0, math.cos(d), 0],
                               [0, 0, 0, 1]])                    
        elif axis.upper() == 'Z':
            matrix = np.array([[math.cos(d), 0, math.sin(d), 0],
                               [0, 1, 0, 0],
                               [-math.sin(d), 0, math.cos(d), 0],
                               [0, 0, 0, 1]])                       
        else:
            raise ValueError("Invalid axis of rotation.  Axis must be either X, Y, or Z")
            
        self.data = matrix @ self.data
                         
    
    
    def perspectiveProjection(self, d):
        """
        Returns the point projected onto 2d x-y plane given prospective d.
        Return value is a tuple (x, y)
        """
        
        projMatrix = np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, -1/d, 1]])
                         
        res = projMatrix @ self.data
        return (res[0][0]/res[3][0], res[1][0]/res[3][0]) #postprocess via 4th coord
        
        
        
    @staticmethod
    def translationMatrix(x, y, z):
        """
        Returns the translation matrix in homogeneous coordinates which shifts
        by x, y and z units in the x, y and z direction.  
        """
        return np.array([[1, 0, 0, x],
                         [0, 1, 0, y],
                         [0, 0, 1, z],
                         [0, 0, 0, 1]])