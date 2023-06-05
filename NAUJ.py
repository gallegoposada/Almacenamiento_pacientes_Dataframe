import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

saludo = '''**** BIENVENID@ ****'''
print(saludo)

cant_registros=int(input("Ingrese el numero de pacientes que desea registrar: "))

df_pacientes = pd.DataFrame(columns=["Nombre", "Num. Identificación", "Sexo", "Edad", "Peso", "Estatura cm", "IMC", "IMC cat", "Rango Edad"])

for i in range (0, cant_registros):
    nombre = input("Ingrese el nombre del paciente " + str(i+1) + " : ")
    while True:
        try:
            identificacion = int(input("Ingresa el número de identificación del paciente " + str(i+1) + " : "))
            break
        except:
            print("Debes ingresar un número.")
    
    while True:
        sexo = input("Ingresa el sexo del paciente " + str(i+1) +  " (H - hombre / M -  mujer / O - oto): ")
        sexo = sexo.upper()
        if sexo== 'H' or sexo== 'M' or sexo=='O':
            break

        else:
            print("El sexo debe ser especificado con H para hombre, M para mujer u O para otro.")
    
    
    while True:
        try:
            edad = int(input("Ingresa la edad del paciente " + str(i+1) + " : "))
            if 0 < edad <= 10:
                rango_edad = "0-10"
            if 10 < edad <= 20:
                rango_edad = "11-20"
            if 20 < edad <= 30:
                rango_edad = "21-30"
            if 30 < edad <= 40:
                rango_edad = "31-40"
            if 40 < edad <= 50:
                rango_edad = "41-50"
            if 50 < edad <= 60:
                rango_edad = "51-60"
            if 60 < edad <= 70:
                rango_edad = "61-70"
            if 70 < edad <= 80:
                rango_edad = "71-80"
            if 80 < edad <= 90:
                rango_edad = "81-90"
            break
        except:
            print("Debes ingresar un número.")
    
    while True:
        try:
            Peso = float(input("Ingresa el peso en Kg del paciente " + str(i+1) + " : "))
            break
        except:
            print("Debes ingresar un número.")
    
    while True:
        try:
            estatura= float(input("Ingresa la estatura del paciente en centimetros " + str(i+1) + " : "))
            break
        except:
            print("Debes ingresar un número.")
    
    IMC_num = Peso / ((estatura/100)**2)
    if IMC_num < 18.5:
        IMC_cat = "Bajo Peso"
    if 18.5 <= IMC_num <= 24.9:
        IMC_cat = "Peso Normal"
    if 24.9 < IMC_num < 29.9:
        IMC_cat = "Sobrepeso"
    if 29.9 < IMC_num:
        IMC_cat = "Obesidad"

    nuevo_registro = {'Nombre':nombre, 'Num. Identificación': identificacion, 'Sexo':sexo, 
    'Edad':edad, 'Peso':Peso, 'Estatura cm':estatura, 'IMC': IMC_num, 'IMC cat': IMC_cat, 'Rango Edad':rango_edad}
    
    df_pacientes = df_pacientes.append( nuevo_registro, ignore_index = True)


print(df_pacientes)

menu = """
---- MENÚ DE OPCIONES ----
1. Registrar nuevo Paciente.
2. Eliminar Paciente por num. de indice.
3. Filtrar por sexo.
4. Evaluar rangos etarios.
5. Evaluación IMC.
6. Análisis estadistico de datos.
7. Ver tabla de contenido
8. Salir.
"""
aux = 0

while aux == 0:
    print(menu)
  
    op = int(input("Ingresa el número de la opción: "))

    if op == 1:

        nombre = input("Ingrese el nombre del paciente: ")
        while True:
            try:
                identificacion = int(input("Ingresa el número de identificación del paciente: "))
                break
            except:
                print("Debes ingresar un número.")
    
        while True:
            sexo = input("Ingresa el sexo del paciente (H - hombre / M -  mujer / O - oto): ")
            sexo = sexo.upper()
            if sexo== 'H' or sexo== 'M' or sexo=='O':
                break

            else:
                print("El sexo debe ser especificado con H para hombre, M para mujer u O para otro.")
    
    
        while True:
            try:
                edad = int(input("Ingresa la edad del paciente: "))
                if 0 < edad <= 10:
                    rango_edad = "0-10"
                if 10 < edad <= 20:
                    rango_edad = "11-20"
                if 20 < edad <= 30:
                    rango_edad = "21-30"
                if 30 < edad <= 40:
                    rango_edad = "31-40"
                if 40 < edad <= 50:
                    rango_edad = "41-50"
                if 50 < edad <= 60:
                    rango_edad = "51-60"
                if 60 < edad <= 70:
                    rango_edad = "61-70"
                if 70 < edad <= 80:
                    rango_edad = "71-80"
                if 80 < edad <= 90:
                    rango_edad = "81-90"
                break
            except:
                print("Debes ingresar un número.")
    
        while True:
            try:
                Peso = float(input("Ingresa el peso en Kg del paciente: "))
                break
            except:
                print("Debes ingresar un número.")
    
        while True:
            try:
                estatura= float(input("Ingresa la estatura del paciente en centimetros: "))
                break
            except:
                print("Debes ingresar un número.")
    
        IMC_num = Peso / ((estatura/100)**2)
        if IMC_num < 18.5:
            IMC_cat = "Bajo Peso"
        if 18.5 <= IMC_num <= 24.9:
            IMC_cat = "Peso Normal"
        if 24.9 < IMC_num < 29.9:
            IMC_cat = "Sobrepeso"
        if 29.9 < IMC_num:
            IMC_cat = "Obesidad"

        nuevo_registro = {'Nombre':nombre, 'Num. Identificación': identificacion, 'Sexo':sexo, 
        'Edad':edad, 'Peso':Peso, 'Estatura cm':estatura, 'IMC': IMC_num, 'IMC cat': IMC_cat, 'Rango Edad':rango_edad}
    
        df_pacientes = df_pacientes.append( nuevo_registro, ignore_index = True)
    
    if op==2:
        ayuda = 0
        while True:
            try:
                num_indice=int(input("Ingrese el número de indice del registro que desea eliminar: "))
                df_pacientes = df_pacientes.drop(num_indice)
                print("Registro eliminado exitosamente !!")
                ayuda +=1
                break
            except:
                print("Debes ingresar un número.")
        
        if ayuda == 0:
            print("El número de identificación no ha sido encontrado.")

    if op == 3:
        filtro_sex=input("Ingrese H para filtrar por hombres, M para filtrar por mujeres u O para filtrar por otros: ")
        filtro_sex = filtro_sex.upper()
        if filtro_sex== 'H':
            hombre = pd.DataFrame(columns=["Nombre", "Num. Identificación", "Sexo", "Edad", "Peso", "Estatura", "IMC", "IMC cat", "Rango Edad"])
            hombre = df_pacientes[df_pacientes['Sexo'] == 'H']
            print(hombre)
        
        elif filtro_sex== 'M':
            mujer = pd.DataFrame(columns=["Nombre", "Num. Identificación", "Sexo", "Edad", "Peso", "Estatura", "IMC", "IMC cat", "Rango Edad"])
            mujer = df_pacientes[df_pacientes['Sexo'] == 'M']
            print(mujer)
        
        elif filtro_sex== 'O':
            otro = pd.DataFrame(columns=["Nombre", "Num. Identificación", "Sexo", "Edad", "Peso", "Estatura", "IMC", "IMC cat", "Rango Edad"])
            otro = df_pacientes[df_pacientes['Sexo'] == 'O']
            print(otro)

        else:
            print("Opción inválida, intente de nuevo.")
    

    if op == 4:
        sns.catplot(x='Rango Edad', data = df_pacientes, kind='count', hue='Sexo')
        plt.show()

    if op == 5:

        sns.catplot(x='IMC cat', data = df_pacientes, kind='count', hue='Sexo')
        plt.show()


    if op == 6:

        sns.catplot(x='Sexo', y='Edad', data= df_pacientes, kind='box')
        sns.catplot(x='Sexo', y='Peso', data= df_pacientes, kind='box')
        sns.catplot(x='Sexo', y='Estatura cm', data= df_pacientes, kind='box')
        sns.catplot(x='Sexo', y='IMC', data= df_pacientes, kind='box')
        plt.show()

    if op == 7:
        print(df_pacientes)

    if op == 8:

        aux = aux + 1