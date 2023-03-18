sentences = ["a new world record was set", "in the holy city of ayodhya",

"on the eve of diwali on tuesday",

"with over three lakh diya or earthen lamps",

"lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in','on', 'with']
l1=[]
for i in sentences:
    for j in i.split():
        if j not in stopwords:
            l1.append(j)
print(l1)
print()
print([[word for word in sentences.split() if word not in stopwords]for sentence in sentences])
