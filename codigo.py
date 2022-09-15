import datetime
import time

salas= {}
reservaciones = {}
clientes= {}

print("*"*20)
print("*"*4 + " BIENVENIDO " + "*"*4 )
print("*"*20)

while True:
  print("-"*20)
  print("1. Registrar reservación de una sala")
  print("2. Editar nombre de una reservación ya hecha")
  print("3. Consultar reservación existente para una fecha específica")
  print("4. Registrar nuevo cliente")
  print("5. Registrar sala")
  print("6. Salir \n")
  opcion = int(input("Ingrese el núm. de la acción que quiere realizar \n"))

  if opcion == 1:
    clave_cliente = int(input("Ingrese la clave de cliente: \n"))

    clave_clientes = [clave for clave in clientes.keys()]

    if clave_cliente in clave_clientes:
      fecha_capturada = input("Ingrese la fecha del evento (dd/mm/aaaa): \n")
      fecha_reservacion = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
      fecha_actual = datetime.date.today()
      fecha_valida = fecha_reservacion - datetime.timedelta(days=2)

      if fecha_actual <= fecha_valida:
        clave_sala = int(input("Ingrese la clave de la sala deseada: \n"))

        clave_salas = [clave for clave in salas.keys()]

        if clave_sala in clave_salas:
          turno = input("Ingrese el turno deseado ('M','V','N'): \n")

          if turno.upper() == 'M':
            turno = 'MATUTINO'
          elif turno.upper() == 'V':
            turno = 'VESPERTINO'
          elif turno.upper() == 'N':
            turno = 'NOCTURNO'

          coincidencias = 0
          for sala, fecha, cliente, nombre, turno_reservacion in reservaciones.values():
            if (clave_sala == sala) and (fecha_reservacion == fecha) and (turno == turno_reservacion):
              coincidencias += 1

          if coincidencias == 0:
            nombre_reservacion = input("Ingrese el nombre del evento: \n")

            clave_reservacion = max(list(reservaciones.keys()), default = 0) + 1

            for clave_registrada, [nombre] in clientes.items():
              if clave_sala == clave_registrada:
                nombre_cliente = nombre

            reservaciones[clave_reservacion] = [clave_sala, fecha_reservacion, nombre_cliente, nombre_reservacion, turno]

            print(f"Reservación realizada, esta es la clave de reservación: {clave_reservacion}\n")

          else:
            print("Ya hay una reservación en el tiempo seleccionado\n")
        else:
          print("Se tiene que escoger una sala existente\n")
      else:
        print("La reservación se tiene que hacer dos días antes de la fecha del evento\n")
    else:
      print("Ingrese una clave de cliente existente\n")

  elif opcion == 2:
    clave = int(input("Ingrese la clave de la reservación: \n"))

    if clave in reservaciones.keys():
      nombre_nuevo = input("Ingrese nuevo nombre: \n")

      for clave_registrada, [sala, fecha, cliente, nombre, turno_reservacion] in reservaciones.items():
        if clave == clave_registrada:
          reservaciones.update({clave_registrada: [sala, fecha, cliente, nombre_nuevo, turno_reservacion]})

          print(f"Modificación exitosa, nuevo nombre: {nombre_nuevo}\n")

    else:
      print("Ingrese una clave de reservación válida\n")

  elif opcion == 3:
    fecha_solicitada = input("Ingrese la fecha del evento (dd/mm/aaaa): \n")
    fecha_modificada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()

    print("\n" + "*"*77)
    print("**" + " "*13 + f"REPORTE DE RESERVACIONES PARA EL DÍA {fecha_solicitada}" + " "*13 + "**")
    print("*"*77)
    print("{:<6} {:<20} {:<38} {:<13}".format('SALA','CLIENTE','EVENTO', 'TURNO'))
    print("*"*77)

    for clave_registrada, [sala, fecha, cliente, nombre, turno_reservacion] in reservaciones.items():
      if fecha_modificada == fecha:
        print("{:<6} {:<20} {:<38} {:<13}".format(sala, cliente, nombre, turno_reservacion))

    print("*"*30 + " FIN DEL REPORTE " + "*"*30)

  elif opcion == 4:
    nombre_cliente = input("Ingrese nombre de cliente a registrar: \n")
    clave_cliente = max(list(clientes.keys()), default = 0) + 1

    clientes[clave_cliente] = [nombre_cliente]

    print(f"Cliente registrado, clave de nuevo cliente: {clave_cliente}\n")

  elif opcion == 5:
    nombre_sala = input("Ingrese nombre de la sala a registrar: \n")
    capacidad=int(input("Ingrese la capacidad de la sala: \n"))

    clave_sala = max(list(salas.keys()), default = 0) + 1

    salas[clave_sala] = [nombre_sala,capacidad]

    print(f"Sala registrada, clave de nueva sala: {clave_sala}\n")

  elif opcion == 6:
    break

  else:
    print("Ingrese una respuesta válida\n")

print("GRACIAS POR SU PREFERENCIA")