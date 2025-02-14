import work_a1m
import pandas as pd
DATE_OF_TEST='DATE'
find_roll=242007    #could be 'All'
Subjects=['PHYSICS','CHEMISTRY','MATHEMATICS']
PHYSICS=[]
CHEMISTRY=[]
MATHEMATICS=['Relations and Functions (PUC-I)','Trigonometric Functionsv (PUC-I)','Linear Inequalities (PUC-I)','Limits and Derivatives (PUC-I)',
'Relations and Functions (PUC-II)','Matrices (PUC-II)','Determinants (PUC-II)','Continuity and Differentiability (PUC-II)']
#1. Average of each chapter from diff tests (tupled with chapter_name)
#2. Average of all the tests (avg of 1)
#3. Average of all students
#4. Average of each test (tupled with date and test_id)
#5. Max of a chapter from all the tests. (tupled with date and id)
#6. Max of avg from all chapters. (tupled with date and id)
#7. Max from 1 test (tupled with date id and chapter name)
def calculate_average_of_each_chapter_individual(data_by_roll_no):
    subjectwise_chapter_average_individual={}
    for ssubject in Subjects:
        temp={}
        for chapter_name in eval(ssubject):
            returning_value=[]
            for i in range(len(data_by_roll_no)):
                if data_by_roll_no['Chapter_Name'][i]==chapter_name:
                    returning_value.append(data_by_roll_no['Marks_Scored'][i])
            try:
                temp[chapter_name]=round(sum(returning_value)/len(returning_value))
            except ZeroDivisionError:
                pass
        subjectwise_chapter_average_individual[ssubject]=temp
    return subjectwise_chapter_average_individual

def calculate_average_of_each_chapter_class(data_by_roll_no):
    chapter_name='Relations and Functions (PUC-I)'
    

def main():
    expanded_scorelist=pd.read_excel('Resources/expanded_scorelist.xlsx')
    roll_no=[]
    for index in range(len(expanded_scorelist)): #replace with: range(len(expanded_scorelist))
        roll_no.append(expanded_scorelist["CANDIDATE ID"][index])
    avg_values_all_students=[]
    performance_avg_of_all_students=[]
    for roll in roll_no:
        performance_avg_of_student={}
        for subject in Subjects:
            subject_inp=subject
            try:
                path_of_data=f'Data/{subject_inp}'
                data_by_roll_no=pd.read_csv(path_of_data+f'/{roll}.csv')
                value_of_1=calculate_average_of_each_chapter_individual(data_by_roll_no)
                avg_values_all_students.append(value_of_1) # THIS IS AVG OF ALL STUDENTS PER CHAPTER
                performance_avg_of_student[subject]=(int(roll),DATE_OF_TEST,round(sum(data_by_roll_no['Marks_Scored'])/(len(data_by_roll_no['Marks_Scored']))))
                # print(performance_avg_of_student) THIS SHIT IS AVERAGE OF STUDENT IN ALL THE TEST HE HAS WRITTTEN SUBJECTWISE
            except FileNotFoundError:
                performance_avg_of_student[subject]=(int(roll),DATE_OF_TEST,0)
        performance_avg_of_all_students.append(performance_avg_of_student)
    # print(performance_avg_of_all_students) AVERAGE OF STUDENT IN ALL THE TEST
    avg_of_whole_class={}
    for performance_avg_of_student in performance_avg_of_all_students:
        for subject in Subjects:
            val=[]
            val.append(performance_avg_of_student[subject][2])
            avg_of_whole_class[subject]=(DATE_OF_TEST,round(sum(val)/len(val)))
    print(avg_of_whole_class)
    class_avg_each_chap={}
    for subject in Subjects:
        subject_avg={}
        for chapter in eval(subject):
            val=[]
            for individual_student_avg_dict in avg_values_all_students:
                val.append(individual_student_avg_dict[subject][chapter])
            subject_avg[chapter]=round(sum(val)/len(val))
        class_avg_each_chap[subject]=subject_avg

    # print(class_avg_each_chap) THIS IS AVG OF THE CLASS CHAPTERWISE


# print(calculate_average_of_each_chapter_individual(data_by_roll_no))
main()