# Files

f = input("Enter the file name: ")
fileop = open(f)
c = 0
s = 0
for i in f:
    if i.startswith("X-DSPAM-Confidence"):
        c = c + 1
        n = float(i[20::1])
        s = s + n
    avg = s/(c)
    print("Average spam confidence: ", avg)
  