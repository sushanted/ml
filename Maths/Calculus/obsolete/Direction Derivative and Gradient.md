#### Partial derivatives  

For three dimentions, we can fix x or y, i.e. slicing the graph parallel to x or y axis. With this fixing we get the graph in only terms of x or y. Now we can calculate derivatives in x or y directions separately.  

E.g. z = f(x,y) = xy  

$ \frac{\partial z}{\partial x} = y $  

$ \frac{\partial z}{\partial y} = x $  

for point (3,4), z = 12  

$ \frac{\partial z}{\partial x} = 4 $  

$ \frac{\partial z}{\partial x} = 3 $  

These are the rates of change in the x and y directions, and only in x and y directions (in the directions parallel to x and y axis respectively).

#### Directional derivative without partial derivatives and with partial derivatives (Good method and proof)

https://openstax.org/books/calculus-volume-3/pages/4-6-directional-derivatives-and-the-gradient

#### Directional derivative

Given any point in the input space (x,y), like (3,4) above, there would be a point in the output space (x,y,z); where z = f(x,y). From this point, there would be instantaneous changes (derivatives or slope) towards all the directions (Imagine a point on mountain or inside a vally). How to find the instantaneous changes in any of these directions? We know only two of them, one in the x direction and another in the y direction. Can we use these two to obtain all others?  

**Example 1** : imagine cycling on a uphill road, riding along a straight line parallel to the road needs more efforts. Riding perpeducular to the road is exactly same as riding on a flat surface (piece of a cake!). But our goal is to reach at the highest point, riding perpeducular to road won't get us to there. What if we ride in some angle to the road other than 0 or 90, say 20,30,50 etc in a zig zag manner, we'll require less efforts 
than riding parallel. Starting from angle 1 till 89, we'll require gradually more and more efforts. Notice we said "gradually", **grad**.
We can choose an optimum angle = reach faster and with minimal efforts.  

We can observe that the slope in x direction converges to the slope in y direction **grad**ually (or vice versa)

Following discussion is more towards dot product than directional derivative  
**Example 2** : We can imagine a magnetic field created by two magnets one pulling(or pushing) objects in the direction parallel to the x-axis and another one pulling(or pushing) objects in the direction parallel to the y-axis, depending on the relative power of the two magenets the force applied on the objects could move them in some very different direction than pure x and y. Note an important aspect, the magentic force applied on the objects depend on their position relative to the magnets (or simply their x-y co-ordinates as the positions of the magnets are fixed). One interesting thing here is, if we want to manually push the objects we'll have to work along the magentic force, if we are pushing in the direction of the magnetic force, it is easy, if we are pushing in the exactly opposite direction it is most difficult, for any other direction in-between, it depends on the relativity of that direction with the magentic force direction. The manual direction can be broken into two components, a component parallel to the magnetic force and a component perpendicular to the magnetic force. The component perpendicular to the magentic force direction has no (or very minimal) effect of the magentic force while the parallel component has maximum effect of the magentic force: exactly additive or substractive.  

TODO : Correlate the gradient to magnetic force and manual push to directional vector. Represent the gradient (magentic force) and manual push (direction) as vectors and introduce the dot product as the component in the direction of the magentic force. 

TODO : dot product of a vector V with unit vector is the component of the vector V in the unit vectors direction (or vice versa)
TODO : why unit vector


##### More intuition

Directional derivative is calculated at any point. Any derivative is the change in the output with instantaneous change in the input. Formally value of f(a+h)-f(a) when $ \lim_{h \to 0}$.  
For very small values of h,  
$f(a+h) - f(a) = ((a+h)-(a)) \frac{dy}{dx} =h*  \frac{dy}{dx} $.   
(  
When slope of a line m = $ \frac{y}{x} $ , given value of x we can tell the value of y and vice versa.   
Suppose $x_2 > x_1 and y_2 > y_1 $  
$ y_1 = \frac{y}{x} x_1$   
$ y_2 = \frac{y}{x} x_2$   

$ y_2 - y_1 = \frac{y}{x} (x_2 - x_1) $   

$ \frac{(y_2 - y_1)}{(x_2 - x_1)} = \frac{y}{x}  $   

)

Again returning to derivatives, for a 2 variable function z = f(x,y), the directional derivative is the change in the value of z with the instantaneous change in x and y. x and y can change in any proportion, even only x or only y can change leaving y or x un-altered. Therefore direction of change is important here. To get to any direction, we have to change x and y in appropriate proportions so that we land on a point on that direction. h, the instantaneous change, needs to be devided into its x and y components ($h_x$ and $h_y$) so that we can land into the desired direction by moving $h_x$ amount in the x-direction and $h_y$ amount in the y-direction (The vector sum).  

If $ \lim_{h \to 0}$, then $ \lim_{h_x \to 0}$ and $ \lim_{h_y \to 0}$  

Moving $h_x$ amount in x-direction, z changes by amount $ \frac{\partial z}{\partial x} * h_x$  

Moving $h_y$ amount in y-direction, z changes by amount $ \frac{\partial z}{\partial y} * h_y$  


We can imagine first moving in x-direction by $h_x$ amount and then in y-direction by $h_y$ amount, finally we'll reach our destination (the desired direction). When we reach x-direction  destination point, one can argue that the derivative in the y-direction at that point could be different than that the original point, but considering $h_x$ very very small, we can consider the derivative same at both the points OR can consider our journey to the destination broken into very very very very small $h_{x1},h_{y1},h_{x2},h_{y2},... $ directions respectively, where $ h_{x1} = \frac{h_x}{100000000000000...}$      

Total change from initial point to the destination = $ \frac{\partial z}{\partial x} * h_x $ +$ \frac{\partial z}{\partial y} * h_y $   

This is when the input is changed by h, so rate of change $\frac{d_{output}}{d_{input}}$ =   

$ \frac{ \frac{\partial z}{\partial x} * h_x + \frac{\partial z}{\partial y} * h_y}{h} $  

$ = \frac{\partial z}{\partial x} * \frac{h_x}{h} + \frac{\partial z}{\partial y} * \frac{h_y}{h} $  

$ = \frac{\partial z}{\partial x} * \frac{h_x}{\sqrt{h_x^2+h_y^2}} + \frac{\partial z}{\partial y} * \frac{h_y}{\sqrt{h_x^2+h_y^2}} $  

#### Gradient

We can see that above formula (rate of change in output) is the dot product between the vectors $\vec\nabla = \begin{bmatrix} \frac{\partial z}{\partial x} \\ \frac{\partial z}{\partial y} \end{bmatrix}$ and $ \vec H =  \begin{bmatrix} \frac{h_x}{h} \\ \frac{h_y}{h} \end{bmatrix} $.  
$\begin{bmatrix} \frac{\partial z}{\partial x} \\ \frac{\partial z}{\partial y} \end{bmatrix}$  is the gradient $\vec\nabla$, a vector containing all the partial derivatives. With dot product dual definition (Dot product Equivalence.md), the above dot product can also be represented as :  

$ |\vec\nabla||\vec H|cos\theta $  

At any point $|\vec\nabla|$ is fixed as partial derivatives are fixed.  

$ |\vec H| = \sqrt{(\frac{h_x}{h})^2+(\frac{h_y}{h})^2} $   
$ = \sqrt{\frac{h_x^2+h_y^2}{h^2}} $  
$ = \frac{1}{h}\sqrt{h_x^2+h_y^2}$  
$ = \frac{h}{h} $  
$ = 1 $  

means $\vec H$ is a unit vector.  

therefore maximum value of $ |\vec\nabla||\vec H|cos\theta $ (maximum rate of change at the point) would be $ |\vec\nabla|cos\theta $, $|\vec\nabla|$ being fixed at the point, maximizing the value of $cos\theta$ would give us the maximum value of the dot product, maximum value of $cos\theta$ is 1 when $\theta = 0$. This means the angle between the vectors $\vec\nabla$ and $\vec H$ would be 0 to get maximum rate of change. In other words they should point in the same direction, i.e. $\vec H$ should be a unit vector ($|\vec H|=1$) in the direction of $\vec\nabla$. It means moving (instantaneously) into the direction of $\vec \nabla$ would let us reach maximum height.    

Minimum value of $cos\theta$ is -1 when $\theta = 180$. This means the angle between the vectors $\vec\nabla$ and $\vec H$ would be 180 to get maximum rate of change. In other words they should point in the opposite directions, i.e. $\vec H$ should be a unit vector ($|\vec H|=1$) in the opposite direction of $\vec\nabla$. It means moving (instantaneously) into the opposite direction of $\vec \nabla$ would let us reach minimum height.  



#### Sources

https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/directional-derivative-introduction

https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/directional-derivatives-going-deeper

#### Points

##### Why magnitude of directional derivative matters:  
One very helpful way to think about this is to picture a point in the input space moving with velocity $ \vec{\textbf{v}} $
 The directional derivative of $ f $ along $\vec{\textbf{v}} $
 is the resulting rate of change in the output of the function. So, for example, multiplying the vector $ \vec{\textbf{v}} $ by two would double the value of the directional derivative since all changes would be happening twice as fast.

##### Gradient usefulness:
 Take a moment to delight in the fact that one single operation, the gradient, packs enough information to compute the rate of change of a function in every possible direction! That's so many directions! Left, right, up, down, north-north-east, $34.8^\circ $ degrees clockwise from the $x-axis$... Madness!
 
##### Visualizations
https://mathinsight.org/directional_derivative_gradient_introduction
https://www.geogebra.org/m/Bx8nFMNc

##### Physical Example
https://activecalculus.org/multi/S-10-6-Directional-Derivative.html



