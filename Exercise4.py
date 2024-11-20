a = int(input("Enter 1 for Coding and 0 for Decoding."))
st = input("Enter Message.")
words = st.split(" ")

if(a == 1 ):
    coding = True
elif(a == 0):
    coding = False

if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dfd"
            r2 = "fnd"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))