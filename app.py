import streamlit as st
from src.funcs import *

st.title("HTML minification")
space(2)

# Init lists
dimensions = []
path_to_html = []
path_to_images = []
titles = []
descriptions = []

st.markdown("## Inputs")
number_of_charts = st.number_input("Number of charts", min_value=1, max_value=10, value=1, step=1)
space(2)
for i in range(number_of_charts):

    st.markdown(f"### Chart {i + 1}")
    alls = one_chart(dimensions, path_to_html, path_to_images,titles, descriptions, i, number_of_charts)
    dimensions, path_to_html, path_to_images, titles, descriptions = alls
    space(2)

st.markdown("## Outputs")
html_output = html_minify(dimensions, path_to_html, path_to_images, titles, descriptions)
st.code(html_output)
