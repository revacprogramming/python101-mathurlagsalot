# Functions


  def computepay(h,r):
    if h>40:
        p = 1.5*r*(h-40) + (40*r)
    else:
        p = h*r
    return p

hrs = float(input ("Enter hours: "))
rper = float(input("Enter rate per hour: "))

pr = computepay(hrs,rper)
print("Pay",pr)
             
