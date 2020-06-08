import pandas as pd
import numpy as np
import glob


class Data():
    try:
        '''create class rooms fake numbers'''

        classrooms_list={'lecture':[2101+(i*2) for i in range(16)],'practical':[2102+(i*2) for i in range(10)]}


        '''list from data directory files'''

        mylist = [f for f in glob.glob("../data/*.xlsx")]


        '''read excel files and create matrix'''

        all_dates=[]
        for i in mylist:
            dataframe = pd.read_excel(i)
            # dataframe=dataframe.dropna(how='all')
            all_dates.append(dataframe)

        '''the sum of hours'''

        issum=0
        for i in all_dates:
            for j in i['Unnamed: 8']:
                if type(j)==int:
                    issum+=j


        '''group division number'''

        divide_num=13

    except PermissionError as e:
        print(e)
        print("Please close the excel file.\n")
        input('Press Enter and try again')

    def __init__(self):

        classroom_schedule=self.classroom_schedule(self.classrooms_list)
        teache_schedule=self.teachers_schedule()
        with pd.ExcelWriter('../output/schedule.xlsx', engine='openpyxl') as writer:
            fog=self.for_one_group()[0]
            for gr in range(len(fog)):

                self.xumb=str(fog[gr])
                group_hours=self.group_hours()

                empty=self.create_week()
                scheulde=self.group_data(group_hours,empty,classroom_schedule,teache_schedule)
                group_scheulde=scheulde[0]
                teache_schedule=scheulde[1]
                for i in range(len(group_scheulde)):

                    group_scheulde[i].to_excel(writer,sheet_name=fog[gr],startrow=i*5)
        # print(teache_schedule['Գրիգորյան Ա'])
        # teache_schedule['Գրիգորյան Ա'][0].to_excel('teacher1.xlsx',  startrow=i * 5)
        #
        # teache_schedule['Գրիգորյան Ա'][1].to_excel('teacher2.xlsx',  startrow=i * 5)

    def create_week(self):

        '''create empty class schedule for two weeks'''

        days = ["mon", "tue", "wed", "thu", "fri"]
        empty_df = pd.DataFrame(data=[[None for i in range(5)]],columns=days,index=[i for i in range(1,5)])
        return [empty_df,empty_df.copy()]

    def for_one_group(self):
        groups=[i['Unnamed: 2'].values for i in self.all_dates]
        groups=[i[7:] for i in groups]
        groups=[np.unique(i) for i in groups]

        return groups

    def classroom_schedule(self,class_list):

        classrooms_l = [i for i in class_list['lecture']]
        classrooms_p = [i for i in class_list['practical']]
        classroom_schedule={'lecture':{},'practical':{}}
        for i in classrooms_l:
            classroom_schedule['lecture'].update({str(i): self.create_week()})
        for i in classrooms_p:
            classroom_schedule['practical'].update({str(i): self.create_week()})

        return classroom_schedule

    def teachers_schedule(self):
        teachers = [i['Unnamed: 9'].values for i in self.all_dates]
        teachers = [i[7:] for i in teachers]
        for i in teachers[0]:
            if type(i) != float:
                i=np.unique(i)
        teacher_schedule = {}
        for i in teachers[0]:
            if type(i)!=float:
                teacher_schedule.update({str(i): self.create_week()})
        return teacher_schedule



    def group_hours(self):

        lessons={}
        general=0
        lecture=0
        practical=0

        for file in self.all_dates:
            for row in range(len(file['Unnamed: 2'])):
                if file['Unnamed: 2'][row]==self.xumb:
                    if file['Unnamed: 3'][row]>self.divide_num:
                        divide=True
                    general+=file['Unnamed: 8'][row]
                    lecture+=file['Unnamed: 5'][row]
                    practical += file['Unnamed: 6'][row]
                    les_name=file['Unnamed: 1'][row]

                    if type(file['Unnamed: 1'][row])==float:
                        les_name=file['Unnamed: 1'][row-1]

                    if type(file['Unnamed: 9'][row]) == float:
                        for i in range(row):
                            if file['Unnamed: 9'][row-i]!=float:
                                file['Unnamed: 9'][row]=file['Unnamed: 9'][row-i]
                                break
                    teacher_name = file['Unnamed: 9'][row]
                    dictionary={les_name:{'group':file['Unnamed: 2'][row],
                                          'teacher': teacher_name,
                                          'general':file['Unnamed: 8'][row],
                                          'lecture':file['Unnamed: 5'][row],
                                          'practical': file['Unnamed: 6'][row],
                                          'general_week':(file['Unnamed: 8'][row]*2)/16,
                                          'lecture_week':(file['Unnamed: 5'][row]*2)/16,
                                          'practical_week':(file['Unnamed: 6'][row]*2)/16}}
                    lessons.update(dictionary)

        # if divide:
        #     practical=practical*2
        return {'lessons':lessons,'general':general,'lecture':lecture,'practical':practical,'general_week':(general*2)/16,'lecture_week':(lecture*2)/16,'practical_week':(practical*2)/16}


    def group_data(self,data,empty_schedule,classroom_schedule,teacher_schedule):
        group_schielde=empty_schedule.copy()

        for week in range(len(group_schielde)):
            for ararka in data['lessons'].keys():
                for jam in range(int(data['lessons'][ararka]['general_week'])):
                    for day in ["mon", "tue", "wed", "thu", "fri"]:
                        for hour in range(len(group_schielde[week][day])):
                            if group_schielde[week][day][hour+1]==None \
                                    and (classroom_schedule['lecture'][str(self.classrooms_list['lecture'][0])][week][day][hour+1]==None
                                    or classroom_schedule['practical'][str(self.classrooms_list['practical'][0])][week][day][hour+1]==None)\
                                    and teacher_schedule[str(data['lessons'][ararka]['teacher'])][week][day][hour+1]==None:



                                teacher_schedule[str(data['lessons'][ararka]['teacher'])][week][day][hour + 1]=str(ararka)+' \r\n'+str(data['lessons'][ararka]['group'])

                                if data['lessons'][ararka]['general_week'] > 0 :
                                    group_schielde[week][day][hour+1]=str(ararka)+' \r\n'+str(data['lessons'][ararka]['group'])+' \r\n'+str(data['lessons'][ararka]['teacher'])
                                    data['lessons'][ararka]['general_week']-=1
                                    if data['lessons'][ararka]['lecture_week']>0:

                                        data['lessons'][ararka]['lecture_week']-=1
                                        group_schielde[week][day][hour + 1]+=' \r\n'+str(self.classrooms_list['lecture'][0])+' lecture'
                                    elif data['lessons'][ararka]['practical_week']>0:

                                        data['lessons'][ararka]['practical_week']-=1
                                        group_schielde[week][day][hour + 1] +=' \r\n'+ str(self.classrooms_list['practical'][0])+' practical'

                                break
                    if (int(data['lessons'][ararka]['general_week'])==0):
                        break
        self.classrooms_list['lecture'] = self.classrooms_list['lecture'][1:]
        self.classrooms_list['practical'] = self.classrooms_list['practical'][1:]

        return group_schielde,teacher_schedule
try:
    obj=Data()
except IndexError:

    print("""Files were not found,\nplease make sure that all\nthe necessary files are\nin the Data folder.\n""")
    input('Press Enter and try again')
except Exception as e:
    print(e)
    input('Press Enter and try again')
