# Presentation Scheduler

Organizers of a workshop need your help in scheduling the presentations. There are
total N presentation to be scheduled in S parallel sessions. Each session is divided uniformly in T time slots and each time slot has P presentation. For example, in     Table 1 the schedule shows S = 3, T = 2, and P = 4, s.t. N = T × S × P = 24 presentations.
`Table 1: Example`

||Time Slot 1|Time Slot 1|
|------|-----|-----|
|Session 1|p1, p2, p3, p4 |p5, p6, p7, p8|
|Session 2|p9, p10, p11, p12| p13, p14, p15, p16|
|Session 3|p17, p18, p19, p20| p21, p22, p23, p24|
Desirable attributes of a good schedule
1. All presentations in one session should be on a single theme.
2. All presentations in parallel sessions should be on themes as far away as possible to avoid conflict.

Let us assume d(1, 2) represents distance between the themes of the presentations p1
and p2, s.t. d(1, 2) = d(2, 1). Further, let us assume d is in the range [0, 1]. Accordingly the similarity between the themes of the presentations p1 and p2 is measured as u(1, 2) = 1 − d(1, 2).

Let us now define goodness of a schedule Sch as
G(Sch) =sX=Ss=1Xt=Tt=1XC0(i,j)s.t. i,j∈si6=j u(i, j) + Z × Xt=Tt=1XC1(i,j) s.t. i∈s,j /∈s d(i, j) (1)

- where C0(i, j) represents “all pairs of presentations with same session and slot” and C1(i, j)represents “all pairs of presentations in same slot but in different (parallel) sessions”. 

*For Table 1:*
`G(Sch) = u(1, 2) + u(1, 3) + u(1, 4) + u(2, 3) + u(2, 4) + u(3, 4)+u(5, 6) + u(5, 7) + ...+ Z × [d(1, 9) + d(1, 10) + ... + d(1, 17) + d(2, 18) + ...+ d(5, 13) + ... + d(13, 21) + ...]`

The constant Z trades-off the importance of semantic coherence of one session versus
reducing conflict across parallel sessions.
##### Our goal is to model the problem as a searching problem and find the schedule with the maximum goodness.

`SOLUTION 1`- *Greedy using priority queue*

## Description:-
This Method uses a priority queue to store distances between nodes( presentations ) and take pair with maximum distance and place it in different sessions of same time slot if overall goodness value is rising. This method considers `3 cases`.

- `p1(s1,t1) and p2(any s, t2!=t1)` If pair of presentations is in different time slots then find node in one of the pairs time slot p3(s3!=s1 , t1) or p3(s3!=s2 , t2) such that it is at minimum distance from p1 or p2(whichever in the same point) and swap with the node in different slot.

- `p1(s1,t1) and p2(s2!=s1, t1)` No changes required.

- `p1(s1,t1) and p2(s1, t1)` Find node p3(s3!=s1) such that it is minimum distant from any point. and swap.

`
Important :- Greedy solutions many times depend on initial state. Therefore we use randomize function to start algorithm from stp*4 different states.
`


`SOLUTION 2`- *Normal greedy iterations*

Description:-

- This approach is using greedy approach by searching for `most optimal/greedy swap` (if possible) and then swap and doing it same again and again for considerable iterations.
- Once again we initialized using randomized initial states as approach 1.




