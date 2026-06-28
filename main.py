if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        st.write(f"Tu IMC es: {imc:.2f}")
        if imc < 18.5:
            st.write("Estado: Bajo peso")
        elif imc < 25:
            st.write("Estado: Peso normal")
        else:
            st.write("Estado: Sobrepeso o más")
    else:
        st.error("Por favor, ingresa valores mayores a cero.")
