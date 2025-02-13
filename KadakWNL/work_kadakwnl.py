import pandas as pd
import tabula as tb

# student_analysis=pd.read_excel("Resources\student_analysis.xls",skiprows=8)
# data=student_analysis.head(68) #Questions start from row 8
# easy_questions=[]
# med_questions=[]
# hard_questions=[]

# for i in range(0,60):
#     if data["ATT%"][i]>50:
#         if (data['R%'][i]/["ATT%"][i])*100>65:
#             easy_questions.append[i]
#         elif (data['R%'][i]/["ATT%"][i])*100<25:
#             hard_questions.append[i]
#         else:
#             med_questions.append[i]
#     elif data["ATT%"][i]<25:
#         hard_questions.append[i]

# Accessing the blueprint
tables = tb.read_pdf(r"..\Resources\blueprint_data.pdf", pages="1")
blueprint_data = tables[0]

# Clean column names
blueprint_data.columns = blueprint_data.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
print("Cleaned Column Names:", blueprint_data.columns.tolist())

# Initialize the dictionary properly
chapterwise_blueprint = {
    "Chapter Name": [],
    "Multiple Choice Question": []
}

# Loop through the DataFrame and populate the dictionary
for index, row in blueprint_data.iterrows():
    chapterwise_blueprint["Chapter Name"].append(row["Chapter Name"])
    chapterwise_blueprint["Multiple Choice Question"].append(row["Multiple Choice Question"].split()[0])
print(chapterwise_blueprint)

chapterwise_question_numbers = {}
pointer = 0
for i in range(len(chapterwise_blueprint["Chapter Name"])):
    chapterwise_question_numbers[chapterwise_blueprint["Chapter Name"][i]] = []
    for j in range(int(chapterwise_blueprint["Multiple Choice Question"][i])):
        pointer += 1
        chapterwise_question_numbers[chapterwise_blueprint["Chapter Name"][i]].append(pointer)
chapterwise_question_numbers.pop("Total")
print(chapterwise_question_numbers)
