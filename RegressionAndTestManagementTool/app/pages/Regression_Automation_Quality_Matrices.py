import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Regression Automation Quality Matrices", page_icon="resources/planviewLogo.png",
                   layout="wide")
st.image("resources/Planview-Horizontal-color-RGB.jpeg", width=120)
st.header("Regression Automation Quality Matrices")



regression_history_file = "/RegressionAndTestManagementTool/resources/Regression_History_original.xlsx"

df = pd.read_excel(regression_history_file, sheet_name="RegressionMonitor")


def remove_duplicate_values(values):
    non_duplicate_values = []
    for value in values:
        if value not in non_duplicate_values:
            non_duplicate_values.append(value)
    return non_duplicate_values


def get_job_list(values):
    non_duplicate_values = []
    for value in values:
        non_duplicate_values.append(value)
    return non_duplicate_values


choose = option_menu("Teams: ", ["OKR Jobs", "Insight Jobs", "White Board Jobs", "Tap Jobs"], orientation="horizontal")
if choose:

    job_failure_count, automatable_test_case = st.columns(2)

    job_failure_count.write("Job Failure Count: ")
    job_list = remove_duplicate_values(df.loc[(df["Team"] == choose)].to_dict().get("Job").values())
    failure_count_dict = {}
    all_jobs = get_job_list(df.loc[(df["Team"] == choose)].to_dict().get("Job").values())
    for job in job_list:
        failure_count_dict[job] = all_jobs.count(job)
    team_data_frame = pd.DataFrame({
        "Jobs": remove_duplicate_values(df.loc[(df["Team"] == choose)].to_dict().get("Job").values()),
        "Failure Count": failure_count_dict.values()
    })
    job_failure_count.bar_chart(team_data_frame, x="Jobs", y="Failure Count", height=500, width=300, use_container_width=True)

    automatable_test_case.write("Automatable test cases: ")
    automatable_test_case.image("resources/coming-soon-coming-soon-message-note-hands-holding-paper-sign-announcement-113675278.jpeg")

    automation_pass_rate, automation_execution_time = st.columns(2)
    automation_pass_rate.write("Automation pass rate: ")
    automation_pass_rate.image("resources/coming-soon-coming-soon-message-note-hands-holding-paper-sign-announcement-113675278.jpeg")

    automation_execution_time.write("Automation execution time: ")
    automation_execution_time.image("resources/coming-soon-coming-soon-message-note-hands-holding-paper-sign-announcement-113675278.jpeg")

    automation_test_coverage, automation_script_effectiveness = st.columns(2)
    automation_test_coverage.write("Automation test coverage: ")
    automation_test_coverage.image("resources/coming-soon-coming-soon-message-note-hands-holding-paper-sign-announcement-113675278.jpeg")

    automation_script_effectiveness.write("Automation script effectiveness: ")
    automation_script_effectiveness.image("resources/coming-soon-coming-soon-message-note-hands-holding-paper-sign-announcement-113675278.jpeg")


