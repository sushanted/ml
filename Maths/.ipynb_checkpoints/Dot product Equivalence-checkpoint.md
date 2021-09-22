#### Two definitions

Imagine two vectors $ A =[a_x,a_y]$ and $ B = [b_x,b_y]  $

The dot product is given by following two definitions:  

1. $ a_xb_x + a_yb_y $
2. $|A||B|cos \theta $  

#### How these two definitions are equivalent?  

Imagine a plane with x and y axis. Let's say vector A makes angle of $\theta_1$ with the x-axis, and vector B makes angle of $\theta_2 > \theta_1$ with x-axis, and let $\theta$ be the angle between the two vectors.

Therefore,

$  a_x = |A|cos\theta_1$  
$  a_y = |A|sin\theta_1$  
$  b_x = |B|cos\theta_2$  
$  b_y = |B|sin\theta_2$  
$ \theta = \theta_2 - \theta_1 $  

$ a_xb_x + a_yb_y = |A|cos\theta_1 |B|cos\theta_2 + |A|sin\theta_1|B|sin\theta_2$  

$ = |A||B|cos\theta_1cos\theta_2 + |A||B|sin\theta_1sin\theta_2 $ 

$ = |A||B|(cos\theta_1cos\theta_2 + sin\theta_1sin\theta_2) $ 

$ = |A||B| cos(\theta_2 - \theta_1) $  

$ = |A||B| cos\theta $  

  


#### Proof of : $ cos(\theta_2 - \theta_1) $  


$cos\theta$ and $sin\theta$ are basically respectively x and y co-ordinates of the intersection of the radius at angle $\theta$ with x-axis and the unit circle. When the angle is $-\theta$, x-co-ordinate remains same and positive while the y-co-ordinate becomes negative.  

Proof of $cos(\theta_1 + \theta_2)$: https://www.youtube.com/watch?v=V3-xCPDzQ1Q  

$ \therefore x = cos(-\theta) = cos(\theta)$ and $ y = sin(-\theta)=-sin(\theta) $  

$ cos(\theta) = cos(\theta_2 - \theta_1) $  

$ = cos(\theta_2 + (-\theta_1)) $  

$ = cos\theta_2 cos(-\theta_1) - sin(\theta_2)sin(-\theta_1)$  

$ = cos\theta_2 cos\theta_1 + sin\theta_2sin\theta_1$  









