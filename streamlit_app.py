import streamlit as st

st.write('Hola Monino')
st.write('Te quiero mucho')
st.write('Hola Monono..!!')

st.button('Presionar por besinos!!!')
#st.data_editor('Edit data', data)
#st.checkbox('Check me out')
st.write('Selecciona que quieres..!!')
st.radio('Pick one:', ['Besino','Postrecino','Abrazino'])
st.selectbox('Select', ['Normal','Navideño','Cumpleañero'])
#st.multiselect('Multiselect', [1,2,3])
st.write('Selecciona la cantidad')
st.slider('?Cual es tu edad?', min_value=18, max_value=99)
st.select_slider('Slide to select', options=['1','2',3,'4'])
st.text_input('Introduce algun texto')
st.number_input('Escribe un numero')
st.text_area('Solicitudes especiales')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('Cargar un archivo')
#st.download_button('On the dl', data)

# Use widgets' returned values in variables
for i in range(int(st.number_input('Num:'))): foo()
if st.sidebar.selectbox('I:',['f']) == 'f': b()
my_slider_val = st.slider('Quinn Mallory', 1, 88)
st.write(slider_val)

