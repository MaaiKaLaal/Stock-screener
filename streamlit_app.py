import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pre-Open Screener", layout="wide")

st.title("📊 Pre-Open Screener")

st.markdown("**Upload your Excel file**")

uploaded_file = st.file_uploader("Drag and drop file here", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.success("✅ File uploaded successfully!")

        st.subheader("Preview of Data")
        st.dataframe(df)

        # Optional: Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download as CSV", data=csv, file_name="filtered_data.csv", mime="text/csv")

    except Exception as e:
        st.error(f"❌ Failed to read Excel file: {e}")
else:
    st.info("Awaiting Excel file upload...")
import streamlit as st

try:
    import openpyxl
    st.success("✅ openpyxl is installed.")
except ImportError:
    st.error("❌ openpyxl is NOT installed.")
import streamlit as st
import pandas as pd

# ✅ openpyxl presence check (temporary)
try:
    import openpyxl
    st.success("✅ openpyxl is installed.")
except ImportError:
    st.error("❌ openpyxl is NOT installed.")
