import streamlit as st

st.title("Resource Technical Evaluation")

st.title(":blue[_Resource Technical Evaluation_] :speech_balloon:")

st.title("E = mc^2")
st.title("$E = mc^2$")




# st.write automatic detect content format and render it nicely
#List , dict , dataframe, palin text, or plot

data = {'Luanda' , 'City'}
st.write(data)

# Buttons

clicked = st.button("click me")

#Text Input

name = st.text_input("First name")

#Check Boxese

slect=st.checkbox("I agree")

# Markdown
st.markdown("#This is text bold# **This is italic \n- this text is in new line**")

#Feedback
st.feedback("starts") 
st.multiselect('basic','avarge' 'expert')
st.radio("pick one" , [yes,no, no-answer])
