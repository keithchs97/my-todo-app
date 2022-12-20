import streamlit as st
import main_functions

todos = main_functions.read_file()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.title())
    main_functions.write_file(todos)

st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This app is to increase your <b>productivity<b>.",
         unsafe_allow_html=True)

st.text_input(label="Add new todo: ", placeholder="Add new to do...",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo, )

    if checkbox:
        todos.pop(index)
        main_functions.write_file(todos)

        del st.session_state[todo]
        st.experimental_rerun()




