"""Actividad:
Una vez que tenemos el código de la simulación de red básico vamos a
simular una desconexión y conexión de un enrutamiento de la red.

Agregar un método: eliminar_conexion, que a diferencia con agregar 
usaremos .remove.

Utilizaremos una función de Python “time.sleep(segundos)” , 
tenemos que importar “time” .
Esto hace que el programa se detenga durante los segundos que 
determinemos antes de continuar con la ejecución del código siguiente.
En este caso, se está utilizando para simular un retraso entre la
desconexión y la reconexión dinámica de los nodos en la red de
comunicación.

Luego del retraso temporal imprimirá el mensaje : “Simulando 
desconexión y reconexión dinámica…”

Por último imprimirá el mensaje : "¡Hola de nuevo a todos!".
"""
import time



class Nodo:
    def __init__(self, nombre):
        # Identificador del nodo (servidor o cliente)
        self.nombre = nombre
        
        # Lista de nodos conectados
        self.conexiones = []

    def agregar_conexion(self, nodo): # Agrega un nodo a la lista de conexiones del nodo actual
        self.conexiones.append(nodo) 
        print("Reconexión dinámica...")
        time.sleep(2) # Simula un retraso de 2 segundos
        
        
    def eliminar_conexion(self, nodo): # Elimina un nodo de la lista de conexiones del nodo actual
        self.conexiones.remove(nodo)
        print("Desconexión...")
        time.sleep(2) # Simula un retraso de 2 segundos

    def enviar_mensaje(self, mensaje):
        print("Enviando mensaje...")
        time.sleep(2) # Simula un retraso de 2 segundos
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, emisor):
        print(f"{self.nombre} recibió el mensaje: {mensaje} de: {emisor}")
        
# Crear nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

# Conectar servidor con clientes
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

servidor.eliminar_conexion(cliente1)

servidor.enviar_mensaje("Hola clientes, este es el servidor.")