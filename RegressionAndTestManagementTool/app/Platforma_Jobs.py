import requests
import json

headers = {"Accept": "application/vnd.github+json",
           "Authorization": "token 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"}


def fetch(session, url):
    try:
        result = session.get(url, headers=headers)
        return result.json()
    except Exception:
        return {}


session = requests.Session()


class Platforma_Jobs:
    workflows = fetch(session, f"https://api.github.com/repos/pv-platforma/platforma-automation/actions/workflows")

    okr_workflows = {}
    white_board_workflows = {}
    tap_workflows = {}
    insights_workflows = {}

    def get_job_details(self, job):
        return {"status": job.get("conclusion"),
         "job_id": job.get("id"),
         "html_url": job.get("html_url"),
         "comments": None
                }

    def return_all_workflow_data(self):
        for work_flow in self.workflows.get("workflows"):
            work_flow_id = work_flow.get("id")
            workflow_runs = fetch(session,
                                  f"https://api.github.com/repos/pv-platforma/platforma-automation/actions/workflows"
                                  f"/{work_flow_id}/runs")
            workflow_run_id = workflow_runs.get("workflow_runs")[0].get("id")
            workflow_jobs = fetch(session,
                                  f"https://api.github.com/repos/pv-platforma/platforma-automation/actions/runs/{workflow_run_id}/jobs")
            work_flow_name = str(work_flow.get("name"))
            for job in workflow_jobs["jobs"]:
                if work_flow_name.lower().__contains__("okr"):
                    self.okr_workflows[job.get("name")] = self.get_job_details(job)
                elif work_flow_name.lower().__contains__("whiteboard"):
                    self.white_board_workflows[job.get("name")] = self.get_job_details(job)
                elif work_flow_name.lower().__contains__("tap"):
                    self.tap_workflows[job.get("name")] = self.get_job_details(job)
                elif work_flow_name.lower().__contains__("insights"):
                    self.insights_workflows[job.get("name")] = self.get_job_details(job)
        return {"OKR Jobs": self.okr_workflows , "White Board Jobs": self.white_board_workflows,
                "Tap Jobs": self.tap_workflows, "Insight Jobs": self.insights_workflows}


platforma_jobs = Platforma_Jobs()
# Serializing json
json_object = json.dumps(platforma_jobs.return_all_workflow_data(), indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
print(json_object)
