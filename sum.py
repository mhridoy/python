import streamlit as st

st.title ("Sum Numbers in a range")



start = st.text_input("Enter the initial value")
conditionOrStop = st.text_input("Enter the final value")
step = st.text_input("Enter the step")

sum =0

if(st.button('Submit')):
    # String to interger convertion
    start = int(start)
    conditionOrStop = int(conditionOrStop)
    step = int(step)
    for i in range (start, conditionOrStop+1, step):
        st.write(i)
        sum = sum + i

st.write("The sum = ",sum)


