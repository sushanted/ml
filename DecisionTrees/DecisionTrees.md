Good source:
https://www.ke.tu-darmstadt.de/lehre/archiv/ws0809/mldm/dt.pdf

Entropy and Gain, basic understaning of decision trees:  

**Entropy:**  
https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8  
 $  -\sum_i p_i*log_2(p_i) $  
note : $ p_i $ is the probability of each target class (the one to be estimated) inside the catagory value.  

Intuition: $ - p_i*log_2(p_i) $ values are high when $ p_i $ reaches the middle (0.5), very low and very high values contribute very less in the entropy (disorder). The contribution into the entropy is proportional to the distance from the center value (0.5).  
 
 
**Gini:**  
https://www.analyticsvidhya.com/blog/2021/03/how-to-select-best-split-in-decision-trees-gini-impurity/  
$  1 - \sum_i p_i^2 $  
note : $ p_i $ is the probability of each target class (the one to be estimated) inside the catagory value.  

Intuition: exponential values increase exponentially, so higher values (as they get more farther than 0.5 to the 1 side), contribute more in the sum of squares.  
For two values, the probabilities would be p and (1-p)  
$ 1 - [ p^2 + (1-p)^2 ]  $  
$ 1 - [ p^2 + 1 - 2p + p^2 ] $  
$ 1 - 2p^2 -1 + 2p $  
$ 2p - 2p^2 $  
$ 2p(1-p) $  




**Chi square:**  
https://www.analyticsvidhya.com/blog/2021/05/implement-of-decision-tree-using-chaid/  
$ \sqrt{\frac{(x-\bar{x})^2}{\bar{x}}} $  

Intuition: If the value has same or similar distribution for the target classes (50% yes, 50% no; 33% A, 33% B, 33% C), then the attribute it noe looking good for split. But if the distributions are more skewed like (90% yes, 10% no ; 80% A, 10% B, 10%C) then they are giving good information for splitting on the current feature/attribute.  
Example:  
$ \frac{50+50}{2} = 50 $  
$ 50 - 50 = 0 $  
The chi-square formula would give 0 score for 50-50 distribution.  

$ \frac{90+10}{2} = 50 $ 90 and 10 are very apart from their mean 50  
$ 90-50 = 40 , 50-10 = 40 $  
$ \sqrt{40^2/50} + \sqrt{40^2/50} = 32 + 32 = 64 $  


** Gain ratio:**
https://machinewithdata.com/2018/07/10/how-to-calculate-gain-ratio/


Comparision :  
https://quantdare.com/decision-trees-gini-vs-entropy/  
https://towardsdatascience.com/gini-index-vs-information-entropy-7a7e4fed3fcb


Regression:  
The Target attribute is continuous (not catagorical, or say not even can be split into ranges)  
Reduction in standard deviation (SDR) can be used for splitting  
https://www.saedsayad.com/decision_tree_reg.htm

To decide an attribute to partition on among n attributes (A1,A2,A3...)   

For each attribute, weighted sum of costs (weighted sum of Entropy/Gini etc for each catagory) are calculated. Attribute with optimal weighted cost is selected for partition.






Product of contradicting terms to get the measure of purity, above functions graphs are U (or inverted U) shaped.  

Study more : 
How to do regression? regression cost functions. 
Pruning  

Algorithms:  
ID3, C4.5, C5 etc  

Gini index  
Chi squared, CART, MARS, reduction in variance  

https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html  

Advanced:  
Random forest  
XGBoost  








