import os
import pickle
import streamlit as st

# Define base path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, "data")

st.title("Course Recommender")

courses_list = pickle.load(open(os.path.join(DATA_PATH, "courses.pkl"), 'rb'))
similarity = pickle.load(open(os.path.join(DATA_PATH, "similarity.pkl"), 'rb'))

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:7]]
    return recommended_course_names

course_list = courses_list['course_name'].values
selected_course = st.selectbox("Type or select a course you like:", course_list)

if st.button('Show Recommended Courses'):
    st.write("Recommended Courses based on your interests:")
    for course in recommend(selected_course):
        st.text(course)
