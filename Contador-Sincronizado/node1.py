# node1.py
import requests
import time

SERVER_URL = "http://localhost:5000"  # URL del servidor central

def main():
    node_name = "Nodo 1"

    while True:
        # Llamamos a la API /increment
        response = requests.post(f"{SERVER_URL}/increment")
        if response.status_code == 200:
            data = response.json()
            print(f"{node_name} - Valor del contador: {data['counter']}")
        else:
            print(f"{node_name} - Error al incrementar el contador.")

        # Esperamos un tiempo para no saturar el servidor
        time.sleep(2)

if __name__ == "__main__":
    main()
