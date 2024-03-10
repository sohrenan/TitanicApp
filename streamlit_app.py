import streamlit as st
import requests
from PIL import Image
import pickle



with open('TitanicApp/log.sav', 'rb') as file:
    log_model = pickle.load(file)

image = Image.open('TitanicApp/leo.jpg')

def main():
    st.image(image, width=800)  # Display the image as a small icon
    st.title('Você sobreviveria ao titanic?')

    # Centered column for input forms
    with st.form(key='prediction_form'):
        st.header('Envie suas informações')
        age = st.number_input('Idade', min_value=0, max_value=100, value=25)
        fare = st.number_input('Quanto pagaria numa passagem?', min_value=0.0, value=100.0)
        ##gender_options = ['masculino', 'feminino', 'binario']
        ##gender = st.selectbox('Gênero', gender_options)
        predict_button = st.form_submit_button('Prever')

    # Predict when the button is clicked
    if predict_button:
        prediction_result = predict_survival(age, fare)
        if prediction_result == 'Você sobreviveria! Parabéns':
            st.write('**resultado:**', f'<span style="font-size:50px; color:blue">{prediction_result}</span>', unsafe_allow_html=True)
        if prediction_result == 'Você iria de Americanas!!':
            st.write('**resultado:**', f'<span style="font-size:50px; color:red">{prediction_result}</span>',
                     unsafe_allow_html=True)

def predict_survival(age, fare):
    # Make a request to your Flask API
    result = log_model.predict([[age,fare]])


    if result[0] == 1:
        mensagem = 'Você sobreviveria! Parabéns'
    if result[0] == 0:
        mensagem = 'Você iria de Americanas!!'
    return mensagem

if __name__ == '__main__':
    main()
