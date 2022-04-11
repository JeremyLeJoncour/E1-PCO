import streamlit as st
import cv2
import torch
from matplotlib import pyplot as plt
import numpy as np
import os
import tensorflow as tf

import streamlit as st
import cv2
import torch

def get_cap(value:str)->None:
    """
    Create a cv2.VideoCapture object kept in cache to give streamlit the ability to call the release function"""
    if 'capture' in st.session_state.keys():
        st.session_state['capture'].release()
    st.session_state['capture'] = cv2.VideoCapture(value)



# Create a selectbox to get input type for videoCapture
selectbox = st.selectbox("Select an input video:",["Camera","Youtube","Upload a file"])
if selectbox == "Youtube":
    st.text(' Test url : https://www.youtube.com/watch?v=oJ1sAD7IoNs')
    input = st.text_input('Inserez une URL Youtube')

if selectbox == 'Upload a file':
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        with open(os.path.join("fileDir",uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
    file_availables_list = []
    for filepath in os.listdir("fileDir"):
        file_availables_list.append(filepath)
    if len(file_availables_list) >= 1:
        file_selector  = st.selectbox('Choose an already existing file',file_availables_list)

# Create columns for start:stop buttons
col1,col2,col3 = st.columns(3)
with col1:
    start_button = st.button("Start inference",key='start_button')
with col2:
    stop_button = st.button("Stop inference",key='stop_button')



# Init placeholders to display video and read plates data
stframe = st.empty()


# Start inference for choosen stream
if start_button:
    torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

    if selectbox == "Camera":
        output = 0

    if selectbox == "Upload a file":
        output = "fileDir/" + file_selector

    get_cap(output)
    predictions = []

    while st.session_state['capture'].isOpened():
        ret, frame = st.session_state['capture'].read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        prediction =  model(image).pandas().xyxy[0].values
            

        if prediction is not None:
            for pred in prediction:

                x1 = int(pred[0])
                y1 = int(pred[1])
                x2 = int(pred[2])
                y2 = int(pred[3])

                start = (x1,y1)
                end = (x2,y2)

                name = pred[-1]
                color = (0,255,0)
            
                image = cv2.rectangle(image, start, end, color)
                image = cv2.putText(image, name, (x1,y1+25), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
                
                stframe.image(image)

        if stop_button:
            if 'capture' in st.session_state.keys():
                st.session_state['capture'].release() 