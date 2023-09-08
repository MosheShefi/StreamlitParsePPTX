# Import convention
import streamlit as st
from pptx import Presentation
# import glob
# import pathlib
# import os.path

st.write("""# File Picker""")
         
uploaded_files = st.file_uploader("Choose a PPTX file",accept_multiple_files=True)

def upload():
    if uploaded_files is None:
        st.session_state["upload_state"] = "Upload a file first!"
        st.write("Upload a file first!")
    else:
        for uploaded_file in uploaded_files:
            prs = Presentation(uploaded_file)
            st.write("---------- " + uploaded_file.name + " -------------")
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        st.write(shape.text)

st.button("Parse text out of PPTX file/s", on_click=upload)

