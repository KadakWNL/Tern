import pandas as pd
from pprint import pprint
from collections import defaultdict
import os
import time
import json as js
DATE_OF_TEST = None
current_test_id = None
subject = None
# TO DO: Save the class avg in a different json folder only, essentially reducing space used !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PHYSICS = [     
                'Units and Measurements (PUC-I)',
                'Motion in a Straight Line (PUC-I)',
                'Motion in a Plane (PUC-I)',
                'Laws of Motion (PUC-I)',
                'Work, Energy and Power (PUC-I)',
                'System of Particles and Rotational Motion (PUC-I)',
                'Gravitation (PUC-I)',
                'Mechanical Properties of Solids (PUC-I)',
                'Mechanical Properties of Fluids (PUC-I)',
                'Thermal Properties of Matter (PUC-I)',
                'Thermodynamics (PUC-I)',
                'Kinetic Theory (PUC-I)',
                'Oscillations (PUC-I)',
                'Waves (PUC-I)',
                'Electric Charges and Fields (PUC-II)',
                'Electrostatic Potential and Capacitance (PUC-II)',
                'Current Electricity (PUC-II)',
                'Moving charges and magnetism (PUC-II)',
                'Magnetism and Matter (PUC-II)',
                'Electromagnetic Induction (PUC-II)',
                'Alternating Current (PUC-II)',
                'Electromagnetic Waves (PUC-II)',
                'Ray Optics and Optical Instruments (PUC-II)',
                'Wave Optics (PUC-II)',
                'Dual Nature of Radiation and Matter (PUC-II)',
                'Atoms (PUC-II)',
                'Nuclei (PUC-II)',
                'Semiconductor Electronics Materials, Devices and Simple Circuits (PUC-II)']
CHEMISTRY = [   
                'Some Basic Concepts of Chemistry (PUC-I)',
                'Structure of Atom (PUC-I)',
                'Classification of Elements and Periodicity in Properties (PUC-I)',
                'Chemical Bonding and Molecular Structure (PUC-I)',
                'Thermodynamics (PUC-I)',
                'Equilibrium (PUC-I)',
                'Redox Reactions (PUC-I)',
                'Organic Chemistry : Some Basic Principles and Techniques (PUC-I)',
                'Hydrocarbons (PUC-I)',
                'Solutions (PUC-II)',
                'Electrochemistry (PUC-II)',
                'Chemical Kinetics (PUC-II)',
                'The d and f Block Elements (PUC-II)',
                'Coordination Compounds (PUC-II)',
                'Haloalkanes and Haloarenes (PUC-II)',
                'Alcohols, Phenols and Ethers (PUC-II)',
                'Aldehydes, Ketones and Carboxylic Acids (PUC-II)',
                'Amines (PUC-II)',
                'Biomolecules (PUC-II)']
MATHEMATICS = [
                'Sets (PUC-I)',
                'Relations and Functions (PUC-I)',
                'Trigonometric Functionsv (PUC-I)',
                'Complex Numbers and Quadratic Equations (PUC-I)',
                'Linear Inequalities (PUC-I)',
                'Permutations and Combinations (PUC-I)',
                'Binomial Theorem (PUC-I)',
                'Sequences and Series (PUC-I)',
                'Straight Lines (PUC-I)',
                'Conic Sections (PUC-I)',
                'Introduction to Three Dimensional Geometry (PUC-I)',
                'Limits and Derivatives (PUC-I)',
                'Statistics (PUC-I)',
                'Probability (PUC-I)',
                'Relations and Functions (PUC-II)',
                'Inverse Trigonometric Functions (PUC-II)',
                'Matrices (PUC-II)',
                'Determinants (PUC-II)',
                'Continuity and Differentiability (PUC-II)',
                'Application of Derivatives (PUC-II)',
                'Integrals (PUC-II)',
                'Application of Integrals (PUC-II)',
                'Differential Equations (PUC-II)',
                'Vector Algebra (PUC-II)',
                'Three Dimensional Geometry (PUC-II)',
                'Linear Programming (PUC-II)',
                'Probability (PUC-II)']


columns=["Date_of_test", "Avg_of_test", "Avg_class", "Average_of_student_chapter_wise",
        "Class_Average_chapter_wise",'Max_marks_chapter_wise','Max_marks_in_this_test']


#1. Average of each chapter from diff tests (tupled with chapter_name)      DONE
#2. Average of all the tests (avg of 1)                                     DONE
#3. Average of all students                                                 DONE
#4. Average of each test (tupled with date and test_id)                     DONE
#5. Max of a chapter from all the tests. (tupled with date and id)          DONE
#6. Max of avg from all chapters. (tupled with date and id)                 DONE





def save_common_data(data):
    output_path=f'Data/Processed/{subject}'
    file_path=f"{output_path}/common_data.json"
    if os.path.exists(file_path):
        with open(file_path,'r') as current_file:
            try:
                data_of_current_file=js.load(current_file)
            except js.JSONDecodeError:
                data_of_current_file=[]
        if not isinstance(data_of_current_file, list):
            data_of_current_file = [data_of_current_file]
        data_of_current_file.append(data)
        with open(file_path, 'w') as file:
            js.dump(data_of_current_file, file, indent=4)
    else:
        with open(file_path,'w') as current_file:
            js.dump(data, current_file, indent=4)



def save_data_to_csv(data, roll):
    output_path=f'Data/Processed/{subject}'
    os.makedirs(output_path, exist_ok=True)
    file_path = f"{output_path}/{roll}.json"

    if os.path.exists(file_path):
        with open(file_path,'r') as current_file:
            data_of_current_file=js.load(current_file)
            if str(DATE_OF_TEST)+'-'+str(subject)+'-'+str(current_test_id) in list(data_of_current_file.keys()):
                print("Test data already exists!")  #<===== HANDLE THIS!!!!!!!!!!!!!!!!!!!!!!
            if data_of_current_file:
                    pass
            else:
                data_of_current_file = []  # Handle empty or corrupted JSON
        if not isinstance(data_of_current_file, list):
            data_of_current_file = [data_of_current_file]
        data_of_current_file.append(data)
        with open(file_path, 'w') as file:
            js.dump(data_of_current_file, file, indent=4)
    else:
        with open(file_path,'w') as current_file:
            js.dump(data, current_file, indent=4)

def calculate_the_avg_spi_till_date(data_by_roll_no,roll):
    return int(sum(data_by_roll_no["Marks_Scored"])/len(data_by_roll_no["Marks_Scored"]))

def find_highest_scoring_chapter(student_avg_list):
    highest_scores = {}

    for student_data in student_avg_list:  # Loop through the list of dicts
        for roll, subject_data in student_data.items():
            max_marks = -1  # Track max marks
            max_chapters = []  # Store all chapters with max marks

            for subject, chapters in subject_data.items():
                for chapter, marks in chapters.items():
                    if marks > max_marks:
                        max_marks = marks
                        max_chapters = [chapter]  # Reset list with new max
                    elif marks == max_marks:
                        max_chapters.append(chapter)  # Add if it's also max

            # Store as "count-max_marks": [list of chapters]
            key = f"{len(max_chapters)}-{max_marks}"
            highest_scores[roll] = {key: max_chapters}

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
    
    max_marks_dict = {}

    for roll in roll_no_list:
        student_data = {}  # Only store chapters with valid data

        try:
            # Load student's test data
            data_by_roll_no = pd.read_csv(f"{test_data_path}/{roll}.csv")

            for chapter_name in chapter_names:
                max_marks = 0
                max_date, max_test_id = "N/A", "N/A"

                # Iterate through rows and find max marks for the chapter
                for index, row in data_by_roll_no.iterrows():
                    if row['Chapter_Name'] == chapter_name:
                        marks = row['Marks_Scored']
                        if marks > max_marks:
                            max_marks = marks
                            max_date = row['Date']
                            max_test_id = row['Test ID']

                # Store only if valid data is found
                if max_date != "N/A":
                    student_data[chapter_name] = (max_marks, max_date, max_test_id)

        except FileNotFoundError:
            pass  # Ignore if no file exists

        if student_data:  # Only add if student has valid data
            max_marks_dict[int(roll)] = student_data

    return max_marks_dict



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


def main(expanded_scorelist_path=None,date_of_test=None, test_id=None, sub=None):
    global DATE_OF_TEST, current_test_id, subject
    
    DATE_OF_TEST = date_of_test
    current_test_id = test_id
    subject = sub

    path_of_data = f'Data/{subject}'
        
    expanded_scorelist=pd.read_excel(expanded_scorelist_path)
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

    # pprint(avg_of_whole_class)#  AVERAGE OF WHOLE CLASSSSSSSSSSSSSSS
    #3

#==========================================================================
#============Shi is used to calc the Average over time SPI=================
    avg_spi_till_date_roll_wise={}
    temp=0
    for roll in roll_no:
        data_by_roll_no=pd.read_csv(path_of_data+f'/{roll}.csv')
        avg_spi_till_date=calculate_the_avg_spi_till_date(data_by_roll_no,roll)
        temp+=int(avg_spi_till_date)
        avg_spi_till_date_roll_wise[roll]=avg_spi_till_date
    #For class
    avg_spi_till_date_class=int(temp/len(roll_no))
    del temp






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
    # avg_of_each_test={}

    # for roll in roll_no:
    #     indiv_avg={}
    #     val=[]
    #     avg=0

    #     try:
    #         path_of_data=f'Data/{subject}'
    #         data_by_roll_no=pd.read_csv(path_of_data+f'/{roll}.csv')

    #         for index in range(len(data_by_roll_no)):
    #             if data_by_roll_no['Test ID'][index]==current_test_id:
    #                 avg=sum(data_by_roll_no['Marks_Scored'])/len(data_by_roll_no['Marks_Scored'])
    #                 # val.append(data_by_roll_no['Marks_Scored'])

    #         indiv_avg[current_test_id]=(subject,round(avg))

    #     except (ZeroDivisionError,FileNotFoundError):
    #         indiv_avg[current_test_id]=(subject,0)
    #     avg_of_each_test[int(roll)]=indiv_avg

    # # pprint(avg_of_each_test) #RETURNS AVG OF A TEST GIVEN THE TEST NUMBER WITH IT
    # #THIS SHI USELESS :(
    # #Already did it up

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
        list_of_avg_chapter_wise_for_saving={}
        list_of_class_avg_chapter_wise_for_saving={}
        max_marks_chapter_wise_for_saving={}
        max_marks_in_this_test_for_saving=()


        for temp in performance_avg_of_all_students:
            if temp[subject][0]==roll:
                avg_of_the_test_for_saving=temp[subject][2]
        try:
            for temp in avg_values_all_students:
                if list(temp.keys())==[roll]:
                    for chapter in eval(subject):
                        list_of_avg_chapter_wise_for_saving[chapter]=temp[roll][subject][chapter]
        except KeyError:
            pass
        try:
            for chapter in eval(subject):
                list_of_class_avg_chapter_wise_for_saving[chapter]=class_avg_each_chap[subject][chapter]
            max_marks_in_this_test_for_saving=highest_scoring_chapters[int(roll)]
        except Exception: #HANDLE THIS <==============================================================
            pass #<===(Throwing errors for absentees)
        try:
            for chapter in eval(subject):
                max_marks_chapter_wise_for_saving=max_marks_per_chapter[roll]
        except Exception: 
            pass

        data={
            str(DATE_OF_TEST)+'-'+str(subject)+'-'+str(current_test_id):{
                'Avg_of_test':avg_of_the_test_for_saving,
                'Avg_of_student_chapter_wise':list_of_avg_chapter_wise_for_saving,
                'Avg_SPI_till_date':avg_spi_till_date_roll_wise[roll],
                'Max_marks_chapter_wise':max_marks_chapter_wise_for_saving,
                'Max_marks_in_current_test':max_marks_in_this_test_for_saving,
            }
        }
        # data=[DATE_OF_TEST,avg_of_the_test_for_saving,avg_of_whole_class[subject][-1],
        #     tuple(list_of_avg_chapter_wise_for_saving),tuple(list_of_class_avg_chapter_wise_for_saving),
        #     tuple(max_marks_chapter_wise_for_saving),max_marks_in_this_test_for_saving]
        
        save_data_to_csv(data, roll)
    common_data={
            str(DATE_OF_TEST)+'-'+str(subject)+'-'+str(current_test_id):{
                'Avg_of_class':avg_of_whole_class[subject][-1],
                'Avg_of_class_chapter_wise':list_of_class_avg_chapter_wise_for_saving,
                'Avg_SPI_of_class_till_date':avg_spi_till_date
            }
    }
    save_common_data(common_data)
#=====================================================================================
# FILE SAVING FORMAT
#  {
#     DATE-Subject-ID:{
#         Avg_of_test: ###,      Sum of all chapters/no of chapters
#         Avg_of_class:###,      Sum of all students/no of students (Doesnt include absentees, SO DW)
#         Avg_ofstudent_chapter_wise:{      Considers
#             chapter_name:###
#         },
#         Class_AVG_chapter_wise:{
#             chapter_name:###
#         },
#         Max_marks_chapter_wise:{
#             chapter_name: [date,id,marks]
#         },
#         Max marks in this test:{
#             number_of_chapters:[chapters]
#         },
#     }

#================================================================================

if __name__ == "__main__":
    start_time = time.time()  # Start the timer

    main()  # Run your main function

    end_time = time.time()  # End the timer
    execution_time = end_time - start_time  # Calculate elapsed time

    print(f"\nExecution Time: {execution_time:.4f} seconds")  # Display time in seconds
