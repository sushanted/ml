#### Questions:

##### Why partial derivatives?

Cost function is a function of all w and b (and any intermediate entities z,a), All these partial derivatives are part of the gradient vector $ \nabla $. A step in the opposite direction of this vector is suppose to reduce the overall cost.

$ C = \frac{1}{2} \sum_j(y_j-a^L_j)^2 $  

$ \therefore \partial C / \partial a^L_j = (a_j^L-y_j)$  .....1

$ \because \frac{\partial}{\partial x} [(a-x)^2 + (b-y)^2] $  

$=  \frac{\partial}{\partial x} [(a-x)^2] $  

$= \frac{\partial}{\partial x} (a^2-2ax+x^2)$  

$ = 2(x-a)$

Only one j remains, because it is partial derivative  

#### BP2

Consider following setup:  
3 neurons in layer l and 2 neurons in layer l+1  
layer l+1 is the final layer  
j is the index in l layer  
k is the index in l+1 layer  

consider the first(j=1) neuron in layer l, it is feeding into both the neurons (k=1 and 2) of layer l+1  


$ C = \frac{1}{2}\sum_k(y_k-a_k^{l+1})^2 $  

$  = \frac{1}{2}(y_1-a_1^{l+1})^2 + \frac{1}{2}(y_2-a_2^{l+1})^2 $  

$ \frac{\partial C}{\partial z_1^l} = -(y_1-a_1^{l+1})\frac{\partial{a_1^{l+1}}}{\partial{z_1^l}} + -(y_2-a_2^{l+1})\frac{\partial{a_2^{l+1}}}{\partial{z_1^l}} $  

$ \frac{\partial C}{\partial z_1^l} = (a_1^{l+1}-y_1)\frac{\partial{a_1^{l+1}}}{\partial{z_1^l}} + (a_2^{l+1}-y_1)\frac{\partial{a_2^{l+1}}}{\partial{z_1^l}} $  

Applying chain rule:  

$ \frac{\partial C}{\partial z_1^l} = (a_1^{l+1}-y_1)\frac{\partial{a_1^{l+1}}}{\partial{z_1^l}} + (a_2^{l+1}-y_1)\frac{\partial{a_2^{l+1}}}{\partial{z_1^l}} $  

$ \frac{\partial C}{\partial z_1^l} = (a_1^{l+1}-y_1)\frac{\partial{a_1^{l+1}}}{\partial{z_1^{l+1}}}\frac{\partial{z_1^{l+1}}}{\partial{z_1^l}} + (a_2^{l+1}-y_2)\frac{\partial{a_2^{l+1}}}{\partial{z_2^{l+1}}}\frac{\partial{z_2^{l+1}}}{\partial{z_1^l}} $  .....2  

Note the indices carefully above for $\partial z^{l+1}$, $a_1$ is function of $z_1$ while $a_2$ is function of $z_2$  

$ z_1^{l+1} = w_{11}^{l+1}a_1^l+b_1^{l+1} = w_{11}^{l+1}\sigma(z_1^l)+b_1^{l+1}$ and  

$ z_2^{l+1} = w_{21}^{l+1}a_1^l+b_2^{l+1} = w_{21}^{l+1}\sigma(z_1^l)+b_2^{l+1} $  

therefore differentiating with $\partial z_1^l$  

$ \frac{\partial{z_1^{l+1}}}{\partial{z_1^l}} = w_{11}^{l+1}\sigma'(z_1^l) $ and  

$ \frac{\partial{z_2^{l+1}}}{\partial{z_1^l}} = w_{21}^{l+1}\sigma'(z_1^l) $  

Substituting in 2  

$ \frac{\partial C}{\partial z_1^l} = (a_1^{l+1}-y_1)\frac{\partial{a_1^{l+1}}}{\partial{z_1^{l+1}}}w_{11}^{l+1}\sigma'(z_1^l) + (a_2^{l+1}-y_2)\frac{\partial{a_2^{l+1}}}{\partial{z_2^{l+1}}}w_{21}^{l+1}\sigma'(z_1^l) $ ......3  


from 1,  
$(a_1^{l+1}-y_1) = \frac{\partial C}{\partial{a_1^{l+1}}}$ and   
$(a_2^{l+1}-y_2) = \frac{\partial C}{\partial{a_2^{l+1}}}$  

Substituting in 3  

$ \frac{\partial C}{\partial z_1^l} = \frac{\partial C}{\partial{a_1^{l+1}}}\frac{\partial{a_1^{l+1}}}{\partial{z_1^{l+1}}}w_{11}^{l+1}\sigma'(z_1^l) + \frac{\partial C}{\partial{a_2^{l+1}}}\frac{\partial{a_2^{l+1}}}{\partial{z_2^{l+1}}}w_{21}^{l+1}\sigma'(z_1^l) $   

$ \frac{\partial C}{\partial z_1^l} = \frac{\partial C}{\partial{z_1^{l+1}}}w_{11}^{l+1}\sigma'(z_1^l) + \frac{\partial C}{\partial{z_2^{l+1}}}w_{21}^{l+1}\sigma'(z_1^l) $  

$ \frac{\partial C}{\partial z_1^l} = \sum_k\frac{\partial C}{\partial{z_k^{l+1}}}w_{k1}^{l+1}\sigma'(z_1^l)  $  

And generically, for any $j^{th}$ neuron in layer l:  

$ \frac{\partial C}{\partial z_j^l} = \sum_k\frac{\partial C}{\partial{z_k^{l+1}}}w_{kj}^{l+1}\sigma'(z_j^l)  $  

##### How multiple samples'/inputs' costs are aggregated, considering different cost for each sample/input ?
##### how BP2 can be applied recursively for l-1, l-2 etc?

##### Ignore following part, it didn't work out well:

Imagine 3 neurons in l and 2 neurons in l+1, and l+1 is the last layer  

k is the index in l+1 layer  
j is the index in l layer  

$k^{th}$ z in l+1 can be calculated as  

$ z_k^{l+1} = \sum_j w_{kj}^{l+1} a_j^l + b_k^{l+1} $  

sum is over all j output activations from l into weights of l+1 for $k^{th}$ neuron  


$ z_1^{l+1} = \sum_j w_{1j}^{l+1} a_j^l + b_1^{l+1} $  

$ =  w_{11}^{l+1} a_1^l  + w_{12}^{l+1} a_2^l + b_1^{l+1} $  

$ =  w_{11}^{l+1} \sigma(z_1^l) + w_{12}^{l+1} \sigma(z_2^l) + b_1^{l+1} $ ..............1 

$ z_2^{l+1} = \sum_j w_{2j}^{l+1} a_j^l + b_2^{l+1} $  

$ = w_{21}^{l+1} a_1^l + w_{22}^{l+1} a_2^l + b_2^{l+1}$  

$ = w_{21}^{l+1} \sigma(z_1^l) + w_{22}^{l+1} \sigma(z_2^l) + b_2^{l+1}$  ..............2  

$ C = \frac{1}{2} \sum_k(y_k - a_k^{l+1})^2 $  

$ = \frac{1}{2} (y_1 - a_1^{l+1})^2 + \frac{1}{2}(y_2 - a_2^{l+1})^2 $  

$ = \frac{1}{2} (y_1 - a_1^{l+1})^2 + \frac{1}{2}(y_2 - a_2^{l+1})^2 $  

$ = \frac{1}{2} [y_1 - \sigma(z_1^{l+1})]^2 + \frac{1}{2}[y_2 - \sigma(z_2^{l+1})]^2 $  

Substituting 1 and 2

$ = \frac{1}{2} [y_1 - \sigma(w_{11}^{l+1} \sigma(z_1^l) + w_{12}^{l+1} \sigma(z_2^l) + b_1^{l+1})]^2 + \frac{1}{2}[y_2 - \sigma(w_{21}^{l+1} \sigma(z_1^l) + w_{22}^{l+1} \sigma(z_2^l) + b_2^{l+1})]^2 $  

$ \frac{\partial C}{\partial z_1^l} = [y_1 - \sigma(w_{11}^{l+1} \sigma(z_1^l) + w_{12}^{l+1} \sigma(z_2^l) + b_1^{l+1})][ \frac {\partial }{\partial z_1^l}y_1 - \frac {\partial }{\partial z_1^l}[\sigma(w_{11}^{l+1} \sigma(z_1^l) + w_{12}^{l+1} \sigma(z_2^l) + b_1^{l+1})]]$

