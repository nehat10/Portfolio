#!/usr/bin/env python
# coding: utf-8
# Extract education information for consolidating data and separate out the education background by school name, year, college name, major, etc 

import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from string import punctuation
import nltk
import re
import matplotlib.pyplot as plt
from scipy import sparse


# User inputs file name( with path)
fileinput = input("Enter name of updated file(include path):")
if not ".csv" in fileinput:
    fileinput += ".csv"
import pandas as pd 
df1 = pd.read_csv(fileinput, encoding='utf-8' )

df1.head()


School_trial = df1['Student School'].tolist()


for i in range(len(School_trial)):
    print(i,School_trial[i])


df_12 = df1.groupby(['Student School']).size().reset_index(name = 'Count')




from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 20)
df1['Student School'].value_counts().plot(kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school.png')
# Final School VIZ


from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 30)
df_12.plot('Student School',kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school2.png')
# Final School VIZ



df5 = df1['Student School Year Name'].replace(regex={ 'Masters of Business Administration': 'Masters'})

from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (20, 20)
df5.value_counts().plot(kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school_year.png')
# Final school_year VIZ

from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 20)
df1['Student Primary College'].value_counts().plot(kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school_primary.png')


from pandas import Series, DataFrame
df3 =df1
df3 = (df3.set_index(df3.columns.drop('Majors',1).tolist())
           .Majors.str.split(',', expand=True)
           .stack()
           .reset_index()
           .rename(columns={0:'Majors'})
          .loc[:, df3.columns]
        )


df_14 = df1.groupby(['Student Primary College']).size().reset_index(name = 'Count')



from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 30)
df_14.plot('Student Primary College',kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school_primary2.png')



df_15 = df1.groupby(['Majors']).size().reset_index(name = 'Count')


"""from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 20)
df_15.plot('Majors',kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/majors_try.png')
#Bad representation"""




import re
my_list2 = []
sub_patterns2 = ['[A-Z][a-z]* College *[A-Z][a-z]* [A-Z][a-z]* ' ,'college *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*',
                 '[A-Z][a-z]*. [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*','[A-Z][a-z]*.[A-Z][a-z]*. [A-Z][a-z]* School [A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]*', 
                '[A-Z][a-z]* [A-Z][a-z]* College [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* College *[A-Z][a-z]* [A-Z][a-z]*'
                '[A-Z][a-z]* [A-Z][a-z]* University', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* School', 'COLLEGE OF LETTERS AND SCIENCE', '[A-Z][a-z]* College *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*',
                '[A-Z][a-z]* [A-Z][a-z]* School', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* Institute of Technology', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]*', 'college of professional and global education', 'Wharton *', 'Watson *', 'University *[a-z]* [a-z]* [A-Z][a-z]*', 'University *[a-z]* [A-Z][a-z]*', 'UC', 'UCLA *', 'The College of Arts and Sciences',
                'The College of Liberal Arts and Sciences', '[A-Z][a-z]* College of Business', '[A-Z][a-z]* School of Business', 'School of *[A-Z][a-z]* [A-Z][a-z]*', 'School of the *[A-Z][a-z]*', 'Schools of Engineering & Management','School of Visual & Perf Arts', 
                'School of The Arts and Sciences', 'School Of Information', "Saint John's University",'School of the *[A-Z][a-z]*','School of *[A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* School of *[A-Z][a-z]*', '[A-Z][a-z]* College of Engineering', '[A-Z][a-z]* College *','[A-Z][a-z]* [A-Z][a-z]* University','Bennett S. LeBow Coll. of Bus.','C.E. Schmidt Coll of Science','Clg of Nat&Soc Sciences','Col of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*'
                ,'Col *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*' ,'Col of Arts *','Col of *[A-Z][a-z]* & *[A-Z][a-z]*','Col of *[A-Z][a-z]* [A-Z][a-z]* and *[A-Z][a-z]*','Coll of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*'
                ,'Coll *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*' ,'Coll of Arts *','Coll of *[A-Z][a-z]* & *[A-Z][a-z]*','Coll of *[A-Z][a-z]* [A-Z][a-z]* and *[A-Z][a-z]*','Coll *[A-Z][a-z]* & *[A-Z][a-z]*','College of Agriculture *','College of Architecture Planning & Landscape Architect','College of Agricultural, Consumer and Environmental Sciences *','Coll *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*','Coll *[A-Z][a-z]* & [A-Z][a-z]* [A-Z][a-z]*','Coll of *[A-Z][a-z]* [A-Z][a-z]*','College Arts-Humanities','College *[A-Z][a-z]* [A-Z][a-z]*', 'College Of *[A-Z][a-z]','College Of *[A-Z][a-z]* Design',
                'College Visual/Performing Arts','College for *[A-Z][a-z]*','College of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*'
                ,'College *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*' ,'College of Arts *','College of *[A-Z][a-z]* & *[A-Z][a-z] *[A-Z][a-z]*','College of *[A-Z][a-z]* [A-Z][a-z]* and *[A-Z][a-z]*','College of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*', 'College of Business *', 'College of Communication *', 'College of *[A-Z][a-z]*', 'College of the *[A-Z][a-z]*','Colleges Letters Arts Science'
                ,'College *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*', '[A-Z][a-z]* Institute for [A-Z][a-z]*','Kellogg  School Management *','NEWARK COLLEGE OF ARTS & SCIENCES *','Middlebury *','Ira A. Fulton Schools of Engineering','[A-Z][a-z]* Schl of [A-Z][a-z]* [A-Z][a-z]*','[A-Z][a-z]* University','Columbia Engineering *','Comm.*', 'Communication*'
                ,'School of *[A-Z][a-z]* & *[A-Z][a-z]*', 'School of *[A-Z][a-z]*','Sch of *[A-Z][a-z]* and *[A-Z][a-z]*']

pattern = '({})'.format('|'.join(sub_patterns2))
index_pos_list =[]
index_pos=0
for n in df_14['Student Primary College']:
    matches = re.findall(pattern, n)
    print(matches)
    #my_list2.append(matches)
    


df_14.to_excel("/Users/neha.tandon1996/Downloads/pc_1.xlsx", index = True) 

df3.fillna("No details present", inplace=True)
import re
my_list3 = []
sub_patterns2 = ['[A-Z][a-z]* College *[A-Z][a-z]* [A-Z][a-z]* ' ,'college *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*',
                 '[A-Z][a-z]*. [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*','[A-Z][a-z]*.[A-Z][a-z]*. [A-Z][a-z]* School [A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]*', 
                '[A-Z][a-z]* [A-Z][a-z]* College [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* College *[A-Z][a-z]* [A-Z][a-z]*'
                '[A-Z][a-z]* [A-Z][a-z]* University', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* School', 'COLLEGE OF LETTERS AND SCIENCE', '[A-Z][a-z]* College *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*',
                '[A-Z][a-z]* [A-Z][a-z]* School', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* Institute of Technology', '[A-Z][a-z]* School *[A-Z][a-z]* [A-Z][a-z]*', 'college of professional and global education', 'Wharton *', 'Watson *', 'University *[a-z]* [a-z]* [A-Z][a-z]*', 'University *[a-z]* [A-Z][a-z]*', 'UC', 'UCLA *', 'The College of Arts and Sciences',
                'The College of Liberal Arts and Sciences', '[A-Z][a-z]* College of Business', '[A-Z][a-z]* School of Business', 'School of *[A-Z][a-z]* [A-Z][a-z]*', 'School of the *[A-Z][a-z]*', 'Schools of Engineering & Management','School of Visual & Perf Arts', 
                'School of The Arts and Sciences', 'School Of Information', "Saint John's University",'School of the *[A-Z][a-z]*','School of *[A-Z][a-z]* [A-Z][a-z]*', '[A-Z][a-z]* School of *[A-Z][a-z]*', '[A-Z][a-z]* College of Engineering', '[A-Z][a-z]* College *','[A-Z][a-z]* [A-Z][a-z]* University','Bennett S. LeBow Coll. of Bus.','C.E. Schmidt Coll of Science','Clg of Nat&Soc Sciences','Col of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*'
                ,'Col *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*' ,'Col of Arts *','Col of *[A-Z][a-z]* & *[A-Z][a-z]*','Col of *[A-Z][a-z]* [A-Z][a-z]* and *[A-Z][a-z]*','Coll of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*'
                ,'Coll *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*' ,'Coll of Arts *','Coll of *[A-Z][a-z]* & *[A-Z][a-z]*','Coll of *[A-Z][a-z]* [A-Z][a-z]* and *[A-Z][a-z]*','Coll *[A-Z][a-z]* & *[A-Z][a-z]*','College of Agriculture *','College of Architecture Planning & Landscape Architect','College of Agricultural, Consumer and Environmental Sciences *','Coll *[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*','Coll *[A-Z][a-z]* & [A-Z][a-z]* [A-Z][a-z]*','Coll of *[A-Z][a-z]* [A-Z][a-z]*','College Arts-Humanities','College *[A-Z][a-z]* [A-Z][a-z]*', 'College Of *[A-Z][a-z]','College Of *[A-Z][a-z]* Design',
                'College Visual/Performing Arts','College for *[A-Z][a-z]*','College of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*'
                ,'College *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*' ,'College of Arts *','College of *[A-Z][a-z]* & *[A-Z][a-z] *[A-Z][a-z]*','College of *[A-Z][a-z]* [A-Z][a-z]* and *[A-Z][a-z]*','College of *[A-Z][a-z]* [a-z]* [A-Z][a-z]*', 'College of Business *', 'College of Communication *', 'College of *[A-Z][a-z]*', 'College of the *[A-Z][a-z]*','Colleges Letters Arts Science'
                ,'College *[A-Z][a-z]* [A-Z][a-z]* and [A-Z][a-z]*', '[A-Z][a-z]* Institute for [A-Z][a-z]*','Kellogg  School Management *','NEWARK COLLEGE OF ARTS & SCIENCES *','Middlebury *','Ira A. Fulton Schools of Engineering','[A-Z][a-z]* Schl of [A-Z][a-z]* [A-Z][a-z]*','[A-Z][a-z]* University','Columbia Engineering *','Comm.*', 'Communication*'
                ,'School of *[A-Z][a-z]* & *[A-Z][a-z]*', 'School of *[A-Z][a-z]*','Sch of *[A-Z][a-z]* and *[A-Z][a-z]*']

pattern = '({})'.format('|'.join(sub_patterns2))
index_pos_list =[]
index_pos=0
for n in df3['Student Primary College']:
    matches = re.findall(pattern, n)
    print(matches)
    my_list3.append(matches)
    


df17 = DataFrame (my_list3,columns=['Student Primary College', 'Dept'])



df17 = df17.drop(['Dept'], axis=1)

df_pc = df17.groupby(['Student Primary College']).size().reset_index(name = 'Count')





from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 30)
df_pc.plot('Student Primary College',kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school_primary4.png')




from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 20)
df17['Student Primary College'].value_counts().plot(kind='bar', stacked=True)

plt.savefig(r'/Users/neha.tandon1996/Downloads/school_primary3.png')


#Majors- replace similar values for better rep(clean)
#Create final Viz's after cleaning- Majors(1)

df_15.to_excel("/Users/neha.tandon1996/Downloads/maj.xlsx", index = True) 


df_15['Majors'] = df_15['Majors'].str.upper() 





df3['Majors'] = df3['Majors'].str.upper() 
import re
my_list5 = []
sub_patterns2 = ['ARTS*', 'BIOINFORMATICS*','MANAGEMENT*','BUSINESS*','ANALYTICS *','DATA SCIENCE*','PSYCHOLOGY *','SCIENCE *','COMPUTER ENGINEERING*','ENGINEERING*','GRAPHIC DESIGN*', 'FINANCE*','JOURNALISM*','TECHNOLOGY * ','MARKETING*'
                , 'MASS COMMUNICATIONS*','MATHEMATICS*','INFORMATICS*','ECONOMIC DEV*','COMPUTING*','SCIENCES*',
                'COMPUTER SCIENCE*','DESIGN*','PHOTOGRAPHY*','EDUCATION*','ENVIRONMENTAL DESIGN*','NATURAL RESOURCES*'
                ,'FILM*','PHYSICS *','INTERNATIONAL STUDIES*','INTERNATIONAL RELATIONS*','LIFE SCIENCES*','URBAN STUDIES*','PUBLIC ADMIN*','INFORMATION SYSTEMS*','PUBLIC RELATIONS*'
                ,'MEDIA *','PROFESSIONAL STUDIES*','HUMAN DEVELOPMENT*','BEHAVIORAL SCIENCES*','COMP SCI*','TECH *','GENERAL STUDIES*','INFORMATION*','LAW *','POLITICAL SCIENCE*'
                ,'NATURAL AND AGRICULTURAL SCIENCES*','AVIATION*','INFO & COMPUTER SCIENCES*','COMPUTER SCIENCE*','PHARMACY','PUBLIC POLICY*','MEDICAL *', 'ENGLISH*'
                ,'JOURNALISM*','SECURITY & INTELLIGENCE*','FILM & TELEVISION*','INTERNATIONAL SERVICE*','ACCOUNTANCY*','ACTUARIAL SCIENCE*', ' AERONAUTICS*', 'ANTHROPOLOGY*','ANIMATION AND VISUAL EFFECTS*','AGRICULTURAL BUSINESS*','AGRICULTURAL AND APPLIED ECONOMICS*','ECONOMICS','BIOLOGY *','COGNITIVE SCIENCE*','COMMUNICATION*','HISTORY*','GLOBAL HEALTH*', 'ENVIRONMENTAL STUDIES*','LIBERAL ARTS*','MEDIA *','ENTREPRENUERSHIP*']
pattern = '({})'.format('|'.join(sub_patterns2))
index_pos_list =[]
index_pos=0
for n in df3['Majors']:
    matches = re.findall(pattern, n)
    #print(matches)
    my_list5.append(matches)
    
 

df_maj = pd.DataFrame(my_list5,columns=['C1', 'C2','C3','C4','C5','C6'])



df_maj.fillna('No details present', inplace=True)


my_list6 = []
for i in df_maj['C1']:
     my_list6.append(i)
for j in df_maj['C2']:
     my_list6.append(j)
for k in df_maj['C3']:
     my_list6.append(k)
for l in df_maj['C4']:
     my_list6.append(l)
for m in df_maj['C5']:
     my_list6.append(m)
for n in df_maj['C6']:
     my_list6.append(n)



for i in my_list6:
    print(i)


df_major2= pd.DataFrame(my_list6, columns = ['Majors'])



k=-1
df_major2 = df_major2[df_major2.Majors != 'No details present']
for elem in df_major2['Majors']:
    k=k+1
    if elem == 'TECH':
        df_major2.iloc[k]['Majors'] =  'TECHNOLOGY'
    if elem == 'SCIENCE':
        print('1',k)
        df_major2.iloc[k]['Majors'] =  'SCIENCE'
    if elem =='PUBLIC RELATION':
        df_major2.iloc[k]['Majors'] =  'PUBLIC RELATIONS'
    if elem == 'PSYCHOLOGY':
        print('2',k)
        df_major2.iloc[k]['Majors'] =  'PSYCHOLOGY'
    if elem == 'PHYSICS':
        print('3',k)
        df_major2.iloc[k]['Majors'] =  'PHYSICS'
    if elem == 'MEDIA':
        print('4',k) 
        df_major2.iloc[k]['Majors'] =  'MEDIA'
    if elem == 'MATHEMATIC':
        df_major2.iloc[k]['Majors'] =  'MATHEMATICS'
    if elem == 'MASS COMMUNICATION':
        df_major2.iloc[k]['Majors'] =  'MASS COMMUNICATIONS'
    if elem == 'LAW':
        print('5',k)
        df_major2.iloc[k]['Majors'] =  'LAW'
    if elem == 'INFORMATION SYSTEM':
        df_major2.iloc[k]['Majors'] =  'INFORMATION SYSTEMS'
    if elem == 'INFORMATION':
        df_major2.iloc[k]['Majors'] =  'INFORMATION SYSTEMS'
    if elem == 'FINANC':
        df_major2.iloc[k]['Majors'] =  'FINANCE'
    if elem == 'FILMM':
        df_major2.iloc[k]['Majors'] =  'FILM'

    if elem == 'COMP SCI':
        df_major2.iloc[k]['Majors'] =  'COMPUTER SCIENCE'
    if elem == 'ART':
        df_major2.iloc[k]['Majors'] =  'ARTS'
    if elem == 'BIOLOGY':
        print('6',k)
        df_major2.iloc[k]['Majors'] =  'BIOLOGY'
    if elem == 'ANALYTICS':
        print('7',k)
        df_major2.iloc[k]['Majors'] =  'ANALYTICS'



df_major3 = df_major2.groupby(['Majors']).size().reset_index(name = 'Count')



df_major3.to_excel("/Users/neha.tandon1996/Downloads/maj2.xlsx", index = True) 




import string
k=-1
z=0
m=-1
edit_list = []
for i in df_major3['Majors']:
    k=k+1
    m=1
    for j in df_major3[k+1:]['Majors']:
        m=k+1
        s1 = i.translate({ord(c): None for c in string.whitespace})
        s2 = j.translate({ord(c): None for c in string.whitespace})
        z=0
        if s1==s2:
            
            print(s1,s2)
            z = df_major3.iloc[m]['Count']
            print(df_major3.iloc[k]['Count'])
            print(df_major3.iloc[m]['Count'])
            print(z)
            n = z + (df_major3.iloc[k]['Count'])
            edit_list.append([k,n,m])




maj4 = df_major3.copy()
for i,j,m in edit_list:
    print(j)
    maj4.loc[i , 'Count']=  j
    




for i,j,m in edit_list:
    print(m)
    print(maj4.loc[m])
    maj4 = maj4.drop(m)




maj4 = maj4.sort_values(by=['Count'], ascending = False)
maj4.to_excel("/Users/neha.tandon1996/Downloads/maj3.xlsx", index = True)
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 30)
maj4.plot('Majors',kind='bar')

plt.savefig(r'/Users/neha.tandon1996/Downloads/major3.png')





