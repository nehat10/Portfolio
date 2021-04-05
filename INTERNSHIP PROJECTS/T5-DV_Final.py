#!/usr/bin/env python
# coding: utf-8

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
team_df = pd.read_csv(fileinput, encoding='utf-8' )

team_df.head()


team_df2 = team_df.iloc[:, 0:7] 
# rename columns

team_df2.columns=['index','startup','team1','team2','team3','team4','team5']

# Introduce uniform team names and replace other forms
team_df2.team1 = team_df2.team1.str.replace(r'(^.*DATA SCIENCE.*$)', 'Data Science Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*DATA SCIENCE.*$)', 'Data Science Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*DATA SCIENCE.*$)', 'Data Science Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*DATA SCIENCE.*$)', 'Data Science Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*DATA SCIENCE.*$)', 'Data Science Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*data.*$)', 'Data Science Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*data.*$)', 'Data Science Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*data.*$)', 'Data Science Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*data.*$)', 'Data Science Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*data.*$)', 'Data Science Team')


team_df2.team1 = team_df2.team1.str.replace(r'(^.*Data.*$)', 'Data Science Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Data.*$)', 'Data Science Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Data.*$)', 'Data Science Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Data.*$)', 'Data Science Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Data.*$)', 'Data Science Team')





team_df2.team1 = team_df2.team1.str.replace(r'(^.*Creative.*$)', 'Creative Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Creative.*$)', 'Creative Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Creative.*$)', 'Creative Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Creative.*$)', 'Creative Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Creative.*$)', 'Creative Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*CREATIVE.*$)', 'Creative Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*CREATIVE.*$)', 'Creative Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*CREATIVE.*$)', 'Creative Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*CREATIVE.*$)', 'Creative Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*CREATIVE.*$)', 'Creative Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*Communication.*$)', 'Creative Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Communication.*$)', 'Creative Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Communication.*$)', 'Creative Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Communication.*$)', 'Creative Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Communication.*$)', 'Creative Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*COMMUNICATION.*$)', 'Creative Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*COMMUNICATION.*$)', 'Creative Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*COMMUNICATION.*$)', 'Creative Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*COMMUNICATION.*$)', 'Creative Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*COMMUNICATION.*$)', 'Creative Team')



team_df2.team1 = team_df2.team1.str.replace(r'(^.*Project.*$)', 'PM')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Project.*$)', 'PM')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Project.*$)', 'PM')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Project.*$)', 'PM')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Project.*$)', 'PM')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*PROJECT.*$)', 'PM')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*PROJECT.*$)', 'PM')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*PROJECT.*$)', 'PM')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*PROJECT.*$)', 'PM')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*PROJECT.*$)', 'PM')





team_df2.team1 = team_df2.team1.str.replace(r'(^.*BUSINESS.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*BUSINESS.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*BUSINESS.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*BUSINESS.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*BUSINESS.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*Business.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Business.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Business.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Business.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Business.*$)', 'Business Team')


team_df2.team1 = team_df2.team1.str.replace(r'(^.*Marketing.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Marketing.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Marketing.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Marketing.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Marketing.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*MARKETING.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*MARKETING.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*MARKETING.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*MARKETING.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*MARKETING.*$)', 'Business Team')


team_df2.team1 = team_df2.team1.str.replace(r'(^.*Sales.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Sales.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Sales.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Sales.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Sales.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*SALES.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*SALES.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*SALES.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*SALES.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*SALES.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*Customer.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Customer.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Customer.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Customer.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Customer.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*CUSTOMER.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*CUSTOMER.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*CUSTOMER.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*CUSTOMER.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*CUSTOMER.*$)', 'Business Team')


team_df2.team1 = team_df2.team1.str.replace(r'(^.*Research.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Research.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Research.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Research.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Research.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*RESEARCH.*$)', 'Business Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*RESEARCH.*$)', 'Business Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*RESEARCH.*$)', 'Business Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*RESEARCH.*$)', 'Business Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*RESEARCH.*$)', 'Business Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*Develop.*$)', 'Developers Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Develop.*$)', 'Developers Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Develop.*$)', 'Developers Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Develop.*$)', 'Developers Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Develop.*$)', 'Developers Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*DEVELOP.*$)', 'Developers Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*DEVELOP.*$)', 'Developers Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*DEVELOP.*$)', 'Developers Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*DEVELOP.*$)', 'Developers Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*DEVELOP.*$)', 'Developers Team')


team_df2.team1 = team_df2.team1.str.replace(r'(^.*Design.*$)', 'Developers Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Design.*$)', 'Developers Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Design.*$)', 'Developers Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Design.*$)', 'Developers Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Design.*$)', 'Developers Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*DESIGN.*$)', 'Developers Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*DESIGN.*$)', 'Developers Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*DESIGN.*$)', 'Developers Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*DESIGN.*$)', 'Developers Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*DESIGN.*$)', 'Developers Team')


team_df2.team1 = team_df2.team1.str.replace(r'(^.*Visualization.*$)', 'Developers Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*Visualization.*$)', 'Developers Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*Visualization.*$)', 'Developers Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*Visualization.*$)', 'Developers Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*Visualization.*$)', 'Developers Team')

team_df2.team1 = team_df2.team1.str.replace(r'(^.*VISUALIZATION.*$)', 'Developers Team')
team_df2.team2 = team_df2.team2.str.replace(r'(^.*VISUALIZATION.*$)', 'Developers Team')
team_df2.team3 = team_df2.team3.str.replace(r'(^.*VISUALIZATION.*$)', 'Developers Team')
team_df2.team4 = team_df2.team4.str.replace(r'(^.*VISUALIZATION.*$)', 'Developers Team')
team_df2.team5 = team_df2.team5.str.replace(r'(^.*VISUALIZATION.*$)', 'Developers Team')


team_df4 = pd.DataFrame(columns =['index','startup','team1','team2','team3','team4','team5'])
# Separate every startup for each person in a row and add team names as columns
from pandas import Series, DataFrame
team_df5 =team_df2
team_df5 = (team_df5.set_index(team_df5.columns.drop('startup',1).tolist())
           .startup.str.split(',', expand=True)
           .stack()
           .reset_index()
           .rename(columns={0:'startup'})
          .loc[:, team_df5.columns]
        )

team_matrix = pd.DataFrame(columns =['index','startup','Data Science Team','Business Team','PM','Developers Team','Creative Team'])
df= team_df5['startup'].unique().tolist()
del df[-9:]

team_matrix['startup'] = df

DATA_TEAM =0
CREATIVE_TEAM =0
DEVELOPERS_TEAM =0
BUSINESS_TEAM =0
PM =0
id=[]
id2=0
for elem in team_matrix['startup']:
    print(elem)
    id = []
    DATA_TEAM =0
    CREATIVE_TEAM =0
    DEVELOPERS_TEAM =0
    BUSINESS_TEAM =0
    PM =0
    
                 
    id = team_df5['startup'].loc[lambda x: x==elem].index
            
    for k in id:
                
                if team_df5.loc[k, 'team1'] == 'Data Science Team': #Correct it
                    DATA_TEAM = DATA_TEAM +1
                if team_df5.loc[k, 'team1']== 'Creative Team':
                    CREATIVE_TEAM = CREATIVE_TEAM +1
                if team_df5.loc[k, 'team1']== 'Business Team':
                    BUSINESS_TEAM = BUSINESS_TEAM +1
                if team_df5.loc[k, 'team1']== 'Developers Team':
                    DEVELOPERS_TEAM = DEVELOPERS_TEAM +1
                if team_df5.loc[k, 'team1']== 'PM':
                    PM = PM +1
                    
                if team_df5.loc[k, 'team2'] == 'Data Science Team': #Correct it
                    DATA_TEAM = DATA_TEAM +1
                if team_df5.loc[k, 'team2']== 'Creative Team':
                    CREATIVE_TEAM = CREATIVE_TEAM +1
                if team_df5.loc[k, 'team2']== 'Business Team':
                    BUSINESS_TEAM = BUSINESS_TEAM +1
                if team_df5.loc[k, 'team2']== 'Developers Team':
                    DEVELOPERS_TEAM = DEVELOPERS_TEAM +1
                if team_df5.loc[k, 'team2']== 'PM':
                    PM = PM +1
                    
                if team_df5.loc[k, 'team3'] == 'Data Science Team': #Correct it
                    DATA_TEAM = DATA_TEAM +1
                if team_df5.loc[k, 'team3']== 'Creative Team':
                    CREATIVE_TEAM = CREATIVE_TEAM +1
                if team_df5.loc[k, 'team3']== 'Business Team':
                    BUSINESS_TEAM = BUSINESS_TEAM +1
                if team_df5.loc[k, 'team3']== 'Developers Team':
                    DEVELOPERS_TEAM = DEVELOPERS_TEAM +1
                if team_df5.loc[k, 'team3']== 'PM':
                    PM = PM +1
                    
                if team_df5.loc[k, 'team4'] == 'Data Science Team': #Correct it
                    DATA_TEAM = DATA_TEAM +1
                if team_df5.loc[k, 'team4']== 'Creative Team':
                    CREATIVE_TEAM = CREATIVE_TEAM +1
                if team_df5.loc[k, 'team4']== 'Business Team':
                    BUSINESS_TEAM = BUSINESS_TEAM +1
                if team_df5.loc[k, 'team4']== 'Developers Team':
                    DEVELOPERS_TEAM = DEVELOPERS_TEAM +1
                if team_df5.loc[k, 'team4']== 'PM':
                    PM = PM +1
                    
                if team_df5.loc[k, 'team5'] == 'Data Science Team': #Correct it
                    DATA_TEAM = DATA_TEAM +1
                if team_df5.loc[k, 'team5']== 'Creative Team':
                    CREATIVE_TEAM = CREATIVE_TEAM +1
                if team_df5.loc[k, 'team5']== 'Business Team':
                    BUSINESS_TEAM = BUSINESS_TEAM +1
                if team_df5.loc[k, 'team5']== 'Developers Team':
                    DEVELOPERS_TEAM = DEVELOPERS_TEAM +1
                if team_df5.loc[k, 'team5']== 'PM':
                    PM = PM +1
    print(DATA_TEAM,BUSINESS_TEAM,PM,CREATIVE_TEAM,DEVELOPERS_TEAM)
    id2 = team_matrix['startup'].loc[lambda x: x==elem].index
    team_matrix.loc[id2, 'Data Science Team'] = DATA_TEAM
    team_matrix.loc[id2, 'Business Team'] = BUSINESS_TEAM
    team_matrix.loc[id2, 'Creative Team'] = CREATIVE_TEAM
    team_matrix.loc[id2, 'Developers Team'] = DEVELOPERS_TEAM
    team_matrix.loc[id2, 'PM'] = PM 
 
# For every startup name, count the number of people interested in each of its teams.
team_matrix = team_matrix.drop('index', axis=1)
team = team_matrix
import string
id3=0
def cmp(a, b):
     return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
k=0
for i in team_matrix['startup']:
    
    k=k+1
    
    for elem in team_matrix[k:]['startup']:
        
        if cmp(i,elem):
            print('Hi')
            print(elem,i)
            id3 = team_matrix['startup'].loc[lambda x: x==elem].index
            team_matrix.loc[id3, 'startup'] = i
                # replace elem with i


team_trial = team_matrix['startup'].tolist()
team_trial



team_final2 = pd.DataFrame(columns =['startup','Data Science Team','Business Team','PM','Developers Team','Creative Team'])

team_try = team_matrix
id = []
count1=0
count2=0
count3=0
count4=0
count5=0
for elem in team_try['startup'].unique():
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    print(elem)
    id = team_try['startup'].loc[lambda x: x==elem].index
    for k in id:
            count1 = count1 + team_try.loc[k, 'Data Science Team']               
            count2 = count2 + team_try.loc[k, 'Business Team']
            count3 = count3 + team_try.loc[k, 'PM']
            count4 = count4 + team_try.loc[k, 'Developers Team']
            count5 = count5 + team_try.loc[k, 'Creative Team']
    new_row = {'startup': elem, 'Data Science Team': count1, 'Business Team': count2, 'PM': count3, 'Developers Team': count4, 'Creative Team':count5}
    team_final2 = team_final2.append(new_row, ignore_index=True)

team_final2 = team_final2[:-1]
team_final2.to_excel (r'/Users/neha.tandon1996/Downloads/matrix.xlsx', index = True, header=True)
# Show team wise, startup wise popularity
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (200, 20)
team_final2.plot('startup',kind='bar', stacked=True)

plt.title("Popularity")
fileinput2 = input("Enter path to save file:")
plt.savefig(fileinput2, encoding='utf-8')






