#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""

q=input("Enter in price of item:")
#convert to a number
q=float(q)
q=round(q,2)

w=input("Enter in price of item:")
#convert to a number
w=float(w)
w=round(w, 2)

e=input("Enter in price of item:")
#convert to a number
e=float(e)
e=round(e, 2)

r=input("Enter in price of item:")
#convert to a number
r=float(r)
r=round(r,2)

t=input("Enter in price of item:")
#convert to a number
t=float(t)
t=round(t,2)

subtotal=q+w+e+r+t
#convert to a number
subtotal=float(subtotal)

gst= subtotal*0.05
#convert to a number
gst=float(gst)

pst= subtotal*0.07
#convert to a number
pst= float(pst)


total= subtotal+ gst+ pst
#convert to a number
total=float(total)


gst = round(subtotal * 0.05, 2)
pst = round(subtotal * 0.07, 2)
total = round(subtotal + gst + pst, 2)

print(f"The subtotal:{subtotal:.2f}")
print(f"GST at 5%: {gst:.2f}")
print(f"PST at 7%: {pst:.2f}")
print(f"Total: {total:.2f}")
