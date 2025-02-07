import streamlit as st
from PIL import Image
import webbrowser
st.markdown(
    """
    <style>
    st.App{
        background-color: white; /* Light grayish-blue */
    }
    </style>"""
    ,
    unsafe_allow_html=True
)
st.title("PORTFOLIO")
st.text("(SY Btech Student at MITAOE)")
cuisine = st.sidebar.selectbox("Select to see" , ("About","Education" , "Skills" , "Projects"))
if(cuisine=='About'):
    st.text("NAME : TANMAY DATTATRAY FALKE\nCOLLEGE : MIT ACADEMY OF ENGINEERING , ALANDI\nBRANCH : COMPUTER ENGINEERING\nYEAR : SECOND YEAR")
    image = st.image('WhatsApp Image 2024-12-24 at 14.04.02_5070bca6.jpg' , width=200)
   
elif(cuisine=='Education'):
    st.text("\n\nFY CGPA : 8.2\n\n12th PERCENTAGE : 73.50%\n\nJEE MAINS PERCENTILE : 86.7\n\nMHT-CET PERCENTILE : 95.85")
elif(cuisine=='Skills'):
    st.text("PYTHON (pandas , numpy , matplotlib , streamlit , scikitlearn , langchain)\n\nC++(DSA)\n\nC\n\nHTML,CSS,JS")  
    b = st.link_button('codechef profile' , url='https://www.codechef.com/users/tanmayfalke29')  
    c = st.link_button('leetcode profile' , url='https://leetcode.com/u/tanmayfalke29/')
elif(cuisine=='Projects'):
    img = st.image('download (2).png', width=50)
    aa = st.link_button('github profile' , url='https://github.com/tanmayfalke7')