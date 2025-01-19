# node4.py
import requests
import time

SERVER_URL = "http://localhost:5000"


def main():
    node_name = "Nodo 4"
    while True:
        # Obtenemos el valor actual
        response = requests.get(f"{SERVER_URL}/value")
        if response.status_code == 200:
            data = response.json()
            current_value = data["counter"]
            print(f"{node_name} - Valor actual del contador: {current_value}")

            # Si el contador llega a 9, lo reseteamos
            if current_value == 9:
                reset_response = requests.post(f"{SERVER_URL}/reset")
                if reset_response.status_code == 200:
                    reset_data = reset_response.json()
                    print(f"{node_name} - Contador reseteado a: {reset_data['counter']}")
                else:
                    print(f"{node_name} - Error al resetear el contador.")
        else:
            print(f"{node_name} - Error al obtener el valor del contador.")

        # Esperamos un tiempo antes de volver a consultar
        time.sleep(1)


if __name__ == "__main__":
    main()
