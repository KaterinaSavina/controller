import streamlit as st
import requests
import psycopg2

def connect_db(x):
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="DB_for_python",
        user="postgres",
        password="1111",
    )
    connection.set_session(autocommit=True)
    with connection.cursor() as cursor:
        if x == "Error":
            cursor.execute("SELECT description FROM response_for_controller where error like 'Error'")
            result = cursor.fetchone()
            for row in result:
                return (row[::])
        else:
            cursor.execute("SELECT description FROM response_for_controller where error like 'Ок'")
            result = cursor.fetchone()
            for row in result:
                return(row[::])
    return(result)

def process_text():

    form = st.form(key='my_form')
    url = form.text_input(label="Введите адрес ресурса", placeholder="https://")
    submit_button = form.form_submit_button(label='Обработать')

    response = requests.get(url)
    if response.status_code != 200:
        st.write("Ошибка:")
        st.write(response.status_code)
        st.write(connect_db("Error"))

    else:
        st.write(connect_db("Ok"))

process_text()
