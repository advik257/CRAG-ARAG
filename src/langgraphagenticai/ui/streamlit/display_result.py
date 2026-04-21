import streamlit as st
from langchain.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultsstreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_results(self):
        """
        Function to display the results in the Streamlit app.
        """
        st.title("Results Display")

        if self.usecase == "Basic Chatbot":
            # Assuming graph.stream expects a dict with 'messages' as a list
            for event in self.graph.stream({'messages': [HumanMessage(content=self.user_message)]}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    # Display user message
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    # Assuming value['messages'] is a list of messages, get the last AI message
                    if 'messages' in value and value['messages']:
                        last_message = value['messages'][-1]
                        if isinstance(last_message, AIMessage):
                            with st.chat_message("assistant"):
                                st.write(last_message.content)
                        else:
                            st.write(f"Non-AI message: {last_message}")