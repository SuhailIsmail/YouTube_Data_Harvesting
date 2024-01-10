#                              Comment_Info
#-----------------------------------------------------------------------------
from Video_ids import *


def Comm_info(video_ids):
    Comm_data=[]
    try:   
        for ids in video_ids:
            request = YT.commentThreads().list(
                part="snippet",
                videoId=ids,
                maxResults = 99
            )
            response = request.execute()

            for item in response["items"]:
                data = dict(
                    Comment_Id = item["snippet"]["topLevelComment"]["id"],
                    Video_Id = item["snippet"]["topLevelComment"]["snippet"]["videoId"],        
                    Comment_Text = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                    Comment_Author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                    Comment_Published = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
                )
                Comm_data.append(data)

    except:
        pass
    
    return Comm_data

