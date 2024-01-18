#Displaying All the content in Streamlit 


from streamlit_option_menu import option_menu
import streamlit as st
from insertion import *
from table_view import *
from Query import *
from anim import *

st.set_page_config( layout='wide')

with st.sidebar:
    opp = option_menu(
        menu_title=None,options=["INTRO","SCRAP","TABLE VIEW","INSERTION","QUERY"],
        default_index=0,menu_icon=None,icons=["text","text","text","text","text"],
    )

if opp == "INTRO":
    st.title(":red[YouTube Data Harvesting And Were Housing ]")
    st.title(":red[Using Mongo_DB And SQL]")
    st.header(" ",divider='rainbow')
    
    st.subheader(":rainbow[This application harvests data from YouTube using the YouTube API.]")
    st.subheader(":rainbow[Stores it in a MongoDB data lake,migrates it to a SQL data warehouse.]")
    st.subheader(":rainbow[Allows querying the data warehouse.]")
    lt(load, height=400)

elif opp == "SCRAP":
    ch_id = st.text_input(label="Enter Channel ID",placeholder="Channel Id")
    if ch_id and st.button("Extract Data"):
        try:
            Ch_det = channel_info(ch_id)
            Vid_id = get_vid_id(ch_id)
            Vid_det = Vid_info(Vid_id)
            Comm_det = Comm_info(Vid_id)
            st.write({
                    "Channel_Detail":Ch_det,
                    "Video_Detail":Vid_det,
                    "Comment_Detail":Comm_det})
            st.success("Data Extracted Succesfully")
            
        except KeyError:
            st.text("Invalid Channel Id\nPlease Enter Correct Channel Id")
    
elif opp == "TABLE VIEW":
    st.write(table_vi())

elif opp == "INSERTION":
    st.write(data_insertion())

elif opp == "QUERY":
    st.write(Qa())

