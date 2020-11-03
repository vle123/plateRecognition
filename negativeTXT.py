import argparse
import cv2
import re
import random
import os,shutil
d='C:/Users/arman/Pictures/negatives'
l = os.listdir(d)
fichier = open("negatives.txt","w")
for x in l:
    fichier.write(x+"\n")
fichier.close()
