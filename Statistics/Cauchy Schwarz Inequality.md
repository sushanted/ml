$ ax^2+bx+c $ 

$ =a\cdot\left(x^2+\frac {b}{a}x+\frac{c}{a} \right)$ 

$ =a\cdot\left(x^2+\frac {2b}{2a}x+\frac{c}{a} \right)$ 

$ =a\cdot\left(x^2+2\frac {b}{2a}x+\frac{c}{a} \right)$ 

$ =a\cdot\left(x^2+2\frac {b}{2a}x+ \frac{b^2}{4a^2}-\frac{b^2}{4a^2}+ \frac{c}{a} \right)$ 

$ =a\cdot\left(\left(x^2+2\frac {b}{2a}x+ \frac{b^2}{4a^2}\right)-\frac{b^2}{4a^2}+ \frac{c}{a} \right)$ 

$ =a\cdot\left(\left(x+\frac {b}{2a}\right)^2-\frac{b^2}{4a^2}+ \frac{c}{a} \right)$ 

$ =a\cdot\left(x+\frac b{2a}\right)^2-\frac{b^2}{4a}+c $  

$ =a\cdot\left(x+\frac b{2a}\right)^2-\frac{b^2-4ac}{4a} $  

Note following points:



* being square $(x+\frac b{2a})^2 $ can only be >= 0 

* when a is positive, $ a\cdot\left(x+\frac b{2a}\right)^2 $ will be always >=0
    
* Base conditions are:  
    *   a is positive AND 
    *   $ ax^2+bx+c $ >= 0 for all values of x. Note: <u><b>"all values of x"</b></u> is important.
  

    
    
For $ ax^2+bx+c >= 0 $ to be true for all (and any) value of x, we must need $ a\cdot\left(x+\frac b{2a}\right)^2-\frac{b^2-4ac}{4a} $ >=0  
    
    
Only $ \frac{b^2-4ac}{4a} $ has the capability to make $ ax^2+bx+c >= 0 $ negative, a already being positive, sign of $ b^2-4ac $ dectates the sign of $ ax^2+bx+c $ i.e. $ a\cdot\left(x+\frac b{2a}\right)^2-\frac{b^2-4ac}{4a} $, when $ \frac{b^2-4ac}{4a} > a\cdot\left(x+\frac b{2a}\right)^2 $ in general.    

    
    
The value of the term $ a\cdot\left(x+\frac b{2a}\right)^2 $ is minimum(0) when    $ x = -\frac{b}{2a} $, in this case $ ax^2+bx+c = a\cdot\left(x+\frac b{2a}\right)^2-\frac{b^2-4ac}{4a} = -\frac{b^2-4ac}{4a} $ ,
    
if $ ax^2+bx+c >=0 $  in this case, following conditions are must (or can be inferred)  
    $ -\frac{b^2-4ac}{4a} >=0 $  
    $ \therefore \frac{b^2-4ac}{4a} <= 0 $  
    $ \therefore b^2-4ac <=0 \because$ a is positive   
    $ \therefore b^2 <= 4ac $ 
    
Therefore if a>0 AND $ ax^2+bx+c >= 0 $ for all(any value) of x, including $ x = -\frac{b}{2a} $ , then $ b^2 <= 4ac $ . Note that value of $ b^2-4ac $ is independant of x and therefore $ b^2-4ac <= 0 $ should always be true to have $ ax^2+bx+c >= 0 $ for all values of x.  
In other words, if $ b^2-4ac <= 0 $, $ ax^2+bx+c $ will never be less than 0.  


<b>Now we can use this fact, to prove Cauchy Schwarz Inequality </b>

Consider a series:

$ (a_1x+b_1)^2 + (a_2x+b_2)^2 + (a_3x+b_3)^2 + ... + (a_nx+b_n)^2 >= 0  \because $ being sum of all squares which is always positive

$ \therefore (a_1^2x^2 + 2a_1b_1x + b_1^2) + (a_2^2x^2 + 2a_2b_2x + b_2^2)+...+ (a_n^2x^2 + 2a_nb_nx + b_n^2) >= 0 $

$ \therefore \sum_{i=1}^{n}a_i^2x^2 + \sum_{i=1}^n2a_ib_ix + \sum_{i=1}^nb_i^2 >= 0 $  

$ \therefore (\sum_{i=1}^{n}a_i^2)x^2 + (2\sum_{i=1}^na_ib_i)x + (\sum_{i=1}^nb_i^2) >= 0 $  

This is a quadratic with  

$ a = \sum_{i=1}^{n}a_i^2 $  
$ b = 2\sum_{i=1}^na_ib_i $  
$ c = \sum_{i=1}^nb_i^2 $  

By the fact proved above,  

$ b^2 <= 4ac $  

So in our case (replacing a,b,c)  

$ (2\sum_{i=1}^na_ib_i)^2 <=  4 (\sum_{i=1}^{n}a_i^2)(\sum_{i=1}^nb_i^2) $  
$ 4(\sum_{i=1}^na_ib_i)^2 <=  4 (\sum_{i=1}^{n}a_i^2)(\sum_{i=1}^nb_i^2) $ 

$ (\sum_{i=1}^na_ib_i)^2 <= (\sum_{i=1}^{n}a_i^2)(\sum_{i=1}^nb_i^2) $ 

This is the Cauchy Schwarz inequality  

A simple example:  

$ (a_1b_1 + a_2b_2 + a_3b_3)^2 <= (a_1^2+a_2^2+a_3^2)(b_1^2+b_2^2+b_3^2) $ 

Another example:  

$ (3x+5y+9z)^2 <= (3^2+5^2+9^2)(x^2+y^2+z^2)$  

$ (3x+5y+9z)^2 <= (115)(x^2+y^2+z^2)$  

One more:  

$ (1 * 2+ 3 * 4+ 5 * 6)^2 <= (1^2+3^2+5^2)(2^2+4^2+6^2)$  

$ 1936 <= 1960 $  








    
    


    








