import functions
import streamlit as st
import streamlit.components.v1 as components
# todos = functions.get_todos()
#
#
# def add_todo():
#     todo = st.session_state["new_todo"] + '\n'
#     todos.append(todo)
#     functions.write_todos(todos_arg=todos)

HtmlFile = open("Beko.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height=1000)

# st.title("Let’s support The Home For Single Mothers in Łódź.")
# st.subheader("This is my todo app.")
# st.write("This app is to increase your productivity")
#
# for index, todo in enumerate(todos):
#     checkbox = st.checkbox(todo, key=todo)
#     if checkbox:
#         todos.pop(index)
#         functions.write_todos(todos_arg=todos)
#         del st.session_state[todo]
#         st.rerun()
# st.text_input(label="Enter to do", placeholder="Add new todo...",
#               on_change=add_todo, key="new_todo")
