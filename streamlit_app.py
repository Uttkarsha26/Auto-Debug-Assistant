import streamlit as st
import requests

st.title(" Why Did My Model Break?")
st.subheader("Paste your ML error log or training output below")

user_input = st.text_area("Error Log / Training Metrics", height=200,
    placeholder="e.g. ValueError: Input contains NaN, or paste your full traceback...")

if st.button("🔍 Diagnose"):
    if user_input.strip():
        with st.spinner("Analyzing your error..."):
            response = requests.post(
                "http://localhost:8000/analyze",
                json={"log_text": user_input}
            )
            result = response.json()["diagnosis"]
        st.success("Diagnosis Complete!")
        st.markdown(result)
    else:
        st.warning("Please paste an error log first.")