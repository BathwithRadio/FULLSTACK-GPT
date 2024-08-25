import streamlit as st # when data changed, whole python file will restart

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🤖",
)

st.title("FullstackGPT Home")

st.markdown(
        """
# Hello!
            
Welcome to my FullstackGPT Portfolio!
            
Here are the apps I made:
            
- [x] [DocumentGPT](/DocumentGPT)
- [ ] [PrivateGPT](/PrivateGPT)
- [ ] [QuizGPT](/QuizGPT)
- [ ] [SiteGPT](/SiteGPT)
- [ ] [MeetingGPT](/MeetingGPT)
- [ ] [InvestorGPT](/InvestorGPT)
"""
)