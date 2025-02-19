import pandas as pd
import camelot as tb
from typing import Dict, List, Tuple
import os
import glob
import math
import csv


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

def get_user_inputs(date,test_id,subject: str) -> Tuple[str, str]:
    while True:
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
    tables = tb.read_pdf(path, pages="1")
    blueprint_data = dict(tables[0].df)
    chaper_names=list(blueprint_data[0])
    chaper_names.pop()
    multiple_choice_questions=list(blueprint_data[1])
    multiple_choice_questions.pop()
    multiple_choice_questions_stripped=list(map(lambda x: x.strip()[0],multiple_choice_questions))
    chapterwise_blueprint = {
        "Chapter Name": chaper_names,
        "Multiple Choice Question": multiple_choice_questions_stripped
    }
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
                    spi -= 0.15  # Penalty for wrong attempts
                elif question in med_questions:
                    spi -= 0.1
                else:
                    spi-=0.5
        performance[chapter_name] = round(spi)
    return performance

def calculation_of_max_spi(    chapterwise_questions: Dict[str, List[int]],
    easy_questions: List[int],
    med_questions: List[int],
    hard_questions: List[int]
    ) -> Dict[str, float]:
    max_spi={}
    for chapter_name, questions in chapterwise_questions.items():
        spi = 0
        for question in questions:
            if question in easy_questions:
                spi += 0.8 * 3
            elif question in med_questions:
                spi += 1.0 * 3
            else:
                spi += 1.2 * 3
        max_spi[chapter_name] = round(spi)
    return max_spi

def scaling_marks(initial_spi,max_spi) -> Dict[str,float]:
    scaled_marks={}
    for chapter in initial_spi:
        s=initial_spi[chapter]
        if s>0:
            pass
        else:
            s=0
        s_max=max_spi[chapter]
        new_spi=math.log10(s + 1) * (100 / math.log10(s_max + 1))
        scaled_marks[chapter]=round(new_spi)
    return scaled_marks

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

def save_test_metadata(subject: str, date: str, test_id: str, metadata_file: str = r"Data\Metadata\test_metadata.csv"):
    """Saves the test metadata to a CSV file to track saved tests."""
    file_exists = os.path.exists(metadata_file)
    
    with open(metadata_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Subject", "Date", "Test ID"])
        writer.writerow([subject, date, test_id])

def is_duplicate_test(subject: str, date: str, test_id: str, metadata_file: str = "test_metadata.csv") -> bool:
    """Checks if the test with the same subject, date, and test ID already exists."""
    if not os.path.exists(metadata_file):
        return False
    
    df = pd.read_csv(metadata_file)
    return ((df["Subject"] == subject) & (df["Date"] == date) & (df["Test ID"] == test_id)).any()


def main(subject=None,date=None,test_id=None,student_analysis_path=None,expanded_scorelist_path=None,blueprint_path=None):
    date, test_id = get_user_inputs(date,test_id,subject)
    
    if is_duplicate_test(subject, date, test_id):
        print(f"Test with Subject: {subject}, Date: {date}, and Test ID: {test_id} already exists. Skipping...")
        return
    
    save_test_metadata(subject, date, test_id)
    
    student_analysis = pd.read_excel(student_analysis_path, skiprows=8)
    easy_questions, med_questions, hard_questions = categorize_questions(student_analysis)
    
    chapterwise_questions = get_chapter_questions(blueprint_path)
    expanded_scorelist = pd.read_excel(expanded_scorelist_path)
    max_spi = calculation_of_max_spi(chapterwise_questions, easy_questions, med_questions, hard_questions)
    print(max_spi)
    
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
        scaled_marks = scaling_marks(performance, max_spi)
        results = [
            [date, expanded_scorelist["CANDIDATE ID"][idx], test_id, chapter, marks]
            for chapter, marks in scaled_marks.items()
        ]
        save_results(results, expanded_scorelist["CANDIDATE ID"][idx], f"Data/{subject}")
        print('Test data saved successfully!')

if __name__ == "__main__":
    main()
