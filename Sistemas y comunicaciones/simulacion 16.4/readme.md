# Simulación de Red con POO en Python

## 📌 Introducción

Este proyecto tiene como objetivo simular una red de comunicación básica utilizando Programación Orientada a Objetos (POO) en Python. Se representa un sistema compuesto por un servidor y múltiples clientes que intercambian mensajes.

La simulación permite comprender cómo funcionan las conexiones entre nodos y cómo se transmiten datos dentro de una red.

---

## 🎯 Objetivos

- Aplicar conceptos de Programación Orientada a Objetos.
- Modelar una red simple mediante clases.
- Implementar comunicación entre objetos.
- Simular el envío y recepción de mensajes.

---

## 🧠 Conceptos utilizados

- Clases y objetos
- Métodos (`__init__`, funciones propias)
- Listas (`append`)
- Iteración (`for`)
- Comunicación entre objetos

---

## 🏗️ Estructura del programa

El sistema se basa en una clase principal:

### Clase `Nodo`

Representa cualquier dispositivo dentro de la red (servidor o cliente).

#### Atributos:
- `nombre`: identificador del nodo
- `conexiones`: lista de nodos conectados

#### Métodos:
- `agregar_conexion(nodo)`: conecta un nodo con otro
- `enviar_mensaje(mensaje)`: envía un mensaje a todos los nodos conectados
- `recibir_mensaje(mensaje, emisor)`: recibe y muestra un mensaje

---

## ⚙️ Funcionamiento

1. Se crean 4 nodos:
   - 1 servidor
   - 3 clientes

2. El servidor se conecta a los clientes.

3. El servidor envía un mensaje.

4. Cada cliente recibe y muestra el mensaje en pantalla.

---

## ▶️ Ejecución

Para ejecutar el programa:

```bash
python simulacion.py

porre