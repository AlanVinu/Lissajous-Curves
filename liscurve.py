##from pandas import set_option
##set_option('max_columns', None)
##set_option('max_rows', None)
##
##from os import chdir
##chdir(r'C:\Users\Alan\Desktop\Chegg')      


##for i in range(26,37):
##    ansP = i
##    ansT = i+9
##    answer = ansP/ansT
##    answer = answer*100
##    answer = round(answer,2)
##    answerR = round(answer)
##    answerR = str(answerR)+"%"
##    answer = str(answer)+"%"
##    print(ansP, ansT, answer, answerR)

from numpy import sin, pi, arange
import matplotlib.pyplot as plt

def x(a, time = [0,2*pi], A = 1, delta = pi/2):
    '''A sin(at + 𝜹)'''
    result = list()
    for t in arange(time[0],time[1],0.01):
        result.append(A * sin( a * t + delta))
    return result

def y(b, time = [0,2*pi], B = 1):
    '''B sin(bt)'''
    result = list()
    for t in arange(time[0],time[1],0.01):
        result.append(B * sin( b * t))
    return result

aVals = [1,2,3,4]
bVals = [1,2,3,4]

fig, ax = plt.subplots(4, 4, figsize = (10,10))

for row in range(4):
    xs = x(aVals[row]) # gets the x values from function x() over t = [0,2*𝝿]
    for col in range(4):
        ys = y(bVals[col]) # gets the y values from function y() over t = [0,2*𝝿]
        ax[row,col].plot(xs,ys)
        ax[row,col].set_aspect(aspect = 'equal')
        ax[row,col].set_title(f"a = {aVals[row]}, b = {bVals[col]}")

# to set a common x label and y label for all plots
for axis in ax.flat:
    axis.set(xlabel = 'A sin(at + δ)', ylabel = 'B sin(bt)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for axis in ax.flat:
    axis.label_outer()

plt.suptitle('Lissajous curve(δ = π/2, A = B = 1, t = [0,2π])')
plt.tight_layout(h_pad = 0.952, rect = [0,0.03,1,0.95])
plt.show()

