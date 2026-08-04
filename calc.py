import os
import numpy #importing numpy for improving simple calculations
import math #importing math for improving simple calculations
import streamlit as st #importing streamlit for creating a simple UI
import re
from numpy.random import default_rng as rng
import matplotlib.pyplot as plt
import pandas as pd

#remember results+save  
if "past_calc" not in st.session_state:
    st.session_state.past_calc = []

if "remember_calc" not in st.session_state:
    st.session_state.remember_calc = ""

#tokenizing math calc part
def calculate(user_input):
    tokens = re.findall(r'-?\d+(?:\.\d+)?|[+\-*/^√π()]', user_input);
    do_math = "".join(tokens)
    do_math = do_math.replace(" ","")
    do_math = do_math.replace("^","**")
    do_math = do_math.replace("√", "**0.5")
    do_math = do_math.replace("π", "math.pi")

    result = eval(do_math)
    return result

#buttons

def pib():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "π" 
    
def rootb():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "√"

def expob():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "^"

def minusb():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "-"

def plusb():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "+"

def divideb():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "/"

def multiplyb():
    remember_input = st.session_state.get("remember_calc","")
    st.session_state.remember_calc = remember_input + "*"

#VISUAL PART

st.title("Calculator App")
st.text("Program recognises + - * / ^ √ π")

#columns
calc, buttons = st.columns([8, 1])

with calc:

    user_input = st.text_input("", placeholder="For now supporting easy calculations", key="remember_calc")
    calculating = st.button("Calculate")
    
    if calculating:
            try:
                result = calculate(user_input)
                st.success(f"{result}")
                st.session_state.past_calc.append(result)
            except:
                st.error(f"Something went wrong")

with buttons:
    
    row1, row2= st.columns([1,1])
    
    with row1:
        st.button(label="π", on_click=pib)
        st.button(label="√", on_click=rootb)
        st.button(label="^", on_click=expob)
    with row2:
        st.button(label="*", on_click=multiplyb)
        st.button(label="-", on_click=minusb)
        st.button(label="/", on_click=divideb)   


#graph and data

with st.sidebar:
    st.subheader("data")
    st.write(st.session_state.past_calc)

st.subheader("visual chart")

if st.session_state.past_calc:
    st.area_chart(st.session_state.past_calc)
else:
    st.text("Calculate to view data")


math_signs = st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =\sum_{k=0}^{n-1} ar^k =a \left(\frac{1-r^{n}}{1-r}\right)''')
st.text("In future adding more user friendly equation visualisation")
