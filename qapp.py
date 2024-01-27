import streamlit as st
import pandas as pd

# Definir los datos de los estudiantes
estudiantes = [
            {
                "apellido": "Adauto Huaman",
                "nombre": "Isaac",
                "correo": "isaac.adauto.h@uni.pe",
            },
            {
                "apellido": "Alvarado Osorio",
                "nombre": "Alexander Oliver",
                "correo": "alexander.alvarado.o@uni.pe",
            },
            {
                "apellido": "Alvarez Huaringa",
                "nombre": "Sandro Enrique",
                "correo": "sandro.alvarez.h@uni.pe",
            },
            {
                "apellido": "Andia Fernandez",
                "nombre": "Diego Paolo",
                "correo": "diego.andia.f@uni.pe",
            },
            {
                "apellido": "Aymachoque Aymachoque",
                "nombre": "Luis Jairo",
                "correo": "luis.aymachoque.a@uni.pe",
            },
            {
                "apellido": "Ballarta Ulloa",
                "nombre": "Natalia Paula",
                "correo": "natalia.ballarta.u@uni.pe",
            },
            {
                "apellido": "Bravo Olano",
                "nombre": "Randy Piero",
                "correo": "rbravo@uni.pe",
            },
            {
                "apellido": "Callupe Pardo",
                "nombre": "Yoselyn Patricia",
                "correo": "yoselyn.callupe.p@uni.pe",
            },
            {
                "apellido": "Carhuas Romero",
                "nombre": "Jhon Jesus",
                "correo": "jhon.carhuas.r@uni.pe",
            },
            {
                "apellido": "Chávez Arifaela",
                "nombre": "Niels Mauro",
                "correo": "niels.chavez.a@uni.pe",
            },
            {
                "apellido": "Del Rio Gutierrez",
                "nombre": "Jairo Kazuo",
                "correo": "jairo.delrio.g@uni.pe",
            },
            {
                "apellido": "Dionicio Achachagua",
                "nombre": "Cesar Alonso",
                "correo": "cesar.dionicio.a@uni.pe",
            },
            {
                "apellido": "Farfan Esteban",
                "nombre": "Gabriel Martin",
                "correo": "gabriel.farfan.e@uni.pe",
            },
            {
                "apellido": "Flores Dalia",
                "nombre": "Gerson Donato",
                "correo": "gfloresd@uni.pe",
            },
            {
                "apellido": "Flores Velarde",
                "nombre": "Roberto Carlos",
                "correo": "roberto.flores.v@uni.pe",
            },
            {
                "apellido": "Leon Sanchez",
                "nombre": "Fransua Mijail",
                "correo": "fransua.leon.s@uni.pe",
            },
            {
                "apellido": "Mallma Orihuela",
                "nombre": "Gherson Bryan",
                "correo": "gherson.mallma.o@uni.pe",
            },
            {
                "apellido": "Mallma Pardo",
                "nombre": "Telesforo",
                "correo": "tmallmap@uni.pe",
            },
            {
                "apellido": "Meza Alvino",
                "nombre": "Fabian Alessandro Moises",
                "correo": "fabian.meza.a@uni.pe",
            },
            {
                "apellido": "Montes Lozano",
                "nombre": "Diego Martin",
                "correo": "diego.montes.l@uni.pe",
            },
            {
                "apellido": "Nuñez Poma",
                "nombre": "Robert Gianpierro Jesus",
                "correo": "robert.nunez.p@uni.pe",
            },
            {
                "apellido": "Palacios Palacios",
                "nombre": "Rafael Enrique",
                "correo": "rafael.palacios.p@uni.pe",
            },
            {
                "apellido": "Palomino Valdivia",
                "nombre": "Erick Da Silva",
                "correo": "erick.palomino.v@uni.pe",
            },
            {
                "apellido": "Quispe Mitma",
                "nombre": "Cesar Fernando",
                "correo": "cesar.quispe.m@uni.pe",
            },
            {
                "apellido": "Quispe Rojas",
                "nombre": "Alfredo Martin",
                "correo": "alfredo.quispe.r@uni.pe",
            },
            {
                "apellido": "Quispe Tenorio",
                "nombre": "Ximena Lucia",
                "correo": "ximena.quispe.t@uni.pe",
            },
            {
                "apellido": "Ramirez Villaverde",
                "nombre": "Oscar Leonardo",
                "correo": "oscar.ramirez.v@uni.pe",
            },
            {
                "apellido": "Rodriguez Inga",
                "nombre": "Fernando Frans",
                "correo": "frodriguezi@uni.pe",
            },
            {
                "apellido": "Salirrosas Avila",
                "nombre": "Sebastian Jose",
                "correo": "sebastian.salirrosas.a@uni.pe",
            },
            {
                "apellido": "Soto Cossio",
                "nombre": "Edwin Isaac",
                "correo": "edwin.soto.c@uni.pe",
            },
            {
                "apellido": "Urbano Chocce",
                "nombre": "Yeison Stiven",
                "correo": "yeison.urbano.c@uni.pe",
            },
            {
                "apellido": "Valencia Grey",
                "nombre": "William Gerardo",
                "correo": "william.valencia.g@uni.pe",
            },
            {
                "apellido": "Valerio Contreras",
                "nombre": "Cristhian Jesus",
                "correo": "cristhian.valerio.c@uni.pe",
            },
            {
                "apellido": "Velasquez Solis",
                "nombre": "Walter Antonio",
                "correo": "walter.velasquez.s@uni.pe",
            },
            {
                "apellido": "Villanueva Reyes",
                "nombre": "Juan Axel",
                "correo": "juan.villanueva.r@uni.pe",
            },
        ]

# Definir la función para registrar puntajes
def registrar_puntajes(fecha_actual, puntajes):
    # Crear un DataFrame con los datos de la tabla
    data = []
    for i, estudiante in enumerate(estudiantes):
        data.append({"Apellido": estudiante["apellido"], "Nombre": estudiante["nombre"], fecha_actual: puntajes[i]})

    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel("Registro_Puntaje_SI650U.xlsx", index=False, sheet_name="Registros")

    # Mostrar mensaje de puntajes registrados correctamente
    mensaje = f"Puntajes de la fecha {fecha_actual} correctamente registrados"
    st.success(mensaje)

# Crear la aplicación Streamlit
def main():
    st.title("Registrador de Puntos SI605U Arquitectura Empresarial")

    # Cuadro desplegable para seleccionar fecha
    fecha_actual = st.date_input("Selecciona la fecha", pd.Timestamp.today())

    # Crear la tabla de asistencia
    st.write("### Tabla de Asistencia")
    puntajes = [0] * len(estudiantes)
    for i, estudiante in enumerate(estudiantes):
        apellido_nombre = f"{estudiante['apellido']} {estudiante['nombre']}"
        puntajes[i] = st.number_input(f"Puntaje para {apellido_nombre}", value=0)

    # Botón para registrar puntajes
    if st.button("Registrar Puntajes"):
        registrar_puntajes(fecha_actual.strftime("%d/%m/%Y"), puntajes)
        try:
            with open("Registro_Puntaje_SI650U.xlsx", "rb") as file:
                data = file.read()
                st.download_button(label="Descargar archivo Excel", data=data, file_name="Registro_Puntaje_SI650U.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        except FileNotFoundError:
            st.warning("No se encontró el archivo Excel. Por favor, primero registra los puntajes.")
        
if __name__ == "__main__":
    main()
