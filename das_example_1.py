list = ['mek', 'erku', 'ereq', 'chors', 'hing','vec']

time = {'mek': 10, 'erku': 10, 'ereq': 6, 'chors': 3, 'hing': 1,'vec':10}
time2 = {'mek': 10, 'erku': 10, 'ereq': 6, 'chors': 3, 'hing': 1,'vec':10}


def func():
    x = 0.5
    while sum(time.values()) != 0:

        week = []
        for j in range(5):
            day = []
            for s in range(4):
                for k in range(len(list)):
                    if time2[list[k]] * x < time[list[k]]:
                        day.append(list[k])
                        time[list[k]] -= 1
                        break
            if len(day) > 0:
                week.append(day)

        x = 0
        yield week
for i in func():
    for j in i:
        print(j)
    print('***************')
# da=[]
# m=[[],[],[],[],[]]
# for i in func():
#     if len(i[0])<4:
#         for j in range(len(m)):
#             m[j]+=i[j]
#     else:
#         da.append(i)
# print('\n')
# da.append(m)
# for i in range(len(da)-1):
#     for j in range(len(da[i])) :
#         if len(da[i][j])<4 and len(da[i][j])+len(da[-1][-1])==4:
#             da[i][j]+=da[-1][-1]
#             del da[-1][-1]
#         elif len(da[i][j])<4 and len(da[i][j])+len(da[-1][-1])!=4:
#             da[i][j].append('mek')
#
#
# for i  in da:
#     for j in i:
#         print(j)
#     print('***************')
#






