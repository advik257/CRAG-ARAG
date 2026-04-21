import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import config

class LoadStreamlitUI:

    def __init__(self, config: config):
        self.config = config
        self.usercontrols = {}

    def load_ui(self):
        page_title = self.config.get_page_title() or "LangGraph Agentic AI"
        st.set_page_config(page_title="  🤖  " +   page_title,  layout="wide")
        st.header("  🤖  " +   page_title)

        with st.sidebar:
            st.subheader("Configuration")
            self.usercontrols["llm"] = st.selectbox("Select LLM", options=self.config.get_llm_options())

            if self.usercontrols["llm"] == "Groq":
                self.usercontrols["selected_groq_model"] = st.selectbox("Select GROQ Model", options=self.config.get_groq_model_options())
                self.usercontrols["GROQ_API_Key"] = st.text_input("GROQ_API_Key", type="password", key="groq_api_key")

                # warning
                if not self.usercontrols["GROQ_API_Key"]:
                    st.warning("Please enter your GROQ API Key to use GROQ LLM. Refer to the documentation for more details: https://www.groq.com/docs.")

            # Use Case selection
            self.usercontrols["Selected_Use_Case"] = st.selectbox("Select Use Case", options=self.config.get_usecase_options())

        return self.usercontrols
    
