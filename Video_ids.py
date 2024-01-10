#                            To get Video Ids
#--------------------------------------------------------------------------------------------------------

from channel_info import *


def get_vid_id(chan_id):
    vid_id = []
    req = YT.channels().list(
            part = "contentDetails", id = chan_id).execute()
    ply_id = req["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    token = None

    while True:
        req1 = YT.playlistItems().list(
            part="snippet",
            playlistId = ply_id,
            pageToken=token).execute()

        for item in range(len(req1["items"])):
            vid_id.append(req1["items"][item]["snippet"]["resourceId"]["videoId"])
        token = req1.get('nextPageToken')

        if token is None:
            break
    return vid_id


