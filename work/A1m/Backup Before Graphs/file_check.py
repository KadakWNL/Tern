import pandas as pd
import camelot as tb
def check_analysis_data(path):
    student_analysis = pd.read_excel(path,skiprows=8)
    if list(student_analysis.columns)==['QNo', 'ATT%', 'R%', 'W%', 'SUBJECT', 'TOPIC / SCHEME', 'POS', 'NEG',
                                        'KEY', 'ANSWER', 'RESULT', 'MARKS']:
        return True
    else:
        return False
def check_scorelist_data(path,subject):
    expanded_scorelist = pd.read_excel(path)
    if list(expanded_scorelist.columns)==['CANDIDATE ID', 'CANDIDATE NAME', 'FATHER', 'GROUP', 'OTHER', 'Test No',
                                        'Test', 'Date', 'Duration', f'{subject} Max', f'{subject} Min',
                                        f'{subject} R', f'{subject} R IDS', f'{subject} W',
                                        f'{subject} W IDS', f'{subject} L', f'{subject} L IDS',
                                        f'{subject} C', f'{subject} C IDS', f'{subject} Mk',
                                        f'{subject} GMax', f'{subject} GMin', f'{subject} Avg', 'Total',
                                        'Maximum', 'Minimum', 'Average', 'Test Rank', 'Group Rank',
                                        'Percentage']:
        return True
    else:
        return False
def check_blueprint_data(path):
    tables = tb.read_pdf(path, pages="1")
    if list(tables[0].df)==[0, 1, 2]:
        return True
    else:
        return False



def main(student_analysis_path,expanded_scorelist_path,blueprint_data_path,subject):
    if check_analysis_data(student_analysis_path) and check_scorelist_data(expanded_scorelist_path,subject) and check_blueprint_data(blueprint_data_path):
        return True
    
    else:
        return False

if __name__=='__main__':
    student_analysis_path=r'Resources\student_analysis.xls'
    expanded_scorelist_path=r'Resources\expanded_scorelist.xlsx'
    blueprint_data_path=r'Resources\blueprint_data.pdf'
    subject='MATHEMATICS'
    main(student_analysis_path,expanded_scorelist_path,blueprint_data_path,subject)