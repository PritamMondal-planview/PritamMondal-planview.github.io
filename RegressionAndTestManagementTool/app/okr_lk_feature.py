import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

st.set_page_config(page_title="OKR Tests", layout="wide")
# st.title("OKR Tests")

with st.sidebar:
    choose = option_menu("Suites", ["Regression", "Smoke"])
if choose == "Regression":
    HtmlFile1 = open("/Users/pritam.mondal/Repos/automation/features2html/output_features2html/features_20220824_2049.html", 'r', encoding='utf-8')
    HtmlFile2 = open("/Users/pritam.mondal/Repos/automation/features2html/output_features2html/features_20220824_2022.html", 'r', encoding='utf-8')
    # HtmlFile1 = open("/Users/pritam.mondal/Repos/automation/features2html/output_features2html/features_20220824_2049.html", 'r', encoding='utf-8')
    source_code1 = HtmlFile1.read()
    source_code2 = HtmlFile2.read()
    # components.html(source_code1, height=3000)
    components.html(source_code2, height=3000)

if choose == "Smoke":
    """
    Feature:OKR-LK Integration

        Scenario: Happy Flow
      
            Given Admin user logs into LK
            
            When  user navigates to OKR board
            
            Then Objective create button should be available
    
        Scenario: Negative Flow
          
            Given LK Admin user logs into LK
            
            When  user navigates to OKR board
            
            Then Objective create button should be available
        """