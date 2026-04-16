"""Objetivo:
El objetivo de esta actividad es comprender el concepto de redes de comunicación y practicar la implementación de una simulación básica de una red utilizando programación orientada a objetos en Python.
Instrucciones:
Implementación del código:
Escribe el código necesario para crear la simulación de red. De un servidor y tres clientes.
Crea la clase Nodo con sus métodos __init__, agregar_conexion, enviar_mensaje y recibir_mensaje.
Crea instancias de la clase Nodo para representar el servidor y los clientes.
Establece las conexiones entre el servidor y los clientes utilizando el método agregar_conexion.
Simula el envío de un mensaje desde el servidor a todos los clientes conectados utilizando el método enviar_mensaje.
Prueba y depuración:
Ejecuta tu código para verificar que funcione correctamente.
Comprueba que los mensajes se envíen y reciban correctamente entre el servidor y los clientes.
Ayuda: uno de los posibles componentes que se podría usar es : append:
append() es un método de las listas en Python que se utiliza para agregar un elemento al final de la lista.
Entrega:
● Deberán presentar los archivos .py identificados de manera clara y ordenada.
● Trabajar una buena documentación. Subir al repositorio.
● Se debe enviar el enlace al repositorio correspondiente via classroom"""

class Nodo:
    def __init__(self, nombre):
        # Identificador del nodo (servidor o cliente)
        self.nombre = nombre
        
        # Lista de nodos conectados
        self.conexiones = []

    def agregar_conexion(self, nodo): # Agrega un nodo a la lista de conexiones del nodo actual
        self.conexiones.append(nodo) 

    def enviar_mensaje(self, mensaje):
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

servidor.enviar_mensaje("Hola clientes, este es el servidor.")