#                 Detail insertion to Mongodb
#---------------------------------------------------------------------------

from conn_mongo import *
from channel_info import *
from Video_info import *
from Video_ids import *
from Comm_info import *



def channel_detail(chan_id):
    chan_det = channel_info(chan_id)
    vid_id = get_vid_id(chan_id)
    vids_det = Vid_info(vid_id)
    comment_det = Comm_info(vid_id)

    collec1 = db["channel_detail"]
    collec1.insert_one({"Channel_information":chan_det,"Video_Information":vids_det,
                        "Comment_information":comment_det})
    
    return "Migrate Completed"

