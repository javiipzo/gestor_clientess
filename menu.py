from cliente import Cliente
def gestor():
    gestor = {}
    while True:
        print("\n")
        print("1. Consultar por DNI")
        print("2. Agregar")
        print("3. Modificar")
        print("4. Borrar")
        print('5. Listar')
        print("6. Salir")

        opcion = int(input("Dime que desea hacer:"))
        if opcion==1:
            dni=input('Introduzca el dni: ')
            cond=False
            for i in gestor:
                if dni==i:
                    print('Nombre %s, Apellido %s, con DNI: %s ' % (gestor[i].nombre, gestor[i].apellido, i))
                    cond=True
            if not cond:
                print('No se ha encontrado')
        elif opcion==2:
            print('Introduzca los datos del cliente: ')
            nombre=input('Introduzca el nombre: ')
            apellido=input('Introduzca el apellido: ')
            dni=input('Introduzca el dni: ')
            client=Cliente(dni,nombre,apellido)
            if dni not in gestor:
                gestor[dni]=client
            else:
                print('El cliente ya estaba en el gestor.')
        elif opcion==3:   
            dni=input('Introduzca el dni: ')
            cond=False
            for i in gestor:
                if dni==i:
                    print('Introduzca los datos que quiere modificar.')
                    nombre=input('Introduzca el nombre: ')
                    apellido=input('Introduzca el apellido: ')
                    gestor[i].nombre=nombre
                    gestor[i].apellido=apellido
                    cond=True
            if not cond:
                print('No se ha encontrado')
        elif opcion==4:
            dni=input('Introduzca el dni: ')
            cond=False
            if dni in gestor:
                del gestor[dni]
                cond=True
            if not cond:
                print('No se ha encontrado')
        elif opcion==5:
            for i in gestor:
                print(gestor[i])
        elif opcion==6:
            break
