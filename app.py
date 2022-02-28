import pandas as pd

import streamlit as st
import requests

from react_table import selectable_data_table
import extra_streamlit_components as stx


from streamlit.server.server import Server
from streamlit.script_run_context import get_script_run_ctx


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
response = requests.get('https://discuss.streamlit.io/')
session_cookies = response.cookies
cookies_dictionary = session_cookies.get_dict()

st.write(response.cookies)
st.write(cookies_dictionary)

# streamlit server
st.title('Streamlit Server')
current_session = Server.get_current()
ctx = get_script_run_ctx()
st.write(current_session)
st.write('ctx is: ')
st.write(ctx)
st.write('session_id is:', ctx.session_id)
st.write('session_id is:', ctx.session_state)
