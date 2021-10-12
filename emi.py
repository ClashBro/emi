import streamlit as st
def calculate_emi(p,n,r):
	emi = p * (r/100) * ((1+(r/100))**n / ((1+(r/100))**n-1))
	return emi
st.title('Emi Calculation')
p = st.slider('Principal',1000,1000000,step = 1000)
n = st.slider('Tenure',1,30)
n = n*12
r = st.slider('ROI',1.00,15.00,step=0.05)
r = r/12
if st.button('Calculate') == True:
	st.write('EMI is ',calculate_emi(p,n,r))