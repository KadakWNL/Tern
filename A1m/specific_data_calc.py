import pandas as pd
from pprint import pprint
from collections import defaultdict
import os
import time


test_data=pd.read_csv(r'Data\Metadata\test_metadata.csv')
DATE_OF_TEST='DATE'
current_test_id=690 #Get input from user (dashboard)
find_roll=242007    #could be 'All'
subject='MATHEMATICS'  #From dashboard
path_of_data=f'Data/{subject}'
Subjects=['PHYSICS','CHEMISTRY','MATHEMATICS']
PHYSICS=[]
CHEMISTRY=[]
MATHEMATICS=['Relations and Functions (PUC-I)','Trigonometric Functionsv (PUC-I)','Linear Inequalities (PUC-I)','Limits and Derivatives (PUC-I)',
'Relations and Functions (PUC-II)','Matrices (PUC-II)','Determinants (PUC-II)','Continuity and Differentiability (PUC-II)']







#1. Average of each chapter from diff tests (tupled with chapter_name)      DONE
#2. Average of all the tests (avg of 1)                                     DONE
#3. Average of all students                                                 DONE
#4. Average of each test (tupled with date and test_id)                     DONE
#5. Max of a chapter from all the tests. (tupled with date and id)          DONE
#6. Max of avg from all chapters. (tupled with date and id)                 DONE






def save_data_to_csv(data, roll):
    output_path=f'Data/Processed/{subject}'
    file_path = f"{output_path}/{roll}.csv"
    new_df = pd.DataFrame([data],columns=["Date_of_test", "Avg_of_test", "Avg_class", "Average_of_student_chapter_wise", "Class_Average_chapter_wise",'Max_marks_chapter_wise','Max_marks_in_this_test']
    )
    
    if os.path.exists(file_path):
        try:
            existing_df = pd.read_csv(file_path)
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            combined_df.to_csv(file_path, index=False)
            print(f"Data appended successfully for student {roll}")
        except pd.errors.EmptyDataError:
            new_df.to_csv(file_path, index=False)
            print(f"Created new file for student {roll}")
    else:
        new_df.to_csv(file_path, index=False)
        print(f"Created new file for student {roll}")







def find_highest_scoring_chapter(student_avg_list):
    highest_scores = {}

    for student_data in student_avg_list:  # Loop through the list of dicts
        for roll, subject_data in student_data.items():
            max_chapter = None
            max_marks = -1  # Initialize to a low value

            for subject, chapters in subject_data.items():
                for chapter, marks in chapters.items():
                    if marks > max_marks:
                        max_marks = marks
                        max_chapter = chapter

            highest_scores[roll] = (max_chapter, max_marks)

    return highest_scores


def calculate_max_marks_in_chapters(roll_no_list, subject, chapter_names, test_data_path):
    """
    Finds the maximum marks scored in multiple chapters for each student.

    :param roll_no_list: List of student roll numbers.
    :param subject: Subject name (e.g., "MATHEMATICS").
    :param chapter_names: List of chapters to find max marks for.
    :param test_data_path: Path to student test data (folder with CSV files).
    :return: Dictionary {roll_no: {chapter_name: (max_marks, date, test_id)}}
    """
    
    max_marks_dict = defaultdict(dict)

    for roll in roll_no_list:
        student_data = {chapter: (0, "N/A", "N/A") for chapter in chapter_names}  # Default to 0 marks
        
        try:
            # Load student's test data
            data_by_roll_no = pd.read_csv(f"{test_data_path}/{roll}.csv")

            for chapter_name in chapter_names:
                max_marks = 0  # Default to 0 marks
                max_date, max_test_id = "N/A", "N/A"

                for index, row in data_by_roll_no.iterrows():
                    if row['Chapter_Name'] == chapter_name:
                        marks = row['Marks_Scored']
                        if marks > max_marks:  # Update if a new max is found
                            max_marks = marks
                            max_date = row['Date']
                            max_test_id = row['Test ID']

                # Store results in dictionary
                student_data[chapter_name] = (max_marks, max_date, max_test_id)

        except FileNotFoundError:
            pass

        max_marks_dict[int(roll)] = student_data

    return dict(max_marks_dict)


def calculate_average_of_each_chapter_individual(data_by_roll_no,roll):
    subjectwise_chapter_average_individual={}
    subjectwise_chapter_average_individual_roll_wise={}
    temp={}

    for chapter_name in eval(subject):
        returning_value=[]

        for i in range(len(data_by_roll_no)):
            if data_by_roll_no['Chapter_Name'][i]==chapter_name:
                returning_value.append(data_by_roll_no['Marks_Scored'][i])

        try:
            temp[chapter_name]=round(sum(returning_value)/len(returning_value))
        except ZeroDivisionError:
            pass

    subjectwise_chapter_average_individual[subject]=temp
    subjectwise_chapter_average_individual_roll_wise[int(roll)]=subjectwise_chapter_average_individual

    return subjectwise_chapter_average_individual_roll_wise


def main():
    
    expanded_scorelist=pd.read_excel('Resources/expanded_scorelist.xlsx')
    roll_no=[]

    for index in range(len(expanded_scorelist)): #replace with: range(len(expanded_scorelist))
        roll_no.append(expanded_scorelist["CANDIDATE ID"][index])

    avg_values_all_students=[]
    avg_values_all_students_rollwise={}
    performance_avg_of_all_students=[]

    for roll in roll_no:

        performance_avg_of_student={}
        subject_inp=subject

        try:
            path_of_data=f'Data/{subject_inp}'
            data_by_roll_no=pd.read_csv(path_of_data+f'/{roll}.csv')
            value_of_1=calculate_average_of_each_chapter_individual(data_by_roll_no,roll)
            avg_values_all_students.append(value_of_1) # THIS IS AVG OF ALL STUDENTS PER CHAPTER
            performance_avg_of_student[subject]=(int(roll),DATE_OF_TEST,round(sum(data_by_roll_no['Marks_Scored'])/(len(data_by_roll_no['Marks_Scored']))))
        except FileNotFoundError:
            performance_avg_of_student[subject]=(int(roll),DATE_OF_TEST,0)

        performance_avg_of_all_students.append(performance_avg_of_student)

    # pprint(performance_avg_of_all_students)# AVERAGE OF STUDENT IN ALL THE TEST
    #2
    # pprint(avg_values_all_students)
    #4

#==========================================================================

    avg_of_whole_class={}
    val=[]  
    for performance_avg_of_student in performance_avg_of_all_students:
        
        val.append(performance_avg_of_student[subject][2])
        avg_of_whole_class[subject]=(DATE_OF_TEST,round(sum(val)/len(val)))

    pprint(avg_of_whole_class)#  AVERAGE OF WHOLE CLASSSSSSSSSSSSSSS
    #3

#==========================================================================

    class_avg_each_chap = {} 
    subject_avg = {} 

    for chapter in eval(subject): 
        val = []
        
        for roll in roll_no: 
            found = False 

            for individual_student_avg_dict_with_roll in avg_values_all_students:
                try:
                    student_data = individual_student_avg_dict_with_roll.get(int(roll), {})
                    if subject in student_data and chapter in student_data[subject]:
                        val.append(student_data[subject][chapter])
                        found = True
                except KeyError:
                    pass

            if not found:
                pass

        if val:
            subject_avg[chapter] = round(sum(val) / len(val))
        else:
            subject_avg[chapter] = 0
    class_avg_each_chap[subject] = subject_avg.copy()
    # pprint(class_avg_each_chap)  #Average of the class in each chapters :>
    #5

#==========================================================================
    avg_of_each_test={}

    for roll in roll_no:
        indiv_avg={}
        val=[]
        avg=0

        try:
            path_of_data=f'Data/{subject}'
            data_by_roll_no=pd.read_csv(path_of_data+f'/{roll}.csv')

            for index in range(len(data_by_roll_no)):
                if data_by_roll_no['Test ID'][index]==current_test_id:
                    avg=sum(data_by_roll_no['Marks_Scored'])/len(data_by_roll_no['Marks_Scored'])
                    # val.append(data_by_roll_no['Marks_Scored'])

            indiv_avg[current_test_id]=(subject,round(avg))

        except ZeroDivisionError:
            indiv_avg[current_test_id]=(subject,0)
        avg_of_each_test[int(roll)]=indiv_avg

    # pprint(avg_of_each_test) #RETURNS AVG OF A TEST GIVEN THE TEST NUMBER WITH IT
    #THIS SHI USELESS :(
    #Already did it up

#================================================================================

    max_marks_per_chapter = calculate_max_marks_in_chapters(roll_no, subject, eval(subject), path_of_data)
    # print(max_marks_per_chapter) #Displays max marks per chapter roll_wise
    #6

#================================================================================

    highest_scoring_chapters = find_highest_scoring_chapter(avg_values_all_students)
    # pprint(highest_scoring_chapters) #Best chapter a student is rn :>

#================================================================================

    for roll in roll_no:
        avg_of_the_test_for_saving=0
        list_of_avg_chapter_wise_for_saving=[]
        list_of_class_avg_chapter_wise_for_saving=[]
        max_marks_chapter_wise_for_saving=[]
        max_marks_in_this_test_for_saving=()


        for temp in performance_avg_of_all_students:
            if temp[subject][0]==roll:
                avg_of_the_test_for_saving=temp[subject][2]

        for temp in avg_values_all_students:
            if list(temp.keys())==[roll]:
                for chapter in eval(subject):
                    list_of_avg_chapter_wise_for_saving.append(temp[roll][subject][chapter])

        for chapter in eval(subject):
            list_of_class_avg_chapter_wise_for_saving.append(class_avg_each_chap[subject][chapter])
            max_marks_chapter_wise_for_saving.append(max_marks_per_chapter[roll][chapter])
        max_marks_in_this_test_for_saving=highest_scoring_chapters[roll]


        data=[DATE_OF_TEST,avg_of_the_test_for_saving,avg_of_whole_class[subject][-1],
            tuple(list_of_avg_chapter_wise_for_saving),tuple(list_of_class_avg_chapter_wise_for_saving),
            tuple(max_marks_chapter_wise_for_saving),max_marks_in_this_test_for_saving]
        
        save_data_to_csv(data, roll)
        print(data)


#================================================================================

if __name__ == "__main__":
    start_time = time.time()  # Start the timer

    main()  # Run your main function

    end_time = time.time()  # End the timer
    execution_time = end_time - start_time  # Calculate elapsed time

    print(f"\nExecution Time: {execution_time:.4f} seconds")  # Display time in seconds
