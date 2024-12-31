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

#function to fetch data

def fetch_data():
    query = text("select * from student_Data")
    try :
        with engine.connect() as conn :
            result = conn.execute(query)
            columns = result.keys ()
            data = [dict(zip(columns,row)) for row in result]
            return data
    except Exception as e :
        st.error (F"error fetching data : {e}")
        return []
    

st.title("view student data")

data = fetch_data ()

if data:
    st.table(data)
else:
    st.info("no  data found in tha database.")