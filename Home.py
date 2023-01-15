import streamlit as st
import functions_final

todos = functions_final.get_todos()

def add_todo():
    # session_state looks like a dictionary; it's a special type of object
    # "new_todo": "Hello"
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions_final.write_todos(todos)

# Streamlit is a new library -- makes it easy to create web apps
# To run this app, type in terminal:  streamlit run Home.py
# Each user session on a web app is separate -- the script is executed separately

# To create a requirements.txt file:  pip freeze > requirements.txt
# Requirements.txt is loaded to the server so that it know all the Python
# libraries that it needs to install
# pip freeze would show all the libraries in the command line


st.set_page_config(layout="wide")

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("<h4><b>This app is to increase your productivity</b>.<h4>",
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_final.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


# Getting from the text box
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# To observe the session state
# st.session_state