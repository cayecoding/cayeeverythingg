import streamlit as st

#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Caye Guadalou L. Ruaya :wave:")
    st.title("The Journey Of My Life")
    st.write("Life As an Engineering Student, Let's go!")
    st.write("{Curious About My Life or Who Am I?, Check it out my FB Acc}(https://www.facebook.com/eyacc31/)")

# ---- Life Background ----
with st.container():
    st.write("---") 
    left column, right column = st.columns(2)
    with left_column:
      st.header("Life Background")
      st.write("##")
      st.write(
        """
        A Short Background About My Self:
        - 19 yrs old
        - Born in Toledo,Cebu City
        - I Live in Dapa, Siargao Island but currently I am here in Surigao City for School.
        - I am a 1st yr College Student here in Surigao Del Norte State University.
        - Taking a course of Bachelor Science in Computer Engineering.

)
