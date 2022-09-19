import streamlit as st
import json
from datetime import date as dt
import pandas as pd


from streamlit_option_menu import option_menu

st.set_page_config(page_title="Regression Workflow Jobs Monitor", page_icon="resources/planviewLogo.png", layout="wide")
st.image("resources/Planview-Horizontal-color-RGB.jpeg", width=120)
st.header("Regression Workflow Jobs Monitor")

headers = {"Accept": "application/vnd.github+json",
           "Authorization": "token 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"}

regression_history_file = "/RegressionAndTestManagementTool/resources/Regression_History_original.xlsx"


def write_to_excel(data_frame):
    df1 = pd.read_excel(regression_history_file)
    df2 = pd.DataFrame(data=data_frame)
    df3 = pd.concat([df1,df2])
    df3.to_excel(regression_history_file, index=False, sheet_name="RegressionMonitor")


def fetch_data(json_file):
    with open(json_file, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object


choose = option_menu("Teams: ", ["T-OKR", "T-Insights", "T-Whiteboard", "T-Tap"], orientation="horizontal")


def get_job_details(team_jobs):
    job_run_details = fetch_data('app/sample.json')
    jobs = job_run_details.get(team_jobs)
    failed_jobs_list = []
    if jobs is not None:
        for job in jobs:
            job_name.info(f"[{job}]({jobs[job].get('html_url')})")
            comments.info(jobs[job].get("comments"))
            if jobs[job].get("status") == "success":
                job_status.success(jobs[job].get("status"))
                # failed_jobs_list.append(job)
            else:
                job_status.error(jobs[job].get("status"))
                failed_jobs_list.append(job)
    failed_jobs = st.multiselect("Select failed jobs to provide comments", failed_jobs_list)
    if failed_jobs:
        failure_comments = st.text_area("Failure Comments")
        owner = st.text_input("commented by")
        if st.button("submit"):
            for failed_job in failed_jobs:
                job_run_details[team_jobs][failed_job]["comments"] = failure_comments + " : " + owner + " : " + str(
                    dt.today())
                job_failure_comments = {"Date": [str(dt.today())], "Team": [team_jobs], "Job": [failed_job],
                                        "Comments": [job_run_details[team_jobs][failed_job]["comments"]]}
                write_to_excel(job_failure_comments)
            with open("app/sample.json", "w") as jsonFile:
                json.dump(job_run_details, jsonFile, indent=4)


job_name, job_status, comments = st.columns(3)
if choose == "T-OKR":
    get_job_details("OKR Jobs")
if choose == "T-Insights":
    get_job_details("Insight Jobs")
if choose == "T-Whiteboard":
    get_job_details("White Board Jobs")
if choose == "T-Tap":
    get_job_details("Tap Jobs")
