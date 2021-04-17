import streamlit as st

from utils.regex_tester import test_url_regex_pattern




url_input = st.text_input(label='Input URL')

if st.button('Submit URL'):
    match_result = test_url_regex_pattern(url_input)
    if match_result is None:
        st.warning("Your input is not URL. Please submit again.")
    else:
        st.markdown("**Your submission:**")
        st.markdown(match_result)
 