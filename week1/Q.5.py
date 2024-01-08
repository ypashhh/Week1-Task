'''The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is 24 students, since this is the
number of PCs in a lab. Write a program that calculates how many groups are
needed for the following number of students: 113, 175, 12. Display how many full
groups there will be, and how many students will be in the smaller "left over"
group'''

group1=113
group2=175
group3=12
size=24

l1=group1//size
l1left=group1%size
print(f"groups {l1} and left over students is {l1left}")

l2=group2//size
l2left=group2%size
print(f"groups {l2} and left over students is {l2left}")

l3=group3//size
l3left=group3%size
print(f"groups {l3} and left over students is {l3left}")

