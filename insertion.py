import streamlit as st
from conn_mongo import *
from detail_insert import *
from Table_creation import *
from stream_table import *

def data_insertion():
    chan_id = st.text_input(label="Enter the Channel id", placeholder="Channel-Id-here")   
    try:
        if chan_id and st.button("Store to db"):
            ch_ids = []
            coll = db['channel_detail']
            for ch_data in coll.find({},{"_id":0,"Channel_information":1}):
                ch_ids.append(ch_data["Channel_information"]["Channel_id"])
            
            if chan_id in ch_ids:
                st.success("Channel id already exists")

            else:
                insert = channel_detail(chan_id)
                st.success("Channel Detail Inserted to Mongo D")

        if chan_id and st.button("Migrate to sql"):
            Table = tables()
            st.success(Table)

    except KeyError :
        st.subheader("Invalid Channel Id\nPlease Enter Correct Channel Id")


