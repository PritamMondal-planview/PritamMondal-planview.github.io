import streamlit as st
import pandas as pd

st.set_page_config(page_title="New Test Case", layout="wide")
st.title("New Test Case")

file = "/resources/PlanviewRegressionSuites.xlsx"


def write_to_csv(data_frame):
    df = pd.DataFrame(data=data_frame)
    # df.to_excel(file, sheet_name="okr", index_label="serial_no")
    # af = pd.read_excel(file)
    with pd.ExcelWriter(file, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="okr", header=False, startrow=writer.sheets["okr"].max_row, index=False)
    return df


with st.form(key="enter new test case"):
    test_case_name = st.text_input("test name")
    test_case_steps = st.text_area("test steps")
    submit = st.form_submit_button("submit")
    data = {"test name: ": [test_case_name], "steps": [test_case_steps]}
    st.table(write_to_csv(data))
