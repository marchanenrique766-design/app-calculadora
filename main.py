import streamlit as st

st.title("App de Salud y Bienestar")
peso = st.number_input("Ingresa tu peso en kg")
altura = st.number_input("Ingresa tu altura en metros (ej: 1.75)")

if st.button("Calcular IMC"):
    imc = peso / (altura ** 2)
    st.write(f"Tu IMC es: {imc:.2f}")
