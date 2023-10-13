import matplotlib.pyplot as plt
import control as cnt
import numpy as np


G1 = cnt.tf(3,[1,1])
G2 = cnt.tf(1,[1,7])
G3 = cnt.tf(7,[1,2])
#G4 = cnt.tf(1,[1,0])
#G5 = cnt.tf(1,[1,-1])
G6 = cnt.tf(1,[1,1,1])

t1 , y1 = cnt.step_response(G1)
t2 , y2 = cnt.step_response(G2)
t3 , y3 = cnt.step_response(G3)
#t4 , y4 = cnt.step_response(G4)
#t5 , y5 = cnt.step_response(G5)
t6 , y6 = cnt.step_response(G6)


plt.plot(t1,y1,label = "G1")
plt.plot(t2,y2, label = "G2")
plt.plot(t3,y3, label = "G3")
#plt.plot(t4,y4, label = "G4")
#plt.plot(t5,y5, label = "G5")
plt.plot(t6,y6, label = "G6")
plt.xlabel("time(ms)")
plt.ylabel("step response")
plt.legend()
plt.show()