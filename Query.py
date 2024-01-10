import streamlit as st
from conn_mongo import *
import psycopg2 as ps
import pandas as pd

def Qa():
    mydb = ps.connect(
        host = "localhost",
        user = "postgres",
        password = "root3",
        database = "Youtube_Data",
        port = "5432"
    )
    curs = mydb.cursor()

    ques = st.selectbox("Select",(
                    "1. What are the names of all the videos and their corresponding channels",
                    "2. Which channels have the most number of videos, and how many videos do they have",
                    "3. What are the top 10 most viewed videos and their respective channels",
                    "4. How many comments were made on each video, and what are their corresponding video names",
                    "5. Which videos have the highest number of likes, and what are their corresponding channel names",
                    "6. What is the total number of likes for each video, and what are their corresponding video names",
                    "7. What is the total number of views for each channel, and what are their corresponding channel names",
                    "8. What are the names of all the channels that have published videos in the year 2022",
                    "9. What is the average duration of all videos in each channel, and what are their corresponding channel names",
                    "10. Which videos have the highest number of comments, and what are their corresponding channel names"
                                ))

    if ques == "1. What are the names of all the videos and their corresponding channels":
        q1 = '''select video_name as videos,channel_name as channel_name from videos'''
        curs.execute(q1)
        mydb.commit()
        t = curs.fetchall()
        df = pd.DataFrame(t,columns=['Channel_Name','Videos_Name'])
        st.write(df)


    elif ques == "2. Which channels have the most number of videos, and how many videos do they have":
        q2 = '''select channel_name as channelname,Video_count as No_videos  from channels
                order by Video_count DESC'''
        curs.execute(q2)
        mydb.commit()
        t = curs.fetchall()
        df = pd.DataFrame(t,columns=['Channel_Name','Video_Count'])
        st.write(df)


    elif ques == "3. What are the top 10 most viewed videos and their respective channels":
        q3 = '''select video_name,view_count,channel_name from videos order by view_count desc limit 10'''
        curs.execute(q3)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Video_Name','View_Count','Channel_Name',])
        st.write(df)

    elif ques == "4. How many comments were made on each video, and what are their corresponding video names":
        q4 = '''select video_name,comment_count from videos where comment_count is not null'''
        curs.execute(q4)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Video_Name','Comment_Count',])
        st.write(df)


    elif ques == "5. Which videos have the highest number of likes, and what are their corresponding channel names":
        q5 = '''select channel_name, like_count from videos where like_count is not null order by like_count desc '''
        curs.execute(q5)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Channel_Names','Likes'])
        st.write(df)
        
    elif ques == "6. What is the total number of likes for each video, and what are their corresponding video names":
        q6 = '''select video_name,like_count from videos'''
        curs.execute(q6)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Video_Name','Likes'])
        st.write(df)


    elif ques == "7. What is the total number of views for each channel, and what are their corresponding channel names":
        q7 = '''select channel_name,channel_views from channels'''
        curs.execute(q7)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Channel_Names','Views'])
        st.write(df)


    elif ques == "8. What are the names of all the channels that have published videos in the year 2022":
        q8 = '''select distinct channel_name from videos
            WHERE  EXTRACT (YEAR FROM published_date) = 2022  '''
        curs.execute(q8)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Channel_Names'])
        st.write(df)


    elif ques == "9. What is the average duration of all videos in each channel, and what are their corresponding channel names":
        q9 = '''select channel_name, AVG(video_duration) from videos group by channel_name '''
        curs.execute(q9)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Channel_Names','Average_Duration'])
        st.write(df)


    elif ques == "10. Which videos have the highest number of comments, and what are their corresponding channel names":
        q10 = '''select video_name,comment_count,channel_name from videos 
            where comment_count is not null order by comment_count desc'''
        curs.execute(q10)
        mydb.commit()
        t1 = curs.fetchall()
        df = pd.DataFrame(t1,columns=['Video_Name','Comment_count','Channel_Name'])
        st.write(df)

