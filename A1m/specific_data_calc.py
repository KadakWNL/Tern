import pandas as pd
subject='MATHEMATICS'
path_of_data=f'Data/{subject}'
find_roll=242007    #could be 'All'
#1. Average of each chapter from diff tests (tupled with chapter_name)
#2. Average of all the tests (avg of 1)
#3. Average of all students
#4. Average of each test (tupled with date and test_id)
#5. Max of a chapter from all the tests. (tupled with date and id)
#6. Max of avg from all chapters. (tupled with date and id)
#7. Max from 1 test (tupled with date id and chapter name)
def calculate_average_of_each_chapter_individual(data_by_roll_no):
    for chapter in 
    returning_value=[]
    for i in range(len(data_by_roll_no)):
        if data_by_roll_no['Chapter_Name'][i]==chapter_name:
            returning_value.append(data_by_roll_no['Marks_Scored'][i])
    return(round(sum(returning_value)/len(returning_value)),chapter_name)

def calculate_average_of_each_chapter_class(data_by_roll_no):
    chapter_name='Relations and Functions (PUC-I)'


def main():
    expanded_scorelist=pd.read_excel('Resources/expanded_scorelist.xlsx')
    roll_no=[]
    for index in range(len(expanded_scorelist)): #replace with: range(len(expanded_scorelist))
        if find_roll=='All':
            roll_no.append(expanded_scorelist["CANDIDATE ID"][index])
        elif find_roll==expanded_scorelist["CANDIDATE ID"][index]:
            roll_no.append(expanded_scorelist["CANDIDATE ID"][index])
    if roll_no==[]:
        print("Not such roll number found.")
    else:
        for roll in roll_no:
            data_by_roll_no=pd.read_csv(path_of_data+f'/{roll}.csv')
    option=input("what do u want 1-7")
    #=====IF THE OPTION IS LIKE 1.2 or 2.2 similarly it means that it is for calculation of all the class :> #======
    if option=='1':
        value_of_1=calculate_average_of_each_chapter_individual(data_by_roll_no)
    if option=='1.2':
        value_of_12=calculate_average_of_each_chapter_class(data_by_roll_no)
    
data_by_roll_no=pd.read_csv(path_of_data+f'/242001.csv')
print(calculate_average_of_each_chapter_individual(data_by_roll_no))