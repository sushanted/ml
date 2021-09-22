## Topics

### Neural network function 

### Cost function and optimization

Cost function : A function which gives the measure of how well trained the network is, less the cost well the trained network. The output is a single number, it is the average of costs calculates over all the training data.

 total cost = function(weights and biases,training examples)
 
 single cost = function(weights and biases,single training input, expected output)
 
=$\sum(expected\_output - actual\_output)^2$   note: summation is over all neurons in output layer

total cost = $\sum\sum(expected\_output - actual\_output)^2$ note : outer summation is over all training examples

  
    
    Our goal is to minimize the cost, i.e. it should give as small value as output as possible.
    How do you know that the given value is minimum? 
    For single variable function $\frac{dy}{dx} = 0$ at the minimum value, imagine a U shaped curve : the values do decrease from both the ends till the bottom of the U, so it is the place where the value is minimum. It is a U-turn from decrease to increase (minima) for a continuous value function. It is minima if values at f(t+dx) and f(t-dx) are greater than the f(t). 

### Gradient descent

### Gradient is a vector (full pack) of partial derivatives for all variables which affect the function

    For a multi-variable function we cannot calculate the tuple of values for variables e.g. (x,y) for which f(x,y) is minimal. For a multi-variable function partial derivatives give the rate of change in each variables direction. The gradient gives the vector which gives the direction for steepest ascent which we can follow to get a local maximum OR in the opposite direction to get a local minimum.

  Example:
  
  $f(x,y) = x^2+y^3$
  
  $\frac{\partial f}{\partial x} = 2x$
  
  $\frac{\partial f}{\partial y} = 3y^2$
  
  Gradient:
  
  $\begin{bmatrix}2x \\ 3y^2 \end{bmatrix}$
  
  General gradient:
  
  $\begin{bmatrix}
      \frac{\partial f}{\partial a} \\
      \frac{\partial f}{\partial b} \\
      \frac{\partial f}{\partial c} \\
      . \\
      . \\
      . \\
      \frac{\partial f}{\partial z} \\
  \end{bmatrix}$

We can start at any random point in the input space e.g. (1,1) and calculate the gradient value e.g. (2,3) and then move into direction of that point e.g. (1-2,1-3) = (-1,-2) and repeat till we get a minimum value for that function.
TODO: how to determine if the value is minimal?




Gradient descent process : Select random weights and biases at first, the cost is defined as avergae cost of all the training samples, calculated using current weights and biases. 




### Questions:

#### Old
##### Why average of costs from all training data? 
##### How to choose learning rate? Does the gradient magnitude gives the approximate measure for learning rate?

#### New
##### Why the change in weights and biases should be smaller, and the cost function to be more granular? 
 A: To know if we are progressing in the right direction to optimize the cost, bigger changes might change all the weights and biases in an uncontrolled manner.  
 Why introduce the quadratic cost? After all, aren't we primarily interested in the number of images correctly classified by the network? Why not try to maximize that number directly, rather than minimizing a proxy measure like the quadratic cost? The problem with that is that the number of images correctly classified is not a smooth function of the weights and biases in the network. For the most part, making small changes to the weights and biases won't cause any change at all in the number of training images classified correctly. That makes it difficult to figure out how to change the weights and biases to get improved performance. If we instead use a smooth cost function like the quadratic cost it turns out to be easy to figure out how to make small changes in the weights and biases so as to get an improvement in the cost. That's why we focus first on minimizing the quadratic cost, and only after that will we examine the classification accuracy. The expected - actual value changes even for a slight change in the weights/biases and thus the cost, for every small change in weights and biases we can check if the cost is decreasing or increasing. Number of images correctly classified will change with weights and biases but it will require major changes weights and biases compared to the quadratic cost function.
