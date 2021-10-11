### Expected value  

Given a probability distribution for a random variable X , and if $ p(x_i) $  is the probability of possible value $ x_i $  
the sample drawn out of the distribution should have $ p(x_i) $ portion of $ x_i $  

For example, if the distribution is (0.1,0.2,0.3,0.4) for values $ (x_1,x_2,x_3,x_4) $  

and if we draw a sample of size 10, the expected amount of $ (x_1,x_2,x_3,x_4) $ would be (1,2,3,4) respectively  

The population mean would be then  

$ \frac{x_1 + x_2 + x_2 + x_3 + x_3 + x_3 + x_4 + x_4 + x_4 + x_4}{10}  $  

$ = \frac{1*x_1 + 2*x_2 + 3*x_3 + 4*x_4}{10}  $  

$ = \frac{1}{10}*x_1 + \frac{2}{10}*x_2 + \frac{3}{10}*x_3 + \frac{4}{10}*x_4 $  

$ = 0.1*x_1 +  0.2*x_2 + 0.3*x_3 + 0.4*x_4 $

$ = p(x_1)*x_1 +  p(x_2)*x_2 + p(x_3)*x_3 + p(x_4)*x_4 $  

$ = \sum_{i=1}^{n} p(x_i)*x_i  $  

$ = E(X) $  

**Expected value is the mean, but as the values are supposed to be repeated in the sample, according their probability, it becomes the weighted average, where weight is the repeatition or probability of the particular value**

#### $ E(X^2) $

For above example,    

$ E(X^2) $  

$ = \frac{x_1^2 +  x_2^2 + x_2^2 + x_3^2 +  x_3^2 +  x_3^2 +  x_4^2 +  x_4^2 +  x_4^2 + x_4^2}{n} $  

$ = \frac{1*x_1^2 + 2*x_2^2 + 3*x_3^2 + 4*x_4^2}{10}  $  

$ = \frac{1}{10}*x_1^2 + \frac{2}{10}*x_2^2 + \frac{3}{10}*x_3^2 + \frac{4}{10}*x_4^2 $  

$ = 0.1*x_1^2 +  0.2*x_2^2 + 0.3*x_3^2 + 0.4*x_4^2 $  

$ = p(x_1)*x_1^2 +  p(x_2)*x_2^2 + p(x_3)*x_3^3 + p(x_4)*x_4^4 $  

$ = \sum_{n=1}^{n} p(x_i)*x_i^2  $ 

*Note: $ E(X) = \sum_{n=1}^{n} p(x_i)*x_i $ but $ E(X^2) != \sum_{n=1}^{n} p(x_i^2)*x_i^2 $*  

Actually : $ E(X^2) = \sum_{n=1}^{n} p(x_i)*x_i^2 $  

Changing the expression inside E doesn't change the probability value, but only the value inside the summation is changed, because the distribution of the varaibles $ x_i $ remains the same.

#### Scaling and location change

$ E(aX+b) = \sum_{i=1}^{n} (a*x_i+b)p(x_i) $  

$ = \sum_{i=1}^{n} (a*x_i)p(x_i) + \sum_{n=1}^{n} (b)p(x_i) $  

$ = a\sum_{i=1}^{n} (x_i)p(x_i) + b\sum_{n=1}^{n} p(x_i) $  

$ = aE(X) + b\sum_{i=1}^{n} p(x_i) $  

$ = aE(X) + b\sum_{i=1}^{n} p(x_i) $  

$ = aE(X) + b(1) $  

$ = aE(X) + b $   

#### Addition 

we know that $ \mu_{x+y} = \mu_x + \mu_y $ the proof can be found in the Mean.md chapter, expected value is also the mean, so the same proof is applicable for expected values.

Consider a box X with red balls and blue balls in the proprtion 1:4 (this is actually the probability distribution of (0.2,0.8)), red ball with weight 8g and blue ball with weight 3g each. If we draw a sample of 5 balls from the box, the probable mean or expected value of the sample would be :  
$ E[X] = \frac{8 + 3 + 3 + 3 + 3}{5} = \frac{20}{5} = 4g $  
$ E[X] = p(r)w_r + p(b)w_b $ = 0.2 * 8 + 0.8 * 3

Consider another box Y with green and yellow cubes in the proportion 1:3 (this is actually the probability distribution of (0.25,0.75)), green cube with weight 2g and yellow cube with weight 6g each. If we draw a sample of 4 cubes from the box, the probable mean or expected value of the sample would be :  
$ E[Y] = \frac{2 + 6 + 6 + 6}{4} = \frac{20}{4} = 5g $  
$ E[Y] = p(g)w_g + p(y)w_y $ = 0.25 * 2 + 0.75 * 6  

Now consider a scenario, where we draw a sample of 5 balls from box X and a sample of 4 cubes from box Y, what would be the expected value of sum of the weights of the two samples? E[X+Y] ?  

The sample drawn from box X should have distribution (8,3,3,3,3)  
The sample drawn from box Y should have distribution (2,6,6,6)  

A pair of (ball,cube) can be selected from the two samples in 5 * 4 = 20 different ways and then can be added to get a possible value. To get the expected value (the mean of all possible values), we need to get mean of all possible pair weights:  

$ \frac{(8+2) + (8+6) + (8+6) + (8+6) + (3+2) + (3+6) + (3+6) + (3+6) + (3+2) + (3+6) + (3+6) + (3+6) + (3+2) + (3+6) + (3+6) + (3+6) + (3+2) + (3+6) + (3+6) + (3+6)}{5*4} $

$ = \frac{[4*8 + (2+6+6+6)] + [4*3 + (2+6+6+6)] + [4*3 + (2+6+6+6)] + [4*3 + (2+6+6+6)] + [4*3 + (2+6+6+6)]}{5 * 4} $  

$ = \frac{4*(8+3+3+3+3)+5*(2+6+6+6)}{5*4} $  

$ = \frac{4*(8+3+3+3+3)}{5*4}+\frac{5*(2+6+6+6)}{5*4} $  

$ = \frac{(8+3+3+3+3)}{5}+\frac{(2+6+6+6)}{4} $ 

 ### $ = E[x] + E[Y] $  

$ = \frac{1(8+2) + 3(8+6) + 4(3+2) + 12(3+6)}{5 * 4} $  

$ = \frac{1}{5* 4}(8+2) + \frac{3}{5* 4}(8+6) + \frac{4}{5* 4}(3+2) + \frac{12}{5* 4}(3+6) $  

$ = \frac{1}{5}\frac{1}{4}(8+2) + \frac{1}{5}\frac{3}{4}(8+6) + \frac{4}{5}\frac{1}{4}(3+2) + \frac{4}{5}\frac{3}{ 4}(3+6) $  

$ = p(8)p(2)(8+2) + p(8)p(6)(8+6) + p(3)p(2)(3+2)+  p(3)p(6)(3+6) $  

Generically:

$ = \sum_{i=1}^{n}\sum_{j=1}^{m} p(x_i)p(y_j)(x_i + y_j) $  

$ = \sum_{i=1}^{n}\sum_{j=1}^{m} p(x_i and y_j)(x_i + y_j) $  

$ = \sum_{i=1}^{n}\sum_{j=1}^{m} p(x_i)p(y_j)(x_i) + p(x_i)p(y_j)(y_j) $  

$ = \sum_{i=1}^{n}\sum_{j=1}^{m} p(x_i)p(y_j)(x_i) + \sum_{i=1}^{n}\sum_{j=1}^{m}p(x_i)p(y_j)(y_j) $  

$ = \sum_{i=1}^{n} p(x_i)(x_i)\sum_{j=1}^{m}p(y_j) + \sum_{i=1}^{n}\sum_{j=1}^{m}p(x_i)p(y_j)(y_j) $  

$ = \sum_{i=1}^{n} p(x_i)(x_i)\sum_{j=1}^{m}p(y_j) + \sum_{j=1}^{m}\sum_{i=1}^{n}p(x_i)p(y_j)(y_j) $  

$ = \sum_{i=1}^{n} p(x_i)(x_i)\sum_{j=1}^{m}p(y_j) + \sum_{j=1}^{m}p(y_j)(y_j)\sum_{i=1}^{n}p(x_i) $  

$ = \sum_{i=1}^{n} p(x_i)(x_i)(1) + \sum_{j=1}^{m}p(y_j)(y_j)(1) $  

$ = \sum_{i=1}^{n} p(x_i)(x_i) + \sum_{j=1}^{m}p(y_j)(y_j) $  

### $ = E[X] + E[Y] $  


#### LOTUS

Function of a random variable, $Y = X ^2 $, there are two values of X for each unique value of Y, e.g. for Y=4, X = {2,-2}  

Therefore $ P(Y=4) = P(X=-2)+P(X=2) $ 

The expected value for X is $ \sum_i x_i P_X(x_i) $  

Here $x_i$ are all the realized values of X, like 1,2,3,4,5,6 for a dice.  

Now expected value of Y = $ \sum_i y_i P_Y(y_i) $  

For $ Y = X^2 $  

$ P_Y(1) = P_X(-1)+P_X(1) $  
$ P_Y(2) = P_X(-2)+P_X(2) $  and so on

And realized values of Y are all positive, when X = -1, Y = 1; when X = 1, Y = 1 again    

$ EY = \sum_i y_i P_Y(y_i) $ 

Assume X can take only following values {-2,-1,1,2}, then Y will have only following values {1,4}  

$ EY = 1 P_Y(1) + 4 P_Y(4)  $

$ = 1 [P_X(-1)+P_X(1)] + 4 [P_X(-2)+P_X(2)]  $  

$ = 1P_X(-1)+ 1P_X(1) + 4 P_X(-2) + 4 P_X(2)  $   

Conveniently distributing values of x for the same y :

$ = (-1)^2P_X(-1)+ 1^2 P_X(1) + (-2)^2 P_X(-2) + 2^2 P_X(2) $  

$ = \sum_i (x_i)^2 P_X(i) $  

In general, for any function g:  

$ E[g(X)]= \sum_i g(x_i) P_X(i) $  






