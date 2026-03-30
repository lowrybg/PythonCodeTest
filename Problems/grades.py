# Write a program that calculates statistics for grades in an exam.
# In the beginning, the program receives the number of students who attended the exam and
# for each student – their grade. In the end, the program must print the percentage of students
# that have grades between 2.00 and 2.99, between 3.00 and 3.99, between 4.00 and 4.99, 5.00 or
# more, as well as the average grade of the exam.
#
# Input Data
# On the console are being read a sequence of numbers, each on a different row:
#
# On the first line – the number of students who attended the exam – an integer within the range [1 … 1000].
# For each student on a separate line – the grade on the exam – a real number within the range [2.00 … 6.00].
# Output Data
# Print on the console 5 lines that hold the following information:
#
# "Top students: {percentage of students with a grade of 5.00 or more}%".
# "Between 4.00 and 4.99: {between 4.00 and 4.99 included}%".
# "Between 3.00 and 3.99: {between 3.00 and 3.99 included}%".
# "Fail: {less than 3.00}%".
# "Average: {average grade}".
# The results must be formatted up to the second symbol after the decimal point.


def calculate_exam_statistics():
    # Read the total number of students
    students_count = int(input())


    top_students = 0
    good_students = 0  # 4.00 to 4.99
    average_students = 0  # 3.00 to 3.99
    fail_students = 0  # Less than 3.00


    total_grades_sum = 0.0


    for _ in range(students_count):
        grade = float(input())
        total_grades_sum += grade

        # Categorize the grade
        if grade >= 5.00:
            top_students += 1
        elif grade >= 4.00:
            good_students += 1
        elif grade >= 3.00:
            average_students += 1
        else:
            fail_students += 1


    p_top = (top_students / students_count) * 100
    p_good = (good_students / students_count) * 100
    p_average = (average_students / students_count) * 100
    p_fail = (fail_students / students_count) * 100

    # Calculate the overall average grade
    average_grade = total_grades_sum / students_count



    print(f"Top students: {p_top:.2f}%")
    print(f"Between 4.00 and 4.99: {p_good:.2f}%")
    print(f"Between 3.00 and 3.99: {p_average:.2f}%")
    print(f"Fail: {p_fail:.2f}%")
    print(f"Average: {average_grade:.2f}")



if __name__ == "__main__":
    calculate_exam_statistics()