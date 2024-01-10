#                     Channel Table Creation 
#----------------------------------------------------------------------------------
import psycopg2 as ps
import pandas as pd
from conn_mongo import *

def channel_table():
    mydb = ps.connect(
        host = "localhost",
        user = "postgres",
        password = "root3",
        database = "Youtube_Data",
        port = "5432"
    )
    
    curs = mydb.cursor()
    
    drop = '''drop table if exists channels'''
    curs.execute(drop)
    mydb.commit()

    try:
        query = '''Create table if not Exists Channels(Channel_Name varchar(100),
                                                Channel_id varchar(100) primary key,
                                                Subscription_Count bigint,
                                                Channel_Views bigint,
                                                Video_Count int,
                                                Channel_Description text)'''
        curs.execute(query)
        mydb.commit()
    except:
        print("Channel Table Already Created")

    ch_list = []
    db = mongo["YT_Data"]
    coll = db["channel_detail"]

    for ch_dat in coll.find({},{"_id":0, "Channel_information":1}):
        ch_list.append(ch_dat["Channel_information"])
    df = pd.DataFrame(ch_list)


    for index,row in df.iterrows():
        query1 = '''insert into channels(
                    Channel_Name,
                    Channel_id,
                    Subscription_Count,
                    Channel_Views,
                    Video_Count,
                    Channel_Description)
                    
                    values(%s,%s,%s,%s,%s,%s)'''
        
        values = (row['Channel_Name'],
                row["Channel_id"],
                row["Subscription_Count"],
                row["Channel_Views"],
                row["Video_Count"],
                row["Channel_Description"])
        
        try:
            curs.execute(query1,values)
            mydb.commit()
        except:
            print("Channels Details Already Inserted")
        
