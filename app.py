import pandas as pd

import streamlit as st
import requests

from react_table import selectable_data_table
import extra_streamlit_components as stx


@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()


cookie_manager = get_manager()


data = [
  { "id": 1, "lastName": 'Snow', "firstName": 'Jon', "age": 35 },
  { "id": 2, "lastName": 'Lannister', "firstName": 'Cersei', "age": 42 },
  { "id": 3, "lastName": 'Lannister', "firstName": 'Jaime', "age": 45 },
  { "id": 4, "lastName": 'Snow', "firstName": 'Jon', "age": 35 },
  { "id": 5, "lastName": 'Lannister', "firstName": 'Cersei', "age": 42 },
  { "id": 6, "lastName": 'Lannister', "firstName": 'Jaime', "age": 45 },

];

#df = pd.DataFrame(raw_data, columns=["First Name", "Last Name", "Age"])

#st.write(df)

st.title("The is the beginning of my table")

rows = selectable_data_table(data)
if rows:
    st.write("You have selected", rows)

st.write("here is the end")

st.subheader("All Cookies:")
cookies = cookie_manager.get_all()
st.write(cookies)


# session_state
st.title('Session cookies')
a_session = requests.get('https://share.streamlit.io/francesfeng/react_table_component/main/app.py')
session_cookies = a_session.cookies
cookies_dictionary = session_cookies.get_dict()

st.write(session_cookies)
st.write(cookies_dictionary)
