import streamlit as st
from streamlit_option_menu import option_menu
import json

st.set_page_config(page_title="OKR Tests", layout="wide")
st.title("OKR Tests")

json_file = "/resources/OKR_Tests/Regression.json"

with st.sidebar:
    choose = option_menu("Suites", ["Regression", "Smoke"])


def read_from_json():
    with open(json_file, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object


okr_regression_tests = {}

if choose == "Regression":
    total_tests = len(read_from_json()["regression"])
    col1, col2, col3 = st.columns(3)
    c = 1
    for test in read_from_json()["regression"]:
        okr_regression_tests[read_from_json()["regression"][test]["test_name"]] = \
            {
                "pre requisites": read_from_json()["regression"][test]["pre_requisite"],
                "test steps": read_from_json()["regression"][test]["test_steps"],
                "required apis": read_from_json()["regression"][test]["required_apis"],
                "comments": read_from_json()["regression"][test]["comments"]
            }
        if c <= 10:
            col1.text(read_from_json()["regression"][test]["test_name"])
            col1.json(okr_regression_tests[read_from_json()["regression"][test]["test_name"]], expanded=False)
        elif 10 < c <= 20:
            col2.text(read_from_json()["regression"][test]["test_name"])
            col2.json(okr_regression_tests[read_from_json()["regression"][test]["test_name"]], expanded=False)
        elif 20 < c <= 30:
            col3.text(read_from_json()["regression"][test]["test_name"])
            col3.json(okr_regression_tests[read_from_json()["regression"][test]["test_name"]], expanded=False)
        c += 1
