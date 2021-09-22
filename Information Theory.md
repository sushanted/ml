Information content: why negative log of probability?

https://towardsdatascience.com/information-content-the-logic-behind-it-4e6d6e625240

Information content is inversely proportional to the probability of event and more thought of as the surprise value. Less probable events convey more information, more probable events convey less information.  

IC = $ -log_2(p) = log_2(\frac{1}{p}) $  

Entropy is the total information in the system:  

Suppose there are 1 red, 10 green and 89 blue balls in a box.  

p(R) = $ \frac{1}{100} $  

p(G) = $ \frac{10}{100} $  

p(B) = $ \frac{89}{100} $  

IC(R) > IC(G) > IC(B)  

IC(R) = $ -log_2(\frac{1}{100}) $  = 6.64  
IC(G) = $ -log_2(\frac{10}{100}) $ = 3.32  
IC(B) = $ -log_2(\frac{89}{100}) $ = 0.17  

total red balls info = 1 * 6.64 = 6.64  
total green balls info = 10 * 3.32 = 33.2  
total blue balls info = 89 * 0.17 = 15.13  

total info = 6.64 + 33.2 + 15.13 = 54.97

mean OR average OR expected info value = $ \frac{54.97}{100} = 0.5497 $ 

expected value for info = $ \frac{1 * 6.64 + 10 * 3.32 + 89 * 0.17}{100} $  

 = $ \frac{1 * 6.64}{100} + \frac{10 * 3.32}{100} + \frac{89 * 0.17}{100} $  
 
 = 0.01 * 6.64 + 0.1 * 3.32 + 0.89 * 0.17  
 
 Note here n was 100 ,but it is applicable in general
 
 = p(R) * 6.64 + p(G) * 3.32 + p(B) * 0.17  
 
 = p(R)* IC(R) + p(G)* IC(G) + p(B) * IC(B)  
 
 = $ p(R) * -log_2(p(R)) + p(G) * -log_2(p(G)) + p(G) * -log_2(p(G)) $ 
 
 
 Generically, Expected value for info: 
 
 = $ \sum - p(x)log_2(p(x)) $   
 
 = $ - \sum p(x)log_2(p(x)) $   
 
 









