import streamlit as st
import json
from streamlit_lottie import st_lottie as lt 

Lot_anim = "youtube.json"

def load_anim(file_path):
    with open (file_path,"r") as f:
        return json.load(f)

load = load_anim(Lot_anim)
