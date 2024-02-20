import streamlit as st
import numpy as np
import matplotlib.pylab as plt

st.title('Simulation[tm]')
st.write("Here is our super important simulation.")

x = st.sidebar.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
y = st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

arr = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)
for i in range(arr.shape[1]):
    plt.plot(arr[:, i])

st.pyplot()