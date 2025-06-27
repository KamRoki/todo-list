import streamlit as st
from utils.task_manager import load_tasks, save_tasks
from datetime import date

st.set_page_config(page_title = 'To-Do List App',
                   layout = 'centered')

st.title('📝 To-Do List App')
st.caption('Manage your tasks efficiently and without stress!')
st.caption('By Kamil Stachurski')


tasks = load_tasks()

# Add new task form
with st.form('new_task_form',
             clear_on_submit = True):
    new_task = st.text_input('New Task:')
    deadline = st.date_input('Deadline:',
                             value = date.today())
    submitted = st.form_submit_button('➕ Add Task')
    if submitted and new_task.strip():
        tasks.append({'task': new_task.strip(),
                      'completed': False,
                      'deadline': str(deadline)})
        save_tasks(tasks)
        st.rerun()
        
st.markdown('---')
st.subheader('📋 Your Tasks:')

# Task list
if 'task_completed' not in st.session_state:
    st.session_state.task_completed = False
    
if st.session_state.task_completed:
    st.success("✅ Task completed!")
    st.session_state.task_completed = False
    
for i, task in enumerate(tasks.copy()):
    col1, col2 = st.columns([0.1, 0.9])
    
    if col1.button('✔️',
                   key = f'done_{i}'):
        tasks.pop(i)
        save_tasks(tasks)
        st.session_state.task_completed = True
        st.rerun()
        
    col2.markdown(f"**{task['task']}**  \n📅 Deadline: `{task.get('deadline', '---')}`")
