# This file was *autogenerated* from the file LinAlg_cloud/AlgebraLiniowa/source/figures/figs.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_18 = Integer(18); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_13 = Integer(13); _sage_const_4p4 = RealNumber('4.4'); _sage_const_3p85 = RealNumber('3.85'); _sage_const_15 = Integer(15); _sage_const_0p6 = RealNumber('0.6'); _sage_const_3p15 = RealNumber('3.15'); _sage_const_3p05 = RealNumber('3.05'); _sage_const_2p65 = RealNumber('2.65')
""" Rysunki do 8 Wykładów """

figlst = [] # inicjacja listy rysunków z nazwami

### Rysunek 1. Dwie proste na płaszczyźnie jako obraz oznaczonego układu 2 równań. ###

var('x1 x2')
eq1 = _sage_const_2 *x1-x2==_sage_const_1 ; eq2 = x1+x2==_sage_const_5 
P0 = point((_sage_const_2 ,_sage_const_3 ), color='black',size=_sage_const_15 , zorder=_sage_const_5 )
p1 = implicit_plot(eq1, (x1, _sage_const_0 , _sage_const_5 ), (x2, _sage_const_0 , _sage_const_5 ), color='red')
p2 = implicit_plot(eq2, (x1, _sage_const_0 , _sage_const_5 ), (x2, _sage_const_0 , _sage_const_5 ), color='green')
txt0 = text('$P(2,3)$', (_sage_const_2p65 , _sage_const_3p05 ), color='black', fontsize=_sage_const_13 )
txt1 = text('$2\,x_1-\,x_2=\,1$',(_sage_const_3p85 , _sage_const_4p4 ), color='black', fontsize=_sage_const_13 )
txt2 = text('$x_1+\,x_2=\,5$',   (_sage_const_3p15 , _sage_const_0p6 ), color='black', fontsize=_sage_const_13 )
plt1 = plot(P0 + p1 + p2 + txt0 + txt1 + txt2, aspect_ratio=_sage_const_1 , axes=False, figsize=_sage_const_5 , frame=True)
figlst.append([plt1,"Rys_1"])


### Rysunek 2. Trzy płaszczyzny jako obraz oznaczonego układu 3 równań. ###

var('x1 x2 x3')
eq1 = _sage_const_2 *x1+_sage_const_1 *x2+_sage_const_1 *x3== _sage_const_1 
eq2 = _sage_const_1 *x1-_sage_const_1 *x2+_sage_const_0 *x3==-_sage_const_1 
eq3 = _sage_const_1 *x1+_sage_const_1 *x2+_sage_const_2 *x3== _sage_const_2 
p1 = implicit_plot3d(eq1,(x1,-_sage_const_5 ,_sage_const_5 ),(x2,-_sage_const_5 ,_sage_const_5 ),(x3,-_sage_const_5 ,_sage_const_5 ),color='red')
p2 = implicit_plot3d(eq2,(x1,-_sage_const_5 ,_sage_const_5 ),(x2,-_sage_const_5 ,_sage_const_5 ),(x3,-_sage_const_5 ,_sage_const_5 ),color='green')
p3 = implicit_plot3d(eq3,(x1,-_sage_const_7 ,_sage_const_7 ),(x2,-_sage_const_5 ,_sage_const_5 ),(x3,-_sage_const_5 ,_sage_const_5 ),color='blue')
plt2 = p1 + p2 + p3 + point3d((-_sage_const_1 /_sage_const_4 ,_sage_const_3 /_sage_const_4 ,_sage_const_3 /_sage_const_4 ), size=_sage_const_18 , color='white')
# figlst.append([plt2,"Rys_2"])
# 3-wymiarowy wykres plt2 bezpośrednio zapisuje się tylko w formacie .png, i to koślawo.
# Lepszy efekt osiąga się wywołując plt2 z linii poleceń Sage'a i zapisując
# (odpowiednio powiększony) obraz Jmol w formacie .jpg albo .png.
# Właśnie tak powstały pliki Rys_24.png i Rys_25.jpg.

for [p,n] in figlst:
    p.save('%s.png'%n)
    p.save('%s.svg'%n)
    p.save('%s.pdf'%n)
    















