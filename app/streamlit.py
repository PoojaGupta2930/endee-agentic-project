import streamlit as st
from agent import agent

st.title("Agentic AI + Endee + RAG")

q = st.text_input("Ask question")

if st.button("Run Agent"):

    ans = agent(q)

    st.write(ans)