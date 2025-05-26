# app.py

import streamlit as st
import pandas as pd
from io import StringIO
import base64

st.title("CSV Text to Excel Converter")

st.markdown("Paste your CSV data below, and download the converted Excel file.")

# User input
csv_text = st.text_area("Enter CSV-formatted text here:", height=300)

if st.button("Convert to Excel"):
    if csv_text.strip() == "":
        st.warning("Please paste some CSV data first.")
    else:
        try:
            df = pd.read_csv(StringIO(csv_text))

            # Save to Excel in memory
            output = StringIO()
            excel_buffer = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')
            df.to_excel(excel_buffer, index=False)
            excel_buffer.close()

            # Read bytes to download
            with open("output.xlsx", "rb") as f:
                bytes_data = f.read()
                b64 = base64.b64encode(bytes_data).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="converted.xlsx">Download Excel File</a>'
                st.markdown(href, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Failed to convert CSV to Excel: {e}")
