
from __future__ import division
import random

from drawingpanel import *



def triangle(canvas,x1,y1,x2,y2,x3,y3,n):
	if n==0:
		canvas.create_polygon(x1,y1,x2,y2,x3,y3,width=5.0,fill=getcolor())
	else:	
		triangle(canvas,x1,y1,(x1+x2)/2,(y1+y2)/2,(x1+x3)/2,(y1+y3)/2,n-1)
		triangle(canvas,x2,y2,(x1+x2)/2,(y1+y2)/2,(x2+x3)/2,(y2+y3)/2,n-1)
		triangle(canvas,x3,y3,(x1+x3)/2,(y1+y3)/2,(x2+x3)/2,(y2+y3)/2,n-1)

def getcolor():
	return random.choice(["red","yellow","blue","black","green","pink","purple","orange"])


def main():
	panel=DrawingPanel(800,800)
	canvas=panel.canvas
	triangle(canvas,400,30,30,770,770,770,5)

main()