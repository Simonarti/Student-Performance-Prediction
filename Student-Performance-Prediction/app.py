import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Prediction System")

st.header("📥 Enter Student Details")

# Inputs
study_hours = st.slider("Study Hours", 0, 10, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
resources = st.selectbox("Resources Available", [0,1])
extracurricular = st.selectbox("Extracurricular Activities", [0,1])
motivation = st.selectbox("Motivation Level", [0,1,2])
internet = st.selectbox("Internet Access", [0,1])
gender = st.selectbox("Gender", [0,1])
age = st.slider("Age", 15, 25, 18)
learning_style = st.selectbox("Learning Style", [0,1,2])
online_courses = st.selectbox("Online Courses", [0,1])
discussions = st.selectbox("Participation in Discussions", [0,1,2])
assignment = st.slider("Assignment Completion (%)", 0, 100, 70)
exam_score = st.slider("Exam Score", 0, 100, 65)
edutech = st.selectbox("Use of EduTech", [0,1])
stress = st.selectbox("Stress Level", [0,1,2])

# Prediction
if st.button("🔮 Predict Performance"):
    
    sample = pd.DataFrame([[study_hours, attendance, resources, extracurricular,
                            motivation, internet, gender, age, learning_style,
                            online_courses, discussions, assignment,
                            exam_score, edutech, stress]],
                          
                          columns=['StudyHours', 'Attendance', 'Resources', 'Extracurricular',
                                   'Motivation', 'Internet', 'Gender', 'Age', 'LearningStyle',
                                   'OnlineCourses', 'Discussions', 'AssignmentCompletion',
                                   'ExamScore', 'EduTech', 'StressLevel'])
    
    prediction = model.predict(sample)[0]

    # Grade mapping
    grade_map = {0: "D", 1: "C", 2: "B", 3: "A"}

    st.subheader("📊 Result")
    st.success(f"Predicted Grade: {grade_map[prediction]}")

# Footer
st.markdown("---")
st.write("ML Project - Student Performance Prediction")