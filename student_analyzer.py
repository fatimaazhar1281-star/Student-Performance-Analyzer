
# Python Week 01 Project:
# Student Performance Analyzer

def display_student_report(name, marks_dict):
    marks_list = list(marks_dict.values())

    average = calculate_average(marks_list)
    print("\n------------------------------")
    print(f'Student    : {name} ')
    print(f'Average    : {average:.2f} ') 
    print(f'Highest    : {find_highest_mark(marks_list)} ')
    print(f'Lowest     : {find_lowest_mark(marks_list)} ')
    print(f'Grade      : {determine_letter_grade(average)} ')
    print(f'Status     : {check_pass_fail_status(average)} ')
    print("------------------------------")

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    total_subjects = len(marks)
    return total / total_subjects

def find_highest_mark(marks):
    highest = marks[0]
    for score in marks:
        if score > highest:
            highest = score
    return highest

def find_lowest_mark(marks):
    lowest = marks[0]
    for score in marks:
        if score < lowest:
            lowest = score
    return lowest

def determine_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    
def check_pass_fail_status(avg):
    if avg >= 50:
        return "Passed"
    else:
        return "Failed"

# --- MAIN APPLICATION RUNTIME ---

class_records = {}
print("=== Welcome to the Class Performance Analyzer ===")

while True:
    raw_subjects_input = input('Enter Subjects (separated by commas): ').strip()
    
    # Reject empty inputs entirely
    if raw_subjects_input == '':
        print('Error: Subject list cannot be blank.')
        continue

    split_inputs = raw_subjects_input.split(',')
    validated_subjects = []
    has_invalid_subject = False

    for item in split_inputs:
        clean_subject = item.strip()
        
        # Reject empty entries resulting from extra trailing or double commas
        if clean_subject == '':
            print("Error: Detected an empty subject entry. Please format correctly.")
            has_invalid_subject = True
            break
            
        # Reject non-alphabet subject strings
        if not clean_subject.replace(" ", "").isalpha():
            print(f"Error: '{clean_subject}' is invalid. Subjects must contain alphabet characters only.")
            has_invalid_subject = True
            break
            
        # Detect and skip duplicates silently to keep a clean storage list
        if clean_subject not in validated_subjects:
            validated_subjects.append(clean_subject)

    if has_invalid_subject:
        continue

    # Ensure we have at least one successfully processed subject to advance
    if len(validated_subjects) > 0:
        subjects = validated_subjects
        print(f"Validated Subjects Tracked: {', '.join(subjects)}")
        break
    else:
        print('Error: Please enter at least one valid subject.')


# STUDENT DETAILS LOOP 
while True:
    # 1. Name Validation
    while True:
        name = input('\nEnter Name (or type "exit" to view final class stats): ').strip()
        
        if name == '':
            print('Error: Name cannot be blank. Please try again.')
            continue
            
        if name.lower() == 'exit':
            break
            
        # Allow names containing spaces while blocking symbols or digits
        if name.replace(" ", "").isalpha():
            # Check for duplicate student names across existing class records
            if name in class_records:
                print(f"Error: '{name}' already exists. Please use a unique identifier or add a surname.")
                continue
            break
        else:
            print('Error: Name must contain alphabetic characters and spaces only.')
        
    if name.lower() == 'exit':
        break

    # 2. Score Collection and Validation per Subject
    student_marks = {}
    for subject in subjects:
        while True:
            try:
                score_input = input(f"Enter marks for {subject}: ").strip()
                score = int(score_input)
                
                # Check performance boundaries
                if 0 <= score <= 100:
                    student_marks[subject] = score
                    break
                else:
                    print("Error: Marks must fall between the 0 and 100 range.")
            except ValueError:
                print("Error: Please enter a valid whole number (no letters, spaces, or decimals).")

    # Display individual performance instantly upon entry
    display_student_report(name, student_marks)
    
    # Store records inside our nested layout dictionary
    class_records[name] = student_marks


# --- METRICS COMPILATION AND AGGREGATION DISPLAY ---
if len(class_records) > 0:
    print("\n=========================================")
    print("         FINAL CLASS STATISTICS          ")
    print("=========================================")
    
    all_averages = []
    topper_name = ""
    highest_class_avg = -1
    lowest_mark = 101
    lowest_mark_student = ""
    
    passed_students_count = 0
    failed_students_count = 0

    # Iterate through all student records
    for student_name, marks_dict in class_records.items():
        current_marks_list = list(marks_dict.values())
        stud_avg = calculate_average(current_marks_list)
        all_averages.append(stud_avg)
        
        # Track counts of passing and failing students
        if check_pass_fail_status(stud_avg) == "Passed":
            passed_students_count += 1
        else:
            failed_students_count += 1
        
        # Identify Class Topper
        if stud_avg > highest_class_avg:
            highest_class_avg = stud_avg
            topper_name = student_name
            
        # Identify absolute individual minimum score
        for mark in current_marks_list:
            if mark < lowest_mark:
                lowest_mark = mark
                lowest_mark_student = student_name

    total_class_average = calculate_average(all_averages)
    
    print(f"Total Students Processed : {len(class_records)}")
    print(f"Students Passed          : {passed_students_count}")
    print(f"Students Failed          : {failed_students_count}")
    print(f"Overall Class Average    : {total_class_average:.2f}")
    print(f"Class Topper             : {topper_name} (Avg: {highest_class_avg:.2f})")
    print(f"Lowest Mark in Class     : {lowest_mark} (Scored by: {lowest_mark_student})")
    print("=========================================")
else:
    print("\nNo student data was recorded.")
