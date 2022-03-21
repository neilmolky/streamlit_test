import streamlit as st

heading = st.header("A rather Cliche first app")

with st.sidebar:
    check = st.checkbox("change colours?")

colour = "black"
if check:
    colour = "rainbow"


msg = st.write("hello world", colour=colour)



