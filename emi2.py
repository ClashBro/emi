import streamlit as st
def calculate_emi(p,n,r):
	emi = p * (r/100) * ((1+(r/100))**n / ((1+(r/100))**n-1))
	return emi
def calculate_outstanding_balance(p,n,r,m):
	balance = (p*((1+(r/100))**n) -(1+(r/100))**m)/(((1+(r/100))**n)-1)
	return balance
st.title('Emi Calculation')
p = st.slider('Principal',1000,1000000,step = 1000)
n = st.slider('Tenure',1,30)
n = n*12
r = st.slider('ROI',1.00,15.00,step=0.05)
r = r/12
m = st.slider('Period after which OLB is calculated',1,n)
if st.button('Calculate EMI') == True:
	st.write('EMI is ',calculate_emi(p,n,r))
if st.button('Calculate OLB') == True:
	st.write('OLB is ',calculate_outstanding_balance(p,n,r,m))