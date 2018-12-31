import re

file1=open("/Users/raka/Documents/hashtag recoomendation/keywords/source/output/2011-2012/edgesList_1preprocessedCount.txt","r")
text=file1.read()

text1=re.sub('\s+\[\s*\d+\s*\]\s*',' ,, ',text)
# print(text1,"\n")


text2=text1.split(" ,, ")
text2[0]='social medium , hashtag recommendation' ## inja avalin edge ro minevisim
del text2[-1]
# print(text2,"\n")
# print(len(text2),'\n')

for s in text2:
    s1=s.split(' , ')
    t=tuple((s1[0],s1[1]))
    ind2=text2.index(s)
    text2[ind2]=t
# print(text2,"\n")
edgesList=text2
file1.close()


# file2=open('edgesList.txt','w')
# file2.write(str(text2))


file2=open("/Users/raka/Documents/hashtag recoomendation/keywords/source/output/2011-2012/edgesList_1preprocessedCount.txt","r")
text3=file2.read()

# text3=file1.read()
text3=re.sub('.*\[','',text3)
text3=re.sub('\]','',text3)
edgesCountList=text3.split('\n')
for i in range(len(edgesCountList)):
    edgesCountList[i]=int(edgesCountList[i])
file2.close()



print('\n',edgesCountList)

# file2=open('edgesCountList.txt','w')
# file2.write(str(edgesCountList))


