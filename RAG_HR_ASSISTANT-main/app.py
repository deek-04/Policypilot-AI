import streamlit as st
from QueryProcessor import process_user_query

st.set_page_config(
    page_title="AI HR Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI HR Assistant")

st.caption("Ask questions about your company's HR policies.")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask your HR question...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = process_user_query(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )