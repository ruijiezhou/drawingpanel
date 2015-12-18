from drawingpanel import *
import math
import random


#def tree_trunk(canvas,x1,y1,x2,y2,l):
	#canvas.create_line(x1,y1,x2,y2,width=5.0)

def tree_branches(panel,canvas,x1,y1,theta,n,l,ang,wid):
	if n==0:
		draw_line(x1,y1,l,theta,canvas,n+1)
		canvas.create_oval(x1+l*math.cos(theta),y1+l*math.sin(theta),x1+(l+20)*math.cos(theta),y1+(l+20)*math.sin(theta),width=wid,fill=getcolor())
	else:
		panel.sleep(l*n/300)
		draw_line(x1,y1,l,theta,canvas,2*n)
		tree_branches(panel,canvas,x1+l*math.cos(theta),y1+l*math.sin(theta),theta+ang*n,n-1,l-3,ang,2*n)
		tree_branches(panel,canvas,x1+l*math.cos(theta),y1+l*math.sin(theta),theta-ang*n,n-1,l-3,ang,2*n)

def ang(n):
	return math.pi/math.pow(n,2)

def getcolor():
	return random.choice(["red","yellow","black","green","pink","purple","orange"])

def getcolor2():
	return random.choice(["brown","dark green","black"])


def draw_line(x1,y1,l,theta,canvas,wid):
	canvas.create_line(x1,y1,x1+l*math.cos(theta),y1+l*math.sin(theta),width=wid,fill=getcolor2())

def cloud(x1,y1,x2,y2,canvas):
	#panel.sleep(l*n/300)
	canvas.create_oval(x1,y1,x2,y2,fill="white",width=1.0,outline="light blue")

def main():	
	panel=DrawingPanel(1200,1200)
	canvas=panel.canvas
	#tree_trunk(canvas,400,800,400,600)
	ang=math.pi/math.pow(8,2)
	#tree_branches(canvas,420,800,math.pi/0.666,8,80,ang,1.0)

	for i in range(0,5):
		#panel.sleep(i*1000)
		#panel.clear()
		tree_branches(panel,canvas,300*i,800,math.pi/0.666,8,50,ang,1.0)

	for i in range(0,10):
		cloud(50+120*i,100,150+120*i,130,canvas)

	#canvas.set_background(canvas,blue)

	canvas.configure(background="light blue")

main()









	



