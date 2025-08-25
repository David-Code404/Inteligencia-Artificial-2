import pandas as pd
import os

# --- 1. DEFINIR LAS RUTAS DE ARCHIVO ---
input_file_path = '/home/davidcode/Descargas/Inteligencia-Artificial-2/Examen-Practico-Elecciones/Datos-Originales/datos.csv'
output_file_path = '/home/davidcode/Descargas/Inteligencia-Artificial-2/Examen-Practico-Elecciones/Datos_Usados/datos_limpios.csv'

# --- 2. PROCESAR EL ARCHIVO ---
try:
    # Cargar el archivo CSV original completo
    df_original = pd.read_csv(input_file_path)

    # Mapeo de columnas originales a los nombres deseados
    column_mapping = {
        'CodigoMesa': 'CODIGO MESA',
        'NumeroMesa': 'MESA',
        'NombreDepartamento': 'DEPARTAMENTO',
        'NombreMunicipio': 'MUNICIPIO',
        'NombreRecinto': 'RECINTO',
        'CodigoCircunscripcionU': 'CIRCUNSCRIPCION',
        'InscritosHabilitados': 'ELECTORES HABILITADOS',
        'VotoEmitido': 'PAPELETAS EN ANFORA',
        'VotoValido': 'VALIDOS',
        'VotoBlanco': 'BLANCOS',
        'VotoNuloDirecto': 'NULOS'
    }

    # Renombrar las columnas
    df_renombrado = df_original.rename(columns=column_mapping)

    # Calcular 'PAPELETAS NO UTILIZADAS' (esta columna no existe en el original)
    df_renombrado['PAPELETAS NO UTILIZADAS'] = df_renombrado['ELECTORES HABILITADOS'] - df_renombrado['PAPELETAS EN ANFORA']

    # Definir la lista de columnas finales que queremos
    columnas_finales = [
        'CODIGO MESA',
        'MESA',
        'DEPARTAMENTO',
        'MUNICIPIO',
        'RECINTO',
        'CIRCUNSCRIPCION',
        'ELECTORES HABILITADOS',
        'PAPELETAS EN ANFORA',
        'PAPELETAS NO UTILIZADAS',
        'VALIDOS',
        'BLANCOS',
        'NULOS'
    ]

    # Seleccionar solo las columnas relevantes
    df_limpio = df_renombrado[columnas_finales]

    # --- 3. GUARDAR EL RESULTADO ---
    # Asegúrate de que la carpeta de salida exista
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    # Guardar el DataFrame limpio en un nuevo archivo CSV
    df_limpio.to_csv(output_file_path, index=False)

    print(f"Proceso completado exitosamente.")
    print(f"Los datos limpios han sido guardados en: '{output_file_path}'.")
    print(f"\nNúmero de filas procesadas: {len(df_limpio)}")
    print("\nPrimeras 5 filas del nuevo archivo:")
    print(df_limpio.head())

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta '{input_file_path}'.")
    print("Asegúrate de que la ruta y el nombre del archivo son correctos.")
except KeyError as e:
    print(f"Error en la columna: {e}")
    print("El archivo CSV no tiene una de las columnas relevantes. Revisa los nombres y la ortografía.")
    print("\nColumnas disponibles en el archivo original:")
    print(df_original.columns.tolist())
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")