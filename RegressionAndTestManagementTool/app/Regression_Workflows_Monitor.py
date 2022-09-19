import streamlit as st
import requests
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Regression Workflows Monitor", page_icon="resources/planviewLogo.png", layout="wide")
st.image("resources/Planview-Horizontal-color-RGB.jpeg", width=120)
st.header("Regression Workflows Monitor")

select_team = option_menu("Teams: ", options=["T-PLATFORMA", "T-OBI"], orientation="horizontal")
# select_env = st.selectbox(label="Environments: ", options=["Dev", "Staging", "Prod"])

headers = {"Accept": "application/vnd.github+json",
           "Authorization": "token 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"}


def fetch(session, url):
    try:
        result = session.get(url, headers=headers)
        return result.json()
    except Exception:
        return {}


session = requests.Session()

if st.button("Let's Analyse"):
    if select_team == "T-PLATFORMA":
        data = fetch(session, f"https://api.github.com/repos/pv-platforma/platforma-automation/actions/workflows")
        workflow_name, status, success_rate_in_last_ten_runs, success_rate = st.columns(4, gap='small')
        workflow_name.write("Work Flow Name")
        status.write("Status")
        success_rate_in_last_ten_runs.write("Success rate in last 10 runs")
        success_rate.write("Overall success rate")
        for work_flow in data.get("workflows"):
            work_flow_name = work_flow.get("name")
            if work_flow_name != 'ci':
                workflow_id = work_flow.get("id")
                run_status = fetch(session, f"https://api.github.com/repos/pv-platforma/platforma-automation/actions"
                                            f"/workflows/{workflow_id}/runs")
                run_id = run_status.get("workflow_runs")[0].get("id")
                jobs_name = fetch(session, f"https://api.github.com/repos/pv-platforma/platforma-automation/actions"
                                           f"/runs/{run_id}/jobs")
                if run_status.get("workflow_runs")[0].get("conclusion") == 'success':
                    status.success(run_status.get("workflow_runs")[0].get("conclusion"))
                else:
                    status.error(run_status.get("workflow_runs")[0].get("conclusion"))
                html_url = run_status.get("workflow_runs")[0].get("html_url")
                workflow_name.info(f"[{work_flow_name}]({html_url})")
                success_count = 0
                failure_count = 0
                for run in run_status.get("workflow_runs"):
                    if run.get("conclusion") == 'success':
                        success_count += 1
                if success_count > 0:
                    success_percentage = (success_count / len(run_status.get("workflow_runs"))) * 100
                else:
                    success_percentage = 0
                success_rate.warning(success_percentage)
                success_count = 0
                failure_count = 0
                for i in range(10):
                    if len(run_status.get("workflow_runs")) > 10:
                        if run_status.get("workflow_runs")[i].get("conclusion") == 'success':
                            success_count += 1
                if success_count > 0:
                    success_percentage = (success_count / len(run_status.get("workflow_runs"))) * 100
                else:
                    success_percentage = 0
                success_rate_in_last_ten_runs.warning(success_percentage)
    else:
        st.error("Error")
