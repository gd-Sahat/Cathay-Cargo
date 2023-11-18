import cv2
import numpy as np

#getting intermediate points on the line between point1 and point2
#for example, calling this function with (p1,p2,3) will return the point
#on the line between p1 and p2, at 1/3 distance from p2
def get_intermediate_point(p1,p2,ratio):
    return [p1[0]+(p2[0]-p1[0])/ratio,p1[1]+(p2[1]-p1[1])/ratio]

#open dilated edge images
img=cv2.imread(dilated_edges,0)

#corners you got from your segmentation and other question
corners=[[29,94],[102,21],[184,52],[183,547],[101,576],[27,509]]
nb_corners=len(corners)

#intermediate points between corners you are going to test
ratios=[2,4,6,8] #in this example, the middle point, the quarter point, etc
nb_ratios=len(ratios)

#list which will contain all connected corners
connected_corners=[]

#double loop for going through all possible corners
for i in range(nb_corners-1):
    for j in range(i+1,nb_corners):
        cpt=0
        c1=corners[i]; c2=corners[j]

        #testing every intermediate points between the selected corners
        for ratio in ratios:
            p=get_intermediate_point(c1,c2,ratio)

            #checking if these points fall on a white pixel in the image
            if img[p[0],p[1]]==255:
                cpt+=1

        #if enough of the intermediate points fall on a white pixel
        if cpt>=int(nb_ratios*0.75):
            #then we assume that the 2 corners are indeed connected by a line
            connected_corners.append([i,j])

print(connected_corners)
