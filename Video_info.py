#                                    video_Details
#-------------------------------------------------------------------------------------------------------------------------------
from Video_ids import *


def Vid_info(video_ids):
    vid_data = []
    for id in video_ids:
        request = YT.videos().list(
            part="snippet,ContentDetails,statistics", id = id)
        resp1 = request.execute()

        for i in resp1["items"]:
            data1 = dict(
                Channel_Name = i['snippet']['channelTitle'],
                Channel_Id = i['snippet']['channelId'],
                Video_Id = i["id"],
                Video_Name = i["snippet"]["title"],
                Video_Description = i["snippet"].get("description"),
                Published_Date = i["snippet"]["publishedAt"],
                View_Count = int(i["statistics"].get("viewCount",0)),
                Like_Count = int(i["statistics"].get("likeCount",0)),
                Favorite_Count = int(i["statistics"].get("favoriteCount")),
                Comment_Count  = i["statistics"].get("commentCount"),
                Tags = i["snippet"].get("tags"),
                Video_Duration = i["contentDetails"]["duration"],
                Thumnail = i['snippet']['thumbnails']['default']['url'],
                Caption_Status = i['contentDetails']['caption']
                )
            vid_data.append(data1)
    return vid_data

     

     