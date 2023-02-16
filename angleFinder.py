import cv2
import math
import matplotlib.pyplot as plt

class angle:
    ## Declare variables
    
    # Store path of image
    self.image_path = 'grasp_1.jpg'
    
    # Read image file
    self.image = cv2.imread(self.image_path)
    
    # Hold coordinates of dots
    self.dots_list = []
    
    ## Functions
    
    # Draw the dots and join it to form a line
    def mouse_dots(mouse_key,x_coor,y_coor,flag,params):
        if mouse_key == cv2.EVENT_LBUTTONDOWN:
            dot_size = len(self.dots_list)
            
            # Check if three dots are present and form a line b/w them
            if dot_size != 0 and dot_size % 3 != 0:
                cv2.arrowedLine(self.image,tuple(self.dots_list[dot_size((dot_size-1)/3)*3]),(x_coor,y_coor),(0,0,255),2)
                
                # Draw the dots
                cv2.circle(self.image,(x_coor,y_coor),5,(0,0,255),cv2.FILLED)
                self.dots_list.append([x_coor,y_coor])
                
    def gradient_finder(dot_1,dot_2):
        # y2-y1/x2-x1
        return (dot_2[1]-dot_1[1])/(dot_2[0]-dot_1[0])
    
    # Find angle b/w dots
    def angle_evaluator(dots_list):
        dot_1,dot_2,dot_3 = dots_list[-3:]
        m_1 = gradient_finder(dot_1,dot_2)
        m_2 = gradient_finder(dot_1,dot_3)
        
        angle_R = math.atan((m_2 - m_1) / (1 + (m_2 * m_1)))
        angle_D = round(math.degrees(angle_R),4)
        
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",metavar='',type=str,default='grasp_1.jpg')
    args, _ = parser.parse_known_args()
    
    
    while True:
        if len(self.dots_list) % 3 == 0 and len(self.dots_list) != 0:
            angle_evaluator(self.dots_list)
            
        cv2.imshow('Image',self.image)
        cv2.
