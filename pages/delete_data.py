import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

# Database configuration
DB_HOST = "127.0.0.1"  # Replace with your MySQL server host
DB_PORT = "3306"  # MySQL default port
DB_NAME = "student_database"  # Replace with your database name
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = urllib.parse.quote("7678319044@1")

db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

def delete_data(student_id):
    query = text("DELETE FROM Student_data WHERE id = :student_id")
    with engine.begin() as conn:  # Use begin() for transaction management
        conn.execute(query, {"student_id": student_id})

st.title("Delete Student Data")
student_id = st.number_input("Enter Student Id to Delete", min_value=1, step=1)
if st.button("Delete"):
    try:
        delete_data(student_id)
        st.success(f"Data with Student ID {student_id} successfully deleted!")
    except Exception as e:
        st.error(f"Error deleting data: {e}")
