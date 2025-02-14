import pandas as pd
import tabula as tb
import pdb

Date=input('Enter date in the format of DD-MM-YYYY')
Test_Id=input('Enter test ID :)')
#================================================================================
#=========Dividing questions into easy medium and hard===========================
student_analysis=pd.read_excel("Tern\Resources\student_analysis.xls",skiprows=8)
data=student_analysis.head(68) #Questions start from row 8
easy_questions=[]
med_questions=[]
hard_questions=[]
for i in range(0,60):
    if data["ATT%"][i]>50:
        if (data['R%'][i]/data["ATT%"][i])*100>65:
            easy_questions.append(i+1)
        elif (data['R%'][i]/data["ATT%"][i])*100<25:
            hard_questions.append(i+1)
        else:
            med_questions.append(i+1)
    elif data["ATT%"][i]<25:
        hard_questions.append(i+1)
    else:
        if (data['R%'][i]/data["ATT%"][i])*100>65:
            med_questions.append(i+1)
        else:
            hard_questions.append(i+1)
print(easy_questions,med_questions,hard_questions,sep='\n')
tables = tb.read_pdf(r"Tern\Resources\blueprint_data.pdf", pages="1")

blueprint_data = tables[0]
# Clean column names
blueprint_data.columns = blueprint_data.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
# Initialize the dictionary properly
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
    chapterwise_question_numbers[chapterwise_blueprint["Chapter Name"][i]] = []
    for j in range(int(chapterwise_blueprint["Multiple Choice Question"][i])):
        pointer += 1
        chapterwise_question_numbers[chapterwise_blueprint["Chapter Name"][i]].append(pointer)
chapterwise_question_numbers.pop("Total")
print(chapterwise_question_numbers)
#==============================================================================
def making_sure_empty_cells_are_noticed(x):
    if type(x) != str:
        return(int(x))
    else:
        return(0)
#==============================================================================
#===========Getting info on student's responses================================
expanded_scorelist=pd.read_excel('Tern\Resources\expanded_scorelist.xlsx')
# print('333333333333333333333333333333333333333333',len(expanded_scorelist))

for p in range(0,len(expanded_scorelist)):
    data2=expanded_scorelist.iloc[p]  
    attempt_correct=[]
    attempt_wrong=[]
    left=[]  
    attempt_correct=list(map(making_sure_empty_cells_are_noticed,str(data2["MATHEMATICS R IDS"])[0].split(',') ))
    attempt_wrong=list(map(making_sure_empty_cells_are_noticed,str(data2["MATHEMATICS W IDS"])[0].split(',') ))
    left=list(map(making_sure_empty_cells_are_noticed,str(data2["MATHEMATICS L IDS"])[0].split(',') ))


    #==============================================================================
    #=============Blueprint interpretation=========================================
    Mathematics=dict()

    #=============================================================================
    #===========SPI Calculation====================================================
    pdb.set_trace()
    SPI=0
    for chapter_name,questions in chapterwise_question_numbers.items():

        if chapter_name in Mathematics:
            pass
        else:
            Mathematics[chapter_name]=0
            for question in questions:
                if question in attempt_correct:
                    if question in easy_questions:
                        SPI+=0.8*3
                    elif question in med_questions:
                        SPI+=1*3
                    else:
                        SPI+=1.2*3
                elif question in attempt_wrong:
                        if question in easy_questions: #MULTIPLIED 3 TO ALL THE WEIGHTS JUST SO THAT THE VALUES ARE BIGGER BECAUSE 
                            SPI-=0.2  #I WAS GETTING single intergers :(
                        elif question in med_questions:
                            SPI-=0.15
                        else:
                            pass
            else:
                SPI-=len(left)*0.1
            Mathematics[chapter_name]=round(SPI)
    print(Mathematics)
    results = []
    for chapter_name, marks_scored in Mathematics.items():
        results.append([Date,expanded_scorelist["CANDIDATE ID"][p],Test_Id, chapter_name, marks_scored])

    # Convert to DataFrame
    df = pd.DataFrame(results, columns=["Date","Roll No","Test ID","Chapter_Name", "Marks_Scored"])

    # Save to CSV file
    df.to_csv(f"Tern/Data/{expanded_scorelist["CANDIDATE ID"][p]}.csv", index=False)

    print(f"Data saved successfully to {expanded_scorelist["CANDIDATE ID"][p]}.csv")
