"""Agregar un método: procesar_buffer, Su función es procesar los 
mensajes que se encuentran almacenados en el buffer del nodo.

Se utiliza la biblioteca random para simular eventos de pérdida de 
paquetes en la comunicación entre nodos. El módulo random en Python
proporciona funciones para generar números aleatorios, lo cual se 
utiliza aquí para simular comportamientos aleatorios en la red, 
específicamente la pérdida de paquetes. debemos Importar “random”

También utilizaremos el pop(), que se usa para eliminar y devolver un
elemento de una lista. Cuando se le pasa un argumento, pop(index), 
eliminará y devolverá el elemento en la posición de índice especificada.  

Una vez agregados los elementos tendrá como resultado, información sobre
el proceso de comunicación, incluida la recepción de mensajes, la
congestión del buffer y la pérdida de paquetes.
"""

import time
import random

class Nodo:
    def __init__(self, nombre):
        # Identificador del nodo (servidor o cliente)
        self.nombre = nombre
        
        # Lista de nodos conectados
        self.conexiones = []
        
        self.buffer = []

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
        
        self.procesar_buffer() # Procesa el buffer antes de enviar el mensaje
        
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, emisor):
        print(f"{self.nombre} recibió el mensaje: {mensaje} de: {emisor}")
        self.buffer.append((mensaje, emisor)) # Agrega el mensaje y el emisor al buffer

    def procesar_buffer(self):
        print(f"\n{self.nombre} procesando buffer...")

        while self.buffer:
            mensaje, emisor = self.buffer.pop(0)  # SOLO UN pop

            time.sleep(1)

            if random.random() < 0.5:  # Simula una probabilidad del 50% de pérdida de paquetes
                print(f"❌ Paquete perdido de {emisor}: {mensaje}")
            else:
                print(f"✅ Procesado: {mensaje} de {emisor}")

            print(f"Buffer restante: {len(self.buffer)}")

        time.sleep(1)
        
        
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

servidor.enviar_mensaje("Hola clientes, este es el servidor.")


cliente2.procesar_buffer()
cliente3.procesar_buffer()