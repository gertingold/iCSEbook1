# This file was *autogenerated* from the file make_figs.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_9p81 = RealNumber('9.81'); _sage_const_600 = Integer(600); _sage_const_0p4 = RealNumber('0.4'); _sage_const_4 = Integer(4); _sage_const_200 = Integer(200); _sage_const_0p2 = RealNumber('0.2'); _sage_const_5p2 = RealNumber('5.2'); _sage_const_0p1 = RealNumber('0.1'); _sage_const_10 = Integer(10); _sage_const_1000 = Integer(1000); _sage_const_3p14 = RealNumber('3.14'); _sage_const_30 = Integer(30); _sage_const_0p01 = RealNumber('0.01'); _sage_const_3p5 = RealNumber('3.5')
var('t')
x0,y0,vx0,vy0 = _sage_const_0 ,_sage_const_0 ,_sage_const_10 ,_sage_const_10 
g = _sage_const_9p81 
t_end = _sage_const_2 *vy0/g
plt = parametric_plot([x0+vx0*t,y0+vy0*t-g*t**_sage_const_2 /_sage_const_2 ],(t,_sage_const_0 ,t_end),\
          axes_labels=[r"$x$",r"$y$"],\
          figsize=_sage_const_3p5  
 )
plt.save("rzut1.pdf")

x0,y0 = _sage_const_0 ,_sage_const_0 
g = _sage_const_9p81 /_sage_const_1000  
v = _sage_const_600 /_sage_const_1000 
plt = sum([parametric_plot([x0+v*cos(alpha)*t,y0+v*sin(alpha)*t-g*t**_sage_const_2 /_sage_const_2 ],(t,_sage_const_0 ,_sage_const_2 *v*sin(alpha)/g),\
    figsize=_sage_const_3p5 ,\
    axes_labels=[r"$x[km]$",r"$y[km]$"]
 ) for alpha in srange(_sage_const_0p01 ,_sage_const_3p14 /_sage_const_2 ,_sage_const_0p1 )])
h = v**_sage_const_2 /(_sage_const_2 *g)
plt = plt + plot(h-x**_sage_const_2 /(_sage_const_4 *h),(x0,_sage_const_0 ,v**_sage_const_2 /g),fill=True,fillalpha=_sage_const_0p2 ,fillcolor='yellow',color='yellow',alpha=_sage_const_0p4 )

plt.save("pplot.pdf")
print "OK"

x0,y0,vx0,vy0 = _sage_const_0 ,_sage_const_0 ,_sage_const_10 ,_sage_const_10 
g = _sage_const_9p81 
t_end = _sage_const_2 *vy0/g

m = _sage_const_200              
tab = [[x0,y0]] 
delta_t = t_end/m
for i in range(_sage_const_1 ,m):                    
    x  = x0 + vx0*delta_t 
    y  = y0 + vy0*delta_t
    vx = vx0
    vy = vy0 - g*delta_t
    x0, y0, vx0, vy0 = [ x, y, vx, vy] 
    tab.append([x0,y0])     
p2 = list_plot(tab[::_sage_const_10 ],color='red',size=_sage_const_30 ,ymax=_sage_const_5p2 )
var('t')
x0,y0,vx0,vy0 = _sage_const_0 ,_sage_const_0 ,_sage_const_10 ,_sage_const_10 
p1 = parametric_plot(\
 [x0+vx0*t,y0+vy0*t-g*t**_sage_const_2 /_sage_const_2 ],\
 (t,_sage_const_0 ,t_end) ,\
    figsize=_sage_const_3p5 ,\
    axes_labels=[r"$x$",r"$y$"]
 )
(p1+p2).save("porownanie.pdf")
