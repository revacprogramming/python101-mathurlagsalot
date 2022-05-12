# Strings


str = "X-DSPAM-Confidence:    0.8475"
stringind = str.find("0.8475")
ans = str[stringind::1]
res = float(ans)
print(res)
