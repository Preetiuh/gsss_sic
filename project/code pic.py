import pandas as pd

# Load datasets
students = pd.read_csv('students.csv')
courses = pd.read_csv('courses.csv')
enrollments = pd.read_csv('enrollments.csv')
grades = pd.read_csv('grades.csv')

# Inspect
print("Students:\n", students.head())
print("Courses:\n", courses.head())
print("Enrollments:\n", enrollments.head())
print("Grades:\n", grades.head())

# Fill missing grades with 0
grades['Grade'] = grades['Grade'].fillna(0)

# Drop duplicates
students.drop_duplicates(inplace=True)

print("Grades after filling missing values:\n", grades)
print("Students after dropping duplicates:\n", students)


# Merge enrollments with students
student_courses = pd.merge(enrollments, students, on='StudentID', how='inner')

# Merge with grades
student_performance = pd.merge(student_courses, grades, on=['StudentID', 'CourseID'], how='left')

# Merge with courses for subject info
full_data = pd.merge(student_performance, courses, on='CourseID', how='left')


# View final merged data
print("Full Merged Data:\n", full_data.head())


# GPA per student
gpa = full_data.groupby('Name')['Grade'].mean().reset_index().rename(columns={'Grade': 'GPA'})

# Subject-wise stats
subject_stats = full_data.groupby('CourseName')['Grade'].agg(['mean', 'max', 'min']).reset_index()

# Result column
full_data['Result'] = full_data['Grade'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

# Grade category
def grade_category(avg):
    if avg >= 90: return 'A'
    elif avg >= 75: return 'B'
    elif avg >= 60: return 'C'
    elif avg >= 40: return 'D'
    else: return 'F'

gpa['Grade'] = gpa['GPA'].apply(grade_category)

# View GPA and grade
print("Student GPA and Grade:\n", gpa)

# Subject-wise stats
subject_stats = full_data.groupby('CourseName')['Grade'].agg(['mean', 'max', 'min']).reset_index()
print("Subject Stats:\n", subject_stats)


# Top 3 performers
top_3 = gpa.sort_values(by='GPA', ascending=False).head(3)

# Pass/Fail count
pass_fail = full_data['Result'].value_counts()

# Subject with highest average
top_subject = subject_stats.sort_values(by='mean', ascending=False).head(1)

print("Top Subject by Average Grade:\n", top_subject)

gpa.to_csv('student_gpa.csv', index=False)
subject_stats.to_csv('subject_stats.csv', index=False)