# app.py
import streamlit as st
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.config import PAGES
from utils.styling import load_css
from components.sidebar import render_sidebar

from pages.sistem_nlp import render_sistem_nlp
from pages.info import render_info

# Page config
st.set_page_config(
    page_title="Learning Insight | PT PLN (Persero) UPDL Surabaya",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="⚡"
)

# Load CSS
load_css()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = PAGES["Sistem NLP"]

st.markdown("""
<script>
    // Function to remove default sidebar items
    function removeDefaultSidebar() {
        // Remove default navigation items
        const sidebarNav = document.querySelector('[data-testid="stSidebarNav"]');
        if (sidebarNav) {
            sidebarNav.style.display = 'none';
        }
        
        // Remove any list items that might be default menu
        const lists = document.querySelectorAll('section[data-testid="stSidebar"] ul');
        lists.forEach(list => {
            if (list.children.length > 0 && list.children[0].textContent.includes('app')) {
                list.style.display = 'none';
            }
        });
    }
    
    // Run on page load
    removeDefaultSidebar();
    
    // Run after any DOM changes
    const observer = new MutationObserver(removeDefaultSidebar);
    observer.observe(document.body, { childList: true, subtree: true });
</script>
""", unsafe_allow_html=True)

render_sidebar()

if st.session_state.page == PAGES["Sistem NLP"]:
    render_sistem_nlp()
elif st.session_state.page == PAGES["Info"]:
    render_info()
