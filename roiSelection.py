import argparse
import cv2
import re
import random
import os,shutil
d='C:/Users/arman/Pictures/car/'
l = os.listdir('C:/Users/arman/Pictures/car')

while(True):
    path = random.choice(l)
    l.remove(path)
    img=cv2.imread(d+path)
    ROI = cv2.selectROI(img)

    if ROI!=(0,0,0,0):
        fichier = open('C:/Users/arman/Pictures/box.txt','a')
        fichier.write(path+" "+str(int(ROI[0]))+" "+str(int(ROI[1]))+" "+str(int(ROI[2]))+" "+str(int(ROI[3]))+"\n")
        fichier.close()
        imgCrop = img[int(ROI[1]):int(ROI[1]+ROI[3]), int(ROI[0]):int(ROI[0]+ROI[2])]
        cv2.imwrite('C:/Users/arman/Pictures/plate/'+path,imgCrop)
        shutil.move(d+path, 'C:/Users/arman/Pictures/carVerif/'+path)
        
        cv2.destroyAllWindows()
