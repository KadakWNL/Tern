import pandas as pd
student_analysis=pd.read_excel("Resources\student_analysis.xls",skiprows=8)
data=student_analysis.head(68) #Questions start from row 8
easy_questions=[]
med_questions=[]
hard_questions=[]
for i in range(0,60):
    if data["ATT%"][i]>50:
        if (data['R%'][i]/["ATT%"][i])*100>65:
            easy_questions.append[i]
        elif (data['R%'][i]/["ATT%"][i])*100<25:
            hard_questions.append[i]
        else:
            med_questions.append[i]
    elif data["ATT%"][i]<25:
        hard_questions.append[i]