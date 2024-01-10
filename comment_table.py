#                               Comments Table Creation 
#----------------------------------------------------------------------------------
from vid_table import *

def Comments_table():
    mydb = ps.connect(
        host = "localhost",
        user = "postgres",
        password = "root3",
        database = "Youtube_Data",
        port = "5432"
    )
    curs = mydb.cursor()

    drop = '''drop table if exists comments'''
    curs.execute(drop)
    mydb.commit()

    query = '''Create table if not Exists comments(
                            Comment_Id varchar(100) primary key,
                            Video_Id varchar(50),        
                            Comment_Text text,
                            Comment_Author varchar(150),
                            Comment_Published timestamp
                        )'''

    curs.execute(query)
    mydb.commit()

    comm_list = []
    db = mongo["YT_Data"]
    coll = db["channel_detail"]
    for comm_dat in coll.find({},{"_id":0, "Comment_information":1}):
        for i in range(len(comm_dat["Comment_information"])):
            comm_list.append(comm_dat["Comment_information"][i])
    df2 = pd.DataFrame(comm_list)


    for index,row in df2.iterrows():
            query = '''insert into comments(
                                    Comment_Id,
                                    Video_Id,        
                                    Comment_Text,
                                    Comment_Author,
                                    Comment_Published 
                                    )
                            
                                    values(%s,%s,%s,%s,%s)'''


            values = (row['Comment_Id'],
                    row['Video_Id'],
                    row['Comment_Text'],
                    row['Comment_Author'],
                    row['Comment_Published'])
            
            curs.execute(query,values)
            mydb.commit()
            
