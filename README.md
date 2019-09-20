# PresentationScheduler


SOLUTION 1-greedy_using_priority_queue

Description:-
 ****Very Efficient Solution

  This Method uses a priority queue to store distances between nodes( presentations ) and take pair with 
  maximum distance and place it in different sessions of same time slot if overall goodness value is rising.
  This method considers 3 cases. 
 1) p1(s1,t1) and p2(any s, t2!=t1) If pair of presentations is in different time slots then find node in one
  of the pairs time slot p3(s3!=s1 , t1) or p3(s3!=s2 , t2)  such that it is at minimum distance from p1 or 
  p2(whichever in the same point) and swap with the node in different slot.
  
 2) p1(s1,t1) and p2(s2!=s1, t1) No changes required.

 3) p1(s1,t1) and p2(s1, t1) Find node p3(s3!=s1) such that it is minimum distant from any point. and swap.

 Important :- Greedy solutions many times depend on initial state. Therefore we use randomize function to 
 start algorithm from s*t*p*4 different states.



SOLUTION 2-normal_greedy_iterations

Description:-

1) This approach is using greedy approach by searching for most optimal/greedy swap (if possible) and then swap and 
doing it same again and again for considerable iterations.
2) Once again we initialized using randomized initial states as approach 1.

