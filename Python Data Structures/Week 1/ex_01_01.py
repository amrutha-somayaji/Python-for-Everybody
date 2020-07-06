text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(' ')
fnum=float(text[23:29])
print(fnum)
