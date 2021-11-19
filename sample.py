import streamlit as st
import pandas as pd
#import cv2

st.write('Hello World')
st.header('Jenny First Webapp')

st.image('media/dog-beach-lifesaver.png')

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')

#tao menu
menu = ['Home', 'About me', 'Read Data','Camera']
choice = st.sidebar.selectbox('Menu list', menu)

if choice == 'Home':
    st.video('https://www.youtube.com/watch?v=ioNng23DkIM')

    col1, col2 = st.columns(2)
    with col1:
        idol_name = st.text_input('What is your idol name?')
        st.write('My idol name:', idol_name)

    with col2:
        age = st.slider('My idol age', min_value=0, max_value=30)
        st.write('My idol age:', age)


elif choice == 'Read Data':
    df = pd.read_csv('media/AB_NYC_2019.csv')
    st.dataframe(df)

elif choice == 'About me':
    st.audio('media/Impact_Moderato.mp3')
    fileUp = st.file_uploader('File uploader',type = ['jpg','png','jpeg'])
    st.image(fileUp)
    # model.predict(fileUp) để hiện phần prediction

elif choice == 'Camera':
    cap = cv2.VideoCapture(0)  # device 0
    run = st.checkbox('Show Webcam')
    capture_button = st.checkbox('Capture')

    captured_image = np.array(None)


    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    FRAME_WINDOW = st.image([])
    while run:
        ret, frame = cap.read()        
        # Display Webcam
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB ) #Convert color
        FRAME_WINDOW.image(frame)

        if capture_button:      
            captured_image = frame
            break

    cap.release()