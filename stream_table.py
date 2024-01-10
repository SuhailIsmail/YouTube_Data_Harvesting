from detail_insert import *
import streamlit as st

#Converting data to dataframe

def stream_channel():
    ch_list = []
    db = mongo["YT_Data"]
    coll = db["channel_detail"]

    for ch_dat in coll.find({},{"_id":0, "Channel_information":1}):
        ch_list.append(ch_dat["Channel_information"])
    df = st.dataframe(ch_list)

    return df

def stream_video():
    vid_list = []
    db = mongo["YT_Data"]
    coll = db["channel_detail"]
    for vid_dat in coll.find({},{"_id":0, "Video_Information":1}):
        for i in range(len(vid_dat["Video_Information"])):
            vid_list.append(vid_dat["Video_Information"][i])
    df2 = st.dataframe(vid_list)

    return df2

def stream_comm():
    comm_list = []
    db = mongo["YT_Data"]
    coll = db["channel_detail"]
    for comm_dat in coll.find({},{"_id":0, "Comment_information":1}):
        for i in range(len(comm_dat["Comment_information"])):
            comm_list.append(comm_dat["Comment_information"][i])
    df2 = st.dataframe(comm_list)

    return df2