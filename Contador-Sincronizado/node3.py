# node3.py
import requests
import time

SERVER_URL = "http://localhost:5000"

def main():
    node_name = "Nodo 3"

    while True:
        response = requests.post(f"{SERVER_URL}/increment")
        if response.status_code == 200:
            data = response.json()
            print(f"{node_name} - Valor del contador: {data['counter']}")
        else:
            print(f"{node_name} - Error al incrementar el contador.")
        time.sleep(4)

if __name__ == "__main__":
    main()
