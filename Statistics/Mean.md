### Properties of mean  

$ \mu = \frac{\sum_{x=1}^{n}x_i}{n} $  

#### Scaling and location change

After Multiplying every element by a and adding b:  

$  \frac{\sum_{i=1}^{n} (ax_i+b)}{n} $  

$= \frac{\sum_{i=1}^{n} ax_i + \sum_{x=1}^{n} b}{n} $  

$= \frac{\sum_{i=1}^{n} ax_i + bn}{n}  $  (...Adding n times b to itself)  

$= \frac{a \sum_{i=1}^{n} x_i + bn}{n}  $  

$= \frac{a \sum_{i=1}^{n} x_i}{n} + b $  

$= a\mu + b $  


Basically,  
1. when you add b to every element in the series of n elements, n b's gets added i.e. sum increases by $ b*n $
therefore the mean increases by $ \frac{b*n}{n} = b $  
2. when you multiply a every element in the series of n elements, there is a common factor of 'a' in the sum. If we get the factor out of the sum, the mean becomes factor of original mean.


#### Addition and Multiplication  

If series X has mean $ \mu_x $ and series Y has mean $ \mu_y $ , the mean of their addition is $ \mu_x + \mu_y $  

Let's say there are two boxes box X and box Y, say box X has 3 apples $ (x_1,x_2,x_3) $ with mean weight $ \mu_x $ and box Y has 4 oranges $ (y_1,y_2,y_3,y_4) $ with mean weight $ \mu_y $, what is the mean weight of an apple and an orange taken together?  

There are 3\*4 possible ways of picking a pair of apple and an orange, there are 3\*4 possible pair weights.

$ \mu_x = \frac{x_1+x_2+x_3}{3} $  

$ \mu_y = \frac{y_1+y_2+y_3+y_4}{4} $  

*Generalized proof:*

$ \mu_{x+y} = \frac{sum of weights of all pairs}{no of pairs} $  

$ = \frac{\sum_{i=1}^{n_x}\sum_{j=1}^{n_y} x_i+y_j}{n_x n_y} $  

$ = \frac{(x_1 + y_1 + x_1 + y_2 + x_1 + y_3 + ... + x_1 + y_{n_y})+(x_2 + y_1 + x_2 + y_2 + x_2 + y_3 + ... + x_2 + y_{n_y})+ ... + (x_{n_x} + y_1 + x_{n_x} + y_2 + x_{n_x} + y_3 + ... + x_{n_x} + y_{n_y})}{n_x n_y} $  

$ = \frac{(n_y x_1 + y_1 + y_2 + y_3 + ... + y_{n_y})+ (n_y x_2 + y_1 + y_2 + y_3 + ... + y_{n_y}) + ... +(n_y x_{n_x} + y_1 + y_2 + y_3 + ... + y_{n_y})}{n_x n_y}$  

$ = \frac{(n_y x_1 + n_y x_2 + ... + n_y x_{n_x}) + n_x(y_1+y_2+y_3+...+y_{n_y})}{n_x n_y} $  


$ = \frac{n_y( x_1 +  x_2 +x_3+ ... +  x_{n_x}) + n_x(y_1+y_2+y_3+...+y_{n_y})}{n_x n_y} $  

$ = \frac{n_y( x_1 +  x_2 +x_3+ ... +  x_{n_x})}{n_x n_y} + \frac{n_x(y_1+y_2+y_3+...+y_{n_y})}{n_x n_y} $  

$ = \frac{( x_1 +  x_2 +x_3+ ... +  x_{n_x})}{n_x} + \frac{(y_1+y_2+y_3+...+y_{n_y})}{ n_y} $  

$ = \mu_x + \mu_y $  

*For our example:*

$ \mu_{x+y} = \frac{[(x_1 + y_1) + (x_1 + y_2) + (x_1 + y_3) +(x_1 + y_4)] + [(x_2 + y_1) + (x_2 + y_2) + (x_2 + y_3) +(x_2 + y_4)] + [(x_3 + y_1) + (x_3 + y_2) + (x_3 + y_3) +(x_3 + y_4)]}{3*4} $  

$ = \frac{[4x_1 + y_1 +y_2 +y_3 +y_4]+[4x_2 + y_1 +y_2 +y_3 +y_4]+[4x_3 + y_1 +y_2 +y_3 +y_4]}{3*4} $   

$ = \frac{4x_1 +4x_2 +4x_3 +3 * (y_1 +y_2 +y_3 +y_4)}{3*4}$  
$ = \frac{4(x_1 +x_2 +x_3) +3 * (y_1 +y_2 +y_3 +y_4)}{3*4}$ 

$ = \frac{4(x_1 +x_2 +x_3)}{3*4} + \frac{3 * (y_1 +y_2 +y_3 +y_4)}{3*4}$  

$ = \frac{x_1 +x_2 +x_3}{3} + \frac{(y_1 +y_2 +y_3 +y_4)}{4} $  

$ = \mu_x + \mu_y $  

*The argument for multiplication is similar*



$ \mu_{x*y} = \frac{product of weights of all pairs}{no of pairs} $  

$ = \frac{(x_1*y_1 + x_1*y_2 + x_1*y_3 + x_1*y_4) +  (x_2*y_1 + x_2*y_2 + x_2*y_3 + x_2*y_4) + (x_3*y_1 + x_3*y_2 + x_3*y_3 + x_3*y_4)}{3*4}$  

$ = \frac{x_1(y_1+y_2+y_3+y_4) +x_2(y_1+y_2+y_3+y_4)+x_3(y_1+y_2+y_3+y_4)}{3*4} $  

$ = \frac{(x_1 +x_2+x_3)(y_1+y_2+y_3+y_4)}{3*4} $  

$ = \frac{(x_1 +x_2+x_3)}{3}*\frac{(y_1+y_2+y_3+y_4)}{4} $  

$ = \mu_x * \mu_y $




















