#                               Video Table Creation 
#----------------------------------------------------------------------------------
from channel_table import *

def Videos_table():
    mydb = ps.connect(
        host = "localhost",
        user = "postgres",
        password = "root3",
        database = "Youtube_Data",
        port = "5432"
    )
    curs = mydb.cursor()

    drop = '''drop table if exists videos'''
    curs.execute(drop)
    mydb.commit()

    query = '''Create table if not Exists videos(
                    Channel_Name varchar(100),
                    Channel_Id varchar(100),
                    Video_Id varchar(30) primary key,
                    Video_Name varchar(200),
                    Video_Description text,
                    Published_Date timestamp,
                    View_Count bigint,
                    Like_Count bigint,
                    Favorite_Count int,
                    Comment_Count int,
                    Tags text,
                    Video_Duration interval,
                    Thumnail varchar(200),
                    Caption_Status varchar(50))'''

    curs.execute(query)
    mydb.commit()

    vid_list = []
    db = mongo["YT_Data"]
    coll = db["channel_detail"]
    for vid_dat in coll.find({},{"_id":0, "Video_Information":1}):
        for i in range(len(vid_dat["Video_Information"])):
            vid_list.append(vid_dat["Video_Information"][i])
    df2 = pd.DataFrame(vid_list)




    for index,row in df2.iterrows():
            query = '''insert into videos(
                                            Channel_Name,
                                            Channel_Id,
                                            Video_Id,
                                            Video_Name,
                                            Video_Description,
                                            Published_Date,
                                            View_Count,
                                            Like_Count,
                                            Favorite_Count,
                                            Comment_Count,
                                            Tags,
                                            Video_Duration,
                                            Thumnail,
                                            Caption_Status
                                        )

                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

            values = (row['Channel_Name'],
                    row['Channel_Id'],
                    row['Video_Id'],
                    row['Video_Name'],
                    row['Video_Description'],
                    row['Published_Date'],
                    row['View_Count'],
                    row['Like_Count'],
                    row['Favorite_Count'],
                    row['Comment_Count'],
                    row['Tags'],
                    row['Video_Duration'],
                    row['Thumnail'],
                    row['Caption_Status'])
            
            curs.execute(query,values)
            mydb.commit()

