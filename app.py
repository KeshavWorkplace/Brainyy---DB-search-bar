import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # loading env variable

# configure API key
genai.configure(api_key=GOOGLE_API_KEY)

# function to load google gemini model and provide sql query as response


def get_gemini_reponse(question, prompt, p_index):
    model = genai.GenerativeModel('gemini-pro')
    # this prompt para tell how model should behave and question is the actual question
    response = model.generate_content([prompt[p_index], question])
    return response.text

# function to retrieve


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# define prompt

prompt = [
    """
You are an expert in converting English questions to SQL query! 
The SQL database has the name Employee and has the following columns -  EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50), LastName VARCHAR(50), Department VARCHAR(50), Position VARCHAR(50), HireDate DATE, Salary DECIMAL(10, 2) \n\nFor example, \nExample 1 - How many entries of records are present?,the SQL command will be something like this SELECT COUNT(*) FROM Employee ;\nExample 2 - Tell me all the employees having salary more than 50000?,the SQL command will be something like this SELECT * FROM Employee where Salary>50000;
also the sql code should not have ```
in beginning or end and sql word in output
""",
    '''
You are an expert in pharasing english sentences.
You are given a question and its answer and you rephrase the answer without changing it's data value in
proper english in context with the question\n\n
Example 1 -  name all the students ? \n ((Aman,) (Raju,)(Raj,)) and returned reponse should be \n The name of all the students
are: - \n 1. Aman\n 2. Raju\n 3. Rajesh
Example 2 -  Average marks of all the students \n (22.94496800,) and the 
returned response should be \n The average marks of all the students are: 23.94
also the response should not have ```
in beginning or in the end.
 '''
]

st.set_page_config(page_title='Brainyy')
st.header('Brainyy')
question = st.text_input("Input: ", key="input")

submit = st.button("Search 🔍")

if submit:
    response = get_gemini_reponse(question, prompt, 0)
    print(response)
    response.replace("```", "")
    data = read_sql_query(response, 'Employee.db')
    response = get_gemini_reponse(question + ' \n' + str(data), prompt, 1)
    st.subheader(response)
