dasaxosner=['grigoryan','petrosyan','hakobyan']
kurser=['k-1','k-2','k-3','k-4','k-5']
l_h=[]
l_s=[]
jamer={'grigoryan':[8,10],'petrosyan':[6,8],'hakobyan':[4,6]}
h_jamer={'grigoryan':[2,3],'petrosyan':[1,2],'hakobyan':[2,3]}
week=2
weeks=[['erkushabti'], ['ereqshabti'], ['choreqshabti'], ['hingshabti'], ['urbat']]
def dasacucak ():
    num=0
    while num<21:
        num = 0
        for j in weeks:
            for i in dasaxosner:

                if len(j) < 5:
                    count = 0
                    for c in weeks:
                        count += c.count(i)
                    if count<jamer[i][0] and len(j)<5:
                        j.append(i)
                        # if j.index(i) not in h_jamer[i]:
                        #
                        #     j[j.index(i)]=''

        for k in weeks:
            num += len(k)
    return weeks


for i in dasacucak():
    print(i[0],' '*(12-len(i[0])),i[1:5])
print('''
''')
for i in dasacucak():
    for j in range(1,len(i)):
        if j not in h_jamer[i[j]] and j<len(i)-1:
            i[j],i[j+1]=i[j+1],i[j]
        if j not in h_jamer[i[j]] and j==len(i)-1:
            i[j],i[j-1]=i[j-1],i[j]

for i in dasacucak():
    print(i[0],' '*(12-len(i[0])),i[1:5])
