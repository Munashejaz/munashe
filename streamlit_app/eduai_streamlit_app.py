import streamlit as st

def main():
    st.set_page_config(page_title="EDUAI Learning", page_icon="🎓", layout="wide")
    
    # Header
    st.title("Learn Smarter, Achieve Greater with AI")
    st.subheader("Welcome to EDUAI Learning – Your AI-powered Educational Hub")
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Toddler & Preprimary", "Primary & Secondary", 
                                       "Exam Papers & Revision", "Educators Empowerment", 
                                       "Parents & Stakeholders", "Multimedia & Publications"])
    
    # Homepage Content
    if page == "Home":
        st.markdown("""
        ### Why Choose EDUAI Learning?
        ✅ AI-powered education for all levels  
        ✅ Interactive learning tools for students  
        ✅ Exam preparation with past papers & solutions  
        ✅ Support for parents & educators  
        """)
    
        st.markdown("---")
        st.subheader("🔍 Explore EDUAI Learning")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📚 Exam Papers & Revision Guide")
        with col2:
            st.button("🎓 Educators Empowerment")
        with col3:
            st.button("👪 Parents & Stakeholders")

if __name__ == "__main__":
    main() 
