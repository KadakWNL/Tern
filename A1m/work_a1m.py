# import pandas as pd
# import tabula as tb
# subject=input("Enter 1 for phy 2 for chem 3 for math: ")
# if subject == '1':
#     pass
# elif subject == '2':
#     pass
# elif subject=='3':
#     pass
# else:
#     print("Wrong input")
#     exit()

# Date=input('Enter date in the format of DD-MM-YYYY')
# Test_Id=input('Enter test ID :)')
# #================================================================================
# #=========Dividing questions into easy medium and hard===========================
# student_analysis=pd.read_excel("Resources\student_analysis.xls",skiprows=8)
# data=student_analysis.head(68) #Questions start from row 8
# easy_questions=[]
# med_questions=[]
# hard_questions=[]
# for i in range(0,60):
#     if data["ATT%"][i]>50:
#         if (data['R%'][i]/data["ATT%"][i])*100>65:
#             easy_questions.append(i+1)
#         elif (data['R%'][i]/data["ATT%"][i])*100<25:
#             hard_questions.append(i+1)
#         else:
#             med_questions.append(i+1)
#     elif data["ATT%"][i]<25:
#         hard_questions.append(i+1)
#     else:
#         if (data['R%'][i]/data["ATT%"][i])*100>65:
#             med_questions.append(i+1)
#         else:
#             hard_questions.append(i+1)
# print(easy_questions,med_questions,hard_questions,sep='\n')
# tables = tb.read_pdf(r"Resources\blueprint_data.pdf", pages="1")

# blueprint_data = tables[0]
# # Clean column names
# blueprint_data.columns = blueprint_data.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
# # Initialize the dictionary properly
# chapterwise_blueprint = {
#     "Chapter Name": [],
#     "Multiple Choice Question": []
# }
# for index, row in blueprint_data.iterrows():
#     chapterwise_blueprint["Chapter Name"].append(row["Chapter Name"])
#     chapterwise_blueprint["Multiple Choice Question"].append(row["Multiple Choice Question"].split()[0])

# chapterwise_question_numbers = {}
# pointer = 0
# for i in range(len(chapterwise_blueprint["Chapter Name"])):
#     chapterwise_question_numbers[chapterwise_blueprint["Chapter Name"][i]] = []
#     for j in range(int(chapterwise_blueprint["Multiple Choice Question"][i])):
#         pointer += 1
#         chapterwise_question_numbers[chapterwise_blueprint["Chapter Name"][i]].append(pointer)
# chapterwise_question_numbers.pop("Total")
# print(chapterwise_question_numbers)
# #==============================================================================
# def making_sure_empty_cells_are_noticed(x):
#     if type(x) != str:
#         return(int(x))
#     else:
#         return(0)
# #==============================================================================
# #===========Getting info on student's responses================================
# expanded_scorelist=pd.read_excel('Resources\expanded_scorelist.xlsx')
# print('333333333333333333333333333333333333333333',len(expanded_scorelist))

# for p in range(0,len(expanded_scorelist)):
#     data2=expanded_scorelist.iloc[p]  
#     attempt_correct=[]
#     attempt_wrong=[]
#     left=[]  
#     attempt_correct=list(map(making_sure_empty_cells_are_noticed,str(data2["MATHEMATICS R IDS"])[0].split(',') ))
#     attempt_wrong=list(map(making_sure_empty_cells_are_noticed,str(data2["MATHEMATICS W IDS"])[0].split(',') ))
#     left=list(map(making_sure_empty_cells_are_noticed,str(data2["MATHEMATICS L IDS"])[0].split(',') ))


#     #==============================================================================
#     #=============Blueprint interpretation=========================================
#     Mathematics=dict()

#     #=============================================================================
#     #===========SPI Calculation====================================================
#     SPI=0
#     for chapter_name,questions in chapterwise_question_numbers.items():
        
#         if chapter_name in Mathematics:
#             pass
#         else:
#             Mathematics[chapter_name]=0
#             for question in questions:
#                 if question in attempt_correct:
#                     if question in easy_questions:
#                         SPI+=0.8*3
#                     elif question in med_questions:
#                         SPI+=1*3
#                     else:
#                         SPI+=1.2*3
#                 elif question in attempt_wrong:
#                         if question in easy_questions: #MULTIPLIED 3 TO ALL THE WEIGHTS JUST SO THAT THE VALUES ARE BIGGER BECAUSE 
#                             SPI-=0.2  #I WAS GETTING single intergers :(
#                         elif question in med_questions:
#                             SPI-=0.15
#                         else:
#                             pass
#             else:
#                 pass
#             Mathematics[chapter_name]=round(SPI)
#     print(Mathematics)
#     results = []
#     for chapter_name, marks_scored in Mathematics.items():
#         results.append([Date,expanded_scorelist["CANDIDATE ID"][p],Test_Id, chapter_name, marks_scored])

#     # Convert to DataFrame
#     df = pd.DataFrame(results, columns=["Date","Roll No","Test ID","Chapter_Name", "Marks_Scored"])

#     # Save to CSV file
#     df.to_csv(f"Data/{expanded_scorelist["CANDIDATE ID"][p]}.csv", index=False)

#     print("Data saved successfully to student_scores.csv")


#=================================================================================================================================
import pandas as pd
import tabula as tb
from typing import Dict, List, Tuple
import os
import glob

def get_subject_code() -> str:
    subject_map = {'1': 'PHYSICS', '2': 'CHEMISTRY', '3': 'MATHEMATICS'}
    subject = input("Enter 1 for physics, 2 for chemistry, 3 for math: ")
    if subject not in subject_map:
        print("Wrong input")
        exit()
    return subject_map[subject]

def check_existing_test(subject: str, date: str, test_id: str) -> bool:
    subject_dir = f"Data/{subject}"
    if not os.path.exists(subject_dir):
        return False
        
    for file_path in glob.glob(f"{subject_dir}/*.csv"):
        try:
            df = pd.read_csv(file_path)
            if df.empty:
                continue
            
            df['Date'] = df['Date'].astype(str).str.strip()
            df['Test ID'] = df['Test ID'].astype(str).str.strip()
            date = str(date).strip()
            test_id = str(test_id).strip()
            
            duplicate_exists = any((df['Date'] == date) & (df['Test ID'] == test_id))
            
            if duplicate_exists:
                print(f"Found duplicate in file: {file_path}")
                print(f"Existing entries with Date={date}, Test ID={test_id}:")
                print(df[((df['Date'] == date) & (df['Test ID'] == test_id))][['Date', 'Test ID']])
                return True
                
        except (pd.errors.EmptyDataError, KeyError) as e:
            print(f"Warning: Error processing file {file_path}: {str(e)}")
            continue
    return False

def get_user_inputs(subject: str) -> Tuple[str, str]:
    while True:
        date = input('Enter date in the format of DD-MM-YYYY: ').strip()
        test_id = input('Enter test ID: ').strip()
        
        if check_existing_test(subject, date, test_id):
            print(f"\nError: Test with date '{date}' and test ID '{test_id}' already exists for {subject}!")
            if input("Would you like to try again? (y/n): ").lower() != 'y':
                exit()
            print()
        else:
            return date, test_id

def categorize_questions(student_analysis: pd.DataFrame) -> Tuple[List[int], List[int], List[int]]:
    data = student_analysis.head(68)  # Questions start from row 8
    easy_questions = []
    med_questions = []
    hard_questions = []
    
    for i in range(60):
        att_percent = data["ATT%"][i]
        success_rate = (data['R%'][i]/att_percent*100) if att_percent > 0 else 0
        
        if att_percent > 50:
            if success_rate > 65:
                easy_questions.append(i+1)
            elif success_rate < 25:
                hard_questions.append(i+1)
            else:
                med_questions.append(i+1)
        elif att_percent < 25:
            hard_questions.append(i+1)
        else:
            if success_rate > 65:
                med_questions.append(i+1)
            else:
                hard_questions.append(i+1)
                
    return easy_questions, med_questions, hard_questions

def get_chapter_questions(blueprint_path: str) -> Dict[str, List[int]]:
    tables = tb.read_pdf(blueprint_path, pages="1")
    blueprint_data = tables[0]
    blueprint_data.columns = blueprint_data.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
    
    chapterwise_blueprint = {
        "Chapter Name": [],
        "Multiple Choice Question": []
    }
    
    for index, row in blueprint_data.iterrows():
        chapterwise_blueprint["Chapter Name"].append(row["Chapter Name"])
        chapterwise_blueprint["Multiple Choice Question"].append(row["Multiple Choice Question"].split()[0])
    
    chapterwise_question_numbers = {}
    pointer = 0
    
    for i in range(len(chapterwise_blueprint["Chapter Name"])):
        chapter_name = chapterwise_blueprint["Chapter Name"][i]
        question_count = int(chapterwise_blueprint["Multiple Choice Question"][i])
        
        chapterwise_question_numbers[chapter_name] = []
        for _ in range(question_count):
            pointer += 1
            chapterwise_question_numbers[chapter_name].append(pointer)
    
    chapterwise_question_numbers.pop("Total", None)
    return chapterwise_question_numbers

def parse_response_ids(x) -> int:
    if isinstance(x, str):
        return int(x) if x.isdigit() else 0
    return 0

def calculate_student_performance(
    student_data: pd.Series,
    subject: str,
    chapterwise_questions: Dict[str, List[int]],
    easy_questions: List[int],
    med_questions: List[int],
    hard_questions: List[int]
) -> Dict[str, float]:
    correct_ids = str(student_data[f"{subject} R IDS"]).split(',')
    wrong_ids = str(student_data[f"{subject} W IDS"]).split(',')
    left_ids = str(student_data[f"{subject} L IDS"]).split(',')
    
    attempt_correct = [parse_response_ids(x) for x in correct_ids]
    attempt_wrong = [parse_response_ids(x) for x in wrong_ids]
    left = [parse_response_ids(x) for x in left_ids]
    
    performance = {}
    for chapter_name, questions in chapterwise_questions.items():
        spi = 0
        for question in questions:
            if question in attempt_correct:
                if question in easy_questions:
                    spi += 0.8 * 3
                elif question in med_questions:
                    spi += 1.0 * 3
                else:
                    spi += 1.2 * 3
            elif question in attempt_wrong:
                if question in easy_questions:
                    spi -= 0.2  # Penalty for wrong attempts
                elif question in med_questions:
                    spi -= 0.15
        performance[chapter_name] = round(spi)
    
    return performance

def create_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")

def save_results(
    results: List[List],
    student_id: str,
    output_dir: str = "Data/Trash"
) -> None:
    create_directory(output_dir)
    
    file_path = f"{output_dir}/{student_id}.csv"
    new_df = pd.DataFrame(
        results,
        columns=["Date", "Roll No", "Test ID", "Chapter_Name", "Marks_Scored"]
    )
    
    if os.path.exists(file_path):
        try:
            existing_df = pd.read_csv(file_path)
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            combined_df = combined_df.sort_values(['Date', 'Test ID'])
            combined_df.to_csv(file_path, index=False)
            print(f"Data appended successfully for student {student_id}")
        except pd.errors.EmptyDataError:
            new_df.to_csv(file_path, index=False)
            print(f"Created new file for student {student_id}")
    else:
        new_df.to_csv(file_path, index=False)
        print(f"Created new file for student {student_id}")

def main():
    subject = get_subject_code()
    date, test_id = get_user_inputs(subject)
    
    student_analysis = pd.read_excel("Resources/student_analysis.xls", skiprows=8)
    easy_questions, med_questions, hard_questions = categorize_questions(student_analysis)
    
    chapterwise_questions = get_chapter_questions("Resources/blueprint_data.pdf")
    expanded_scorelist = pd.read_excel('Resources/expanded_scorelist.xlsx')
    
    for idx in range(len(expanded_scorelist)):
        student_data = expanded_scorelist.iloc[idx]
        performance = calculate_student_performance(
            student_data,
            subject,
            chapterwise_questions,
            easy_questions,
            med_questions,
            hard_questions
        )
        
        results = [
            [date, expanded_scorelist["CANDIDATE ID"][idx], test_id, chapter, marks]
            for chapter, marks in performance.items()
        ]
        
        save_results(results, expanded_scorelist["CANDIDATE ID"][idx], f"Data/{subject}")

if __name__ == "__main__":
    main()