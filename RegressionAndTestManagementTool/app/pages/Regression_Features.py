import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="Regression Features", page_icon="resources/planviewLogo.png", layout="wide")
st.image("resources/Planview-Horizontal-color-RGB.jpeg", width=120)
st.header("Regression Features")

features_directory_path = str(os.getcwd()) + "/tests"
teams = os.listdir(features_directory_path)


def load_features(feature_directory_path, feature):
    for file in os.listdir(feature_directory_path):
        if str(file) == str(feature):
            file = open(feature_directory_path + file)
            lines = file.readlines()
            for line in lines:
                if line.startswith("Feature"):
                    st.header(line)
                elif line.startswith("  Background") or line.startswith("  Scenario") or line.startswith(
                        "    Examples"):
                    st.code(line, language="gherkin")
                else:
                    st.text(line)


def save_uploaded_file(uploaded_feature_files, directory_path):
    for feature_file in uploaded_feature_files:
        with open(os.path.join(directory_path, feature_file.name), "wb") as f:
            f.write(feature_file.getbuffer())


def enter_details_for_existing_teams():
    st.write("Existing team - Enter details below: ")
    select_existing_team, select_existing_module, enter_new_module = st.columns(3)
    existing_team = select_existing_team.selectbox("Existing Teams: ", teams)
    if existing_team:
        modules = os.listdir(features_directory_path + "/" + existing_team)
        modules.append("No Existing Module")
        existing_module = select_existing_module.selectbox("Existing Modules: ", modules)
        if existing_module == "No Existing Module":
            new_module_for_existing_team = enter_new_module.text_input("Please enter new module name")
    uploaded_feature_files = st.file_uploader("Please upload your feature file", accept_multiple_files=True)
    feature_submit_button_for_existing_team = st.button("Submit Feature to existing team")
    if feature_submit_button_for_existing_team:
        if existing_module == "No Existing Module":
            if new_module_for_existing_team:
                os.mkdir(features_directory_path + "/" + existing_team + "/" + new_module_for_existing_team)
                save_uploaded_file(uploaded_feature_files,
                                   features_directory_path + "/" + existing_team + "/" + new_module_for_existing_team)
            else:
                save_uploaded_file(uploaded_feature_files,
                                   features_directory_path + "/" + existing_team + "/" + existing_module)


def enter_details_for_new_team():
    st.write("New team - Enter details below: ")
    enter_team_name, enter_module_name = st.columns(2)
    new_team = enter_team_name.text_input("New Team Name")
    new_module = enter_module_name.text_input("New Module Name")

    uploaded_feature_files = st.file_uploader("Please upload your feature file for your new team",
                                              accept_multiple_files=True)
    feature_submit_button_for_non_existing_team = st.button("Submit Feature to new team")
    if feature_submit_button_for_non_existing_team:
        os.mkdir(features_directory_path + "/" + new_team)
        os.mkdir(features_directory_path + "/" + new_team + "/" + new_module)
        for feature_file in uploaded_feature_files:
            with open(os.path.join(features_directory_path + "/" + new_team + "/" + new_module,
                                   feature_file.name), "wb") as f:
                f.write(feature_file.getbuffer())


with st.sidebar:
    st.header("Please enter your new feature test details if you have any: ")
    enter_details_for_existing_teams()
    enter_details_for_new_team()

choose_team = option_menu("Teams: ", teams, orientation="horizontal", menu_icon="bookshelf")
if choose_team:
    modules = os.listdir(features_directory_path + "/" + choose_team)
    select_module, select_feature = st.columns(2)
    choose_modules = select_module.selectbox("Modules: ", modules)
    if choose_modules:
        choose_feature = select_feature.selectbox("Feature", os.listdir(features_directory_path + "/"
                                                                        + choose_team + "/" + choose_modules + "/"))
        load_features(features_directory_path + "/" + choose_team + "/" + choose_modules + "/", choose_feature)
