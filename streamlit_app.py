import streamlit as st

st.write('Hola Monino')
st.write('Te quiero mucho')
st.write('Hola Monono..!!')

st.button('Presionar por besinos!!!')
#st.data_editor('Edit data', data)
#st.checkbox('Check me out')
st.write('Selecciona que quieres..!!')
st.radio('Pick one:', ['Besino','Postrecino','Abrazino'])
st.selectbox('Select', [Normal,Navideño,Cumpleañero])
#st.multiselect('Multiselect', [1,2,3])
st.write('Selecciona la cantidad')
st.slider('Slide me', min_value=0, max_value=50)
st.select_slider('Slide to select', options=['1','2',3,'4'])
st.text_input('Introduce algun texto')
st.number_input('Escribe un numero')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('Cargar un archivo')
#st.download_button('On the dl', data)
