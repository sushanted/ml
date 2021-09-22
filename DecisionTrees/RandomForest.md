Random forest basics:
https://www.youtube.com/watch?v=J4Wdy0Wc_xQ

Missing data in random forest:
https://www.youtube.com/watch?v=nyxTdL_4Q-Q

For the record with the missing data, create random trees.

Check in how many trees the missing-data-record lands at the same leaf as the other records. Track this for each other record. We can say that the missing-data-record is similar to the other records landing at the same leaf for n trees, as it is going to the same leaf node, it should have all "significant" (for the decision tree) feature values same (intermediate nodes). The number n can be treated as the similarity between the missing-data-record and the other record, more the n, more the similarity. This n can be normalized by dividing it by total number of similarities found. So we can say missing-data-record is 10% similar to record A, 30% with Record B and 60% with Record C (Total 100%). So record C is more similar. 

For catagorical attributes 

