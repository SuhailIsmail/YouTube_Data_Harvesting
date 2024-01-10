import streamlit as st

from conn_mongo import *
from detail_insert import *
from Table_creation import *
from stream_table import *

def table_vi():
    show_table = st.radio("SELECT TABLE" ,("CHANNELS","VIDEOS","COMMENTS"))

    if show_table == "CHANNELS":
        stream_channel()
    elif show_table == "VIDEOS":
        stream_video()
    elif show_table == "COMMENTS":
        stream_comm()
    

