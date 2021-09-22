
#### Variance expressed in terms of expected value

$ Var(X) = \frac{\sum_{y=1}^{m} (y_i - \mu)^2}{m} $  
*Note: y are individual values in the sample, can be duplicate according to their probability*

$ = \sum_{x=1}^{n} (x_i - \mu)^2 * p(x_i) $  
*Note: x are values in the distribution*  
*Note: $ \mu $ is the mean (or expected value) $ \sum_{x=1}^{n}x_i p(x_i) $*  

$ = E[(X - \mu)^2] $  

$ = \sum_{x=1}^{n} (x_i - \mu)^2 * p(x_i) $  

$ = \sum_{x=1}^{n} (x_i^2 - 2x_i\mu + \mu)^2 * p(x_i) $  

$ = \sum_{x=1}^{n}x_i^2p(x_i) - \sum_{x=1}^{n}2x_i\mu p(x_i) + \sum_{x=1}^{n}\mu^2 * p(x_i) $  

$ = \sum_{x=1}^{n}x_i^2p(x_i) - 2\mu\sum_{x=1}^{n}x_i p(x_i) + \mu^2\sum_{x=1}^{n}  p(x_i) $  

$ = E[X^2] - 2\mu\sum_{x=1}^{n}x_i p(x_i) + \mu^2\sum_{x=1}^{n}  p(x_i) $  

$ = E[X^2] - 2\mu\sum_{x=1}^{n}x_i p(x_i) + \mu^2(1) $  

$ = E[X^2] - 2\mu(\mu) + \mu^2(1) $  

$ = E[X^2] - 2\mu^2 + \mu^2 $  

$ = E[X^2] - \mu^2 $  

$ = E[X^2] - \mu^2 $  

$ = E[X^2] - (E[X])^2 $  

#### Properties of variance:  

https://www.youtube.com/watch?v=AzDtXD3bdLY

Var(aX+b)

$ = E[ (aX + b)^2 ] - (E [aX + b])^2 $  

$ = E[ a^2X^2 + 2abX + b^2] - (aE(X) + b)^2 $  

$ = a^2E(X^2) + 2abE(X) + b^2 - a^2E(X)^2 - 2abE(X) - b^2 $  
$ = a^2E(X^2) - a^2E(X)^2 $  

$ = a^2Var(X) $  

Var(X+Y)

$ = E[(X+Y)^2] - (E[X+Y])^2 $  

$ = E[X^2 + 2XY + Y^2] - (E[X]+E[Y])^2 $  

To prove the initial statement, it suffices to show that

\begin{aligned}\operatorname {Var} (X+Y)&=\operatorname {E} \left[(X+Y)^{2}\right]-(\operatorname {E} [X+Y])^{2}\\[5pt]&=\operatorname {E} \left[X^{2}+2XY+Y^{2}\right]-(\operatorname {E} [X]+\operatorname {E} [Y])^{2}.\end{aligned}}}{\displaystyle {\begin{aligned}\operatorname {Var} (X+Y)&=\operatorname {E} \left[(X+Y)^{2}\right]-(\operatorname {E} [X+Y])^{2}\\[5pt]&=\operatorname {E} \left[X^{2}+2XY+Y^{2}\right]-(\operatorname {E} [X]+\operatorname {E} [Y])^{2}.\end{aligned}
Using the linearity of the expectation operator and the assumption of independence (or uncorrelatedness) of X and Y, this further simplifies as follows:

{\begin{aligned}\operatorname {Var} (X+Y)&=\operatorname {E} \left[X^{2}\right]+2\operatorname {E} [XY]+\operatorname {E} \left[Y^{2}\right]-\left(\operatorname {E} [X]^{2}+2\operatorname {E} [X]\operatorname {E} [Y]+\operatorname {E} [Y]^{2}\right)\\[5pt]&=\operatorname {E} \left[X^{2}\right]+\operatorname {E} \left[Y^{2}\right]-\operatorname {E} [X]^{2}-\operatorname {E} [Y]^{2}\\[5pt]&=\operatorname {Var} (X)+\operatorname {Var} (Y).\end{aligned}}}{\displaystyle {\begin{aligned}\operatorname {Var} (X+Y)&=\operatorname {E} \left[X^{2}\right]+2\operatorname {E} [XY]+\operatorname {E} \left[Y^{2}\right]-\left(\operatorname {E} [X]^{2}+2\operatorname {E} [X]\operatorname {E} [Y]+\operatorname {E} [Y]^{2}\right)\\[5pt]&=\operatorname {E} \left[X^{2}\right]+\operatorname {E} \left[Y^{2}\right]-\operatorname {E} [X]^{2}-\operatorname {E} [Y]^{2}\\[5pt]&=\operatorname {Var} (X)+\operatorname {Var} (Y).\end{aligned}}}


Variance of standardized random variables:  

https://www.youtube.com/watch?v=H7wm2lLNNB4





 