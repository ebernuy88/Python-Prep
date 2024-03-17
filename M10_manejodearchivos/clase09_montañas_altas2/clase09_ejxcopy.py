import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python clase09_ej1.py <param1> <param2> <param3>")
    else:
        parametro1 = sys.argv[1]  # Se asigna el primer argumento a la variable parametro1
        parametro2 = sys.argv[2]  # Se asigna el segundo argumento a la variable parametro2
        parametro3 = sys.argv[3]  # Se asigna el tercer argumento a la variable parametro3
        
        # Mostrar los parámetros recibidos como salida
        print("Parámetro 1:", parametro1)  # Se imprime el primer parámetro
        print("Parámetro 2:", parametro2)  # Se imprime el segundo parámetro
        print("Parámetro 3:", parametro3)  # Se imprime el tercer parámetro

if __name__ == "__main__":
    main()