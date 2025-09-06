import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pre-Open Screener", layout="wide")
st.title("📊 Pre-Open Screener")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Load Excel with row 2 (index=1) as header
    df = pd.read_excel(uploaded_file, header=1)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace('"', '')

    # Show preview
    st.subheader("📋 Data Preview")
    st.dataframe(df.head())

    # Helper: find closest matching column name
    def find_col(possible_names):
        for name in df.columns:
            for target in possible_names:
                if target.lower() in name.lower().replace(" ", ""):
                    return name
        return None

    # Detect required columns
    col_ticker = find_col(["Ticker"])
    col_c = find_col(["Open"])
    col_h = find_col(["Low"])
    col_i = find_col(["High"])
    col_n = find_col(["PreOpe", "Pre Ope", "Pre"])

    required_cols = [col_ticker, col_c, col_h, col_i, col_n]

    if None in required_cols:
        st.error(f"❌ Missing some required columns. Found: {required_cols}")
    else:
        # Convert numeric safely
        for col in [col_c, col_h, col_i, col_n]:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        # Conditions
        cond1_pos = df[col_n] >= 0.02
        cond1_neg = df[col_n] <= -0.02
        cond2_pos = df[col_c] > df[col_i]
        cond2_neg = df[col_c] < df[col_h]

        # Matches
        pos_matches = df.loc[cond1_pos & cond2_pos, col_ticker].unique()
        neg_matches = df.loc[cond1_neg & cond2_neg, col_ticker].unique()

        # Show results
        st.subheader("✅ Positive Matches")
        if len(pos_matches) > 0:
            for ticker in pos_matches:
                st.markdown(f"<span style='color:green; font-weight:bold'>{ticker}</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color:grey'>No Match</span>", unsafe_allow_html=True)

        st.subheader("❌ Negative Matches")
        if len(neg_matches) > 0:
            for ticker in neg_matches:
                st.markdown(f"<span style='color:red; font-weight:bold'>{ticker}</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color:grey'>No Match</span>", unsafe_allow_html=True)
