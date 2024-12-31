import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

# Database configuration
DB_HOST = "127.0.0.1"  # Replace with your MySQL server host (e.g., IP address or domain)
DB_PORT = "3306"  # MySQL default port
DB_NAME = "student_database"  # Replace with your database name
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = urllib.parse.quote("7678319044@1")  # URL-encode your password if it contains special characters

# Create a connection to the database
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# function to update data
def update_data(Student_id, field , new_value):
    query = text (f"update student_Data set {field} = :new_value where id = :student_id")
    with engine.connect () as conn :
        conn.execute(query, {"new_value": new_value , "student_id": student_id})
        conn.commit()

#streamlit UI

st.title("update student data")
student_id=st.number_input("enter student id  to update ", min_value=1,step=1)
field = st.selectbox("field to update ",["firstname","lastname","title","age","nationality","registration","num_courses","num_semesters"] )
new_value= st.text_input("new value")
if st.button("update"):
    try:
        update_data(student_id, field,new_value)
        st.success("data sucessfully updated")
    except Exception as e :
        st.error(f"error updating data : {e}")