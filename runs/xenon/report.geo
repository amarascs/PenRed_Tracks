A solid cylinder.                                                       
                                                                        
                                                                        
                                                                        
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   1)   Plane Z=-0.5                                        
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=(-5.000000000000000E-01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   2)   Plane Z=0.5                                         
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=( 5.000000000000000E-01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   3)   Cylinder R=0.5                                      
INDICES=( 1, 1, 0, 0,-1)
X-SCALE=( 5.000000000000000E-01,   0)       
Y-SCALE=( 5.000000000000000E-01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
MODULE  (   1)   Solid cylinder                                      
MATERIAL(   1)
SURFACE (   1), SIDE POINTER=( 1)
SURFACE (   2), SIDE POINTER=(-1)
SURFACE (   3), SIDE POINTER=(-1)
0000000000000000000000000000000000000000000000000000000000000000
END      0000000000000000000000000000000000000000000000000000000



*****************************************
****     PENGEOM (version 2014)      ****
****  Constructive Quadric Geometry  ****
*****************************************



************  Genealogical tree. 


*** MODULE =    1,  KMOTH =    0,  MAT =  1
KDGHT =    1
KSURF =    1    2    3
KFLAG =    2    1    1

The module    1 is the enclosure.


************  Adequacy of the geometry definition.

The largest number of bodies in a module or
     bodies limiting a single body is ............    1

The largest number of limiting surfaces for
     a single body or module is ..................    3


The simulation of this geometry will be relatively fast,
     no further optimization seems to be required.

************  The end.
