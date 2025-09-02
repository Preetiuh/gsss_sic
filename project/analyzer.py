

from logger import logger

import pandas as pd

def load_data():
    students = pd.read_csv('students.csv')
    courses = pd.read_csv('courses.csv')
    enrollments = pd.read_csv('enrollments.csv')
    grades = pd.read_csv('grades.csv')
    grades['Grade'] = grades['Grade'].fillna(0)
    
    merged = enrollments.merge(students, on='StudentID')
    merged = merged.merge(grades, on=['StudentID', 'CourseID'], how='left')
    merged = merged.merge(courses, on='CourseID', how='left')
    merged['Result'] = merged['Grade'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
    return merged

def get_student_view(username, df):
    student_df = df[df['Name'].str.lower() == username.lower()]
    ranked_df = df.groupby('Name')['Grade'].mean().sort_values(ascending=False).reset_index()
    all_marks = df[['Name', 'CourseName', 'Grade']].dropna()

    return {
        'name': username,
        'gpa': student_df['Grade'].mean(),
        'result': student_df['Result'].iloc[0],
        'ranked_df': ranked_df
    }

def get_mentor_view(df, sort_by='Grade', filter_result=None):
    # Group and aggregate student data
    summary = df.groupby('Name').agg({
        'Grade': 'mean',
        'Result': lambda x: x.mode()[0],
        'Department_x': 'first'  # Use the correct column name from merged DataFrame
    }).reset_index()


    # Rename column for clean display
    summary = summary.rename(columns={'Department_x': 'Department'})

    # Apply filtering if requested
    if filter_result:
        summary = summary[summary['Result'] == filter_result]

    # Sort the results
    return summary.sort_values(by=sort_by, ascending=False)

