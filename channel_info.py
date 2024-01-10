#                                             Channel_Details
#-------------------------------------------------------------------------------------------------------------------------------
from conn import *


def channel_info(chan_id):
    request = YT.channels().list(
        part = "snippet,contentDetails,statistics",
        id = chan_id
    )
    res = request.execute()
    
    for item in res['items']:
        data = dict(
            Channel_Name = item['snippet']['title'],
            Channel_id = item['id'],
            Subscription_Count = item['statistics']['subscriberCount'],
            Channel_Views = item['statistics']['viewCount'],
            Channel_Description = item["snippet"]["description"],
            Video_Count = item['statistics']['videoCount'])
        
    return data


