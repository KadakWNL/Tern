name = "Default Name"
rollno = "Default RollNo"
rank = 0
subject = "Default Subject"
total_students=100
# Function to update values
def update_values(new_name=None, new_rollno=None, new_rank=None, new_subject=None,new_total_students=None):
    global name, rollno, rank, subject, total_students
    if new_name is not None:
        name = new_name
    if new_rollno is not None:
        rollno = new_rollno
    if new_rank is not None:
        rank = new_rank
    if new_subject is not None:
        subject = new_subject
    if new_total_students is not None:
        total_students=new_total_students

