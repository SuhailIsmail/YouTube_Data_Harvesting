from googleapiclient.discovery import build
from pprint import pprint
import psycopg2 as ps
import pymongo
import pandas as pd
import streamlit as st

#                   creatin Api_Connection
#-----------------------------------------------------------------
def Api_conn():
    Api_key = 'AIzaSyBIxZEhKouMqkqUH51MboAm_qFJj3CNcug'
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=Api_key)
    return youtube

YT = Api_conn()


