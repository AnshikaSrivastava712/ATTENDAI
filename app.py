import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='ATTENDAI - Making Attendance faster using AI',
        page_icon="logo.jpg"   # Ensure logo.jpg exists or replace with an emoji like "🎯"
    )
    
    # ========== GLOBAL STYLING: DARK BLUE BACKGROUND + INTER FONT ==========
    st.markdown("""
        <style>
        /* Import Google Fonts - Inter */
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700&display=swap');
        
        /* Dark blue backgrounds */
        [data-testid="stAppViewContainer"] {
            background-color: #0a192f;
        }
        [data-testid="stSidebar"] {
            background-color: #0a1a2f;
        }
        [data-testid="stHeader"] {
            background-color: #0a192f;
        }
        
        /* Apply font and text color globally */
        * {
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            color: #e0e3ff !important;
        }
        
        /* Buttons */
        .stButton button {
            background-color: #5865f2;
            color: white !important;
            font-weight: 500;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        .stButton button:hover {
            background-color: #4752c4;
            transform: translateY(-1px);
        }
        
        /* Input fields */
        .stTextInput input, .stTextArea textarea, .stSelectbox select, .stMultiSelect div {
            background-color: #1e2a3a;
            color: #e0e3ff !important;
            border-radius: 6px;
            border: 1px solid #2d3e5a;
        }
        
        /* Dropdown menus */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #1e2a3a;
        }
        
        /* DataFrames / Tables */
        .stDataFrame, .stTable {
            background-color: #0f2138;
            color: #e0e3ff;
        }
        </style>
    """, unsafe_allow_html=True)
    # =========================================================================
    
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

if __name__ == "__main__":
    main()