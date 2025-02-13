import pandas as pd
import tabula as tb

#================================================================================
#=========Dividing questions into easy medium and hard===========================
student_analysis=pd.read_excel("Resources\student_analysis.xls",skiprows=8)
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

#==============================================================================
#===========Getting info on student's responses================================
expanded_scorelist=pd.read_excel('Resources\expanded_scorelist.xlsx')
data2=expanded_scorelist.head(1)
attempt_correct=list(map(lambda x:int(x),data2["MATHEMATICS R IDS"][0].split(',') ))
attempt_wrong=list(map(lambda x:int(x),data2["MATHEMATICS W IDS"][0].split(',') ))
left=list(map(lambda x:int(x),data2["MATHEMATICS L IDS"][0].split(',') ))


#==============================================================================
#=============Blueprint interpretation=========================================
Mathematics=dict()
# Accessing the blueprint
tables = tb.read_pdf(r"Resources\blueprint_data.pdf", pages="1")
# Get the first DataFrame
blueprint_data = tables[0]
# Clean column names
blueprint_data.columns = blueprint_data.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
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

#==============================================================================
#===========SPI Calculation====================================================
SPI=0
for i in attempt_correct:
    if i in easy_questions:
        SPI+=0.8
    elif i in med_questions:
        SPI+=1
    else:
        SPI+=1.2
for i in attempt_wrong:
    if i in easy_questions:
        SPI-=0.2
    elif i in med_questions:
        SPI-=0.15
    else:
        SPI-=0.1
SPI-=len(left)*0.1

print(round(SPI))