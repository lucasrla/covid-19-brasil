# https://github.com/streamlit/streamlit/issues/513
# https://github.com/asg017/streamlit-observable
# https://github.com/asg017/streamlit-observable-showcase

import streamlit as st
from streamlit_observable import observable

st.title("Observables on Streamlit")

st.markdown(
    "Please wait while the notebooks load. They are data heavy and this process may take a while."
)

# https://github.com/asg017/streamlit-observable#api-reference
observable(
    "COVID-19 Brasil por Estado (UF)",
    notebook="@lucasrla/covid-19-casos-e-mortes-no-brasil",
    targets=["chart"],
)

observable(
    "COVID-19 Brasil por Cidade",
    notebook="@lucasrla/covid-19-brasil-por-cidade",
    targets=["chart"],
)

st.markdown("---")

st.markdown(
    "Powered by Streamlit and [@asg017/streamlit-observable](https://github.com/asg017/streamlit-observable)."
)
