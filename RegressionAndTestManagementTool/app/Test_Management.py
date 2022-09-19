import json

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Planview Test Management", layout="wide")
st.title("Planview Test Management")

file = "/resources/PlanviewRegressionSuites.xlsx"
json_file = "/resources/OKR_Tests/Regression.json"



select_team = st.selectbox(label="Teams: ", options=["select team", "T-OBI", "T-OKR"])
select_feature = st.selectbox(label="Features: ", options=["select feature", "OKR-E1 Integration"])
select_test_suite = st.selectbox(label="Test Suites: ", options=["select test suite", "Regression"])

# def add_test_case(test_name, test_steps, comments):
#     test = st.button(test_name)
#     if test:
#         st.text(test_steps)
#         st.text(comments)
#         data = {"test steps": [test_steps], "comments": [comments]}
#         df = pd.DataFrame(data)
#         st.table(df)

test_case_dict = []


def add_test_case(test_name, test_steps, comments):
    test_case_dict.append(test_name)


def show_test_cases():
    tests = st.button(label="test cases: ", args=test_case_dict)
    if tests:
        st.text(test_case_dict)


#
# if select_team == "T-OBI":
#     select_feature = st.selectbox(label="Features: ", options=["select feature", "OKR-E1 Integration"])
#     if select_feature == "OKR-E1 Integration":
#         select_test_suite = st.selectbox(label="Test Suites: ", options=["select test suite", "Regression"])
#         if select_test_suite == "Regression":
#             add_test_case("Happy Flow", "1. Test", "testing")
#             add_test_case("Sad Flow", "1. Test", "testing")


# def submit(team, feature, test_suite):
#     if select_team == team and select_feature == feature and select_test_suite == test_suite:
#         test = st.button("submit")
#         if test:
#             add_test_case("Happy Flow", "1. Test", "testing")
#             add_test_case("Sad Flow", "1. Test", "testing")
#             # st.text(test_case_dict)
#             # with st.expander("Test Cases"):
#             #     col1, col2, col3, col4 = st.columns(4)
#             #     col1.write(test_case_dict[0])
#             #     col2.write(test_case_dict[1])
#             #     col3.write(test_case_dict[0])
#             #     col4.write(test_case_dict[1])
#             #     st.table(pd.read_excel(file))
#
#             with st.expander("Test Cases"):
#                 data = pd.read_excel(file)
#                 while not data.empty:
#                     st.


# def submit(team, feature, test_suite):
#     if select_team == team and select_feature == feature and select_test_suite == test_suite:
#         test = st.button("submit")
#         if test:
#             st.table(pd.read_excel(file, sheet_name="okr"))
#

def read_from_json():
    with open(json_file, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object

def submit(team, feature, test_suite):
    if select_team == team and select_feature == feature and select_test_suite == test_suite:
        test = st.button("submit")
        if test:
            for test in read_from_json()["regression"]:
                st.button(read_from_json()["regression"][test]["test_name"])


submit("T-OKR", "OKR-E1 Integration", "Regression")
