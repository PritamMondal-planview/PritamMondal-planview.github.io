import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="Regression History", page_icon="resources/planviewLogo.png", layout="wide")
st.image("resources/Planview-Horizontal-color-RGB.jpeg", width=120)
st.header("Regression History")

regression_history_file = "/RegressionAndTestManagementTool/resources/Regression_History_original.xlsx"


def remove_duplicate_values(values):
    non_duplicate_values = []
    for value in values:
        if value not in non_duplicate_values:
            non_duplicate_values.append(value)
    return non_duplicate_values


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date, end_date, team, job = st.columns(4)
df = pd.read_excel(regression_history_file, sheet_name="RegressionMonitor")
team_option = st.selectbox('teams', df["Team"].drop_duplicates())
if team_option:
    job_option = st.selectbox('jobs', remove_duplicate_values(df.loc[(df["Team"] == team_option)].to_dict()
                                                              .get("Job").values()))
startDate = start_date.date_input("select start date")
endDate = end_date.date_input("select end date (end date will not be included)")
if st.button("Submit"):
    df1 = []
    for single_date in daterange((date(int(str(startDate)[:4]), int(str(startDate)[5:7]), int(str(startDate)[8:])))
            , date(int(str(endDate)[:4]), int(str(endDate)[5:7]), int(str(endDate)[8:]))):
        date = str(single_date.strftime("%Y-%m-%d"))
        df1.append(df.loc[(df["Team"] == team_option) & (df["Job"] == job_option) & (df["Date"] == date)])
    df3 = pd.concat(df1)
    st.table(df3)


with open(regression_history_file, "rb") as file:
    st.download_button(label="Download Regression_Monitor_History.xlsx", data=file,
                       file_name="Regression_Monitor_History.xlsx", mime='xlsx')
