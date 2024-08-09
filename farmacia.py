import json

def abrirArchivo():
    miJSON=[]
    with open('Ventas.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Ventas.json","w") as outfile:
        json.dump(miData,outfile)

def abrirArchivo():
    miJSON=[]
    with open('Compras.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Compras.json","w") as outfile:
        json.dump(miData,outfile)        

def abrirArchivo():
    miJSON=[]
    with open('Empleados.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Empleados.json","w") as outfile:
        json.dump(miData,outfile)

def abrirArchivo():
    miJSON=[]
    with open('Medicamentos.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Medicamentos.json","w") as outfile:
        json.dump(miData,outfile)

def abrirArchivo():
    miJSON=[]
    with open('Pacientes.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Pacientes.json","w") as outfile:
        json.dump(miData,outfile)

def abrirArchivo():
    miJSON=[]
    with open('Proveedores.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Proveedores.json","w") as outfile:
        json.dump(miData,outfile)                        


print("     __________________________")
print("    | BIENVENIDO A LA FARMACIA|")
print("    |_________________________|")

print("\n1.Ventas\n2.Compras")
opc=int(input("Elige una opción: "))
miInfo=[]

if(opc==1):
    nuevaVenta = {}
    print("-----------------------------------------------")
    print("DATOS DE VENTA")
    print("")
    nuevaVenta["fechaVenta"] = input("fecha de venta: ")
    print("-----------------------------------------------")
    print("DATOS DEL PACIENTE")
    print("")
    nuevaVenta["nombrePaciente"] = input("Nombre : ")
    nuevaVenta["direccion"] = input("Dirección : ")
    print("-----------------------------------------------")
    print("DATOS DEL EMPLEADO")
    print("")
    nuevaVenta["nombreEmpleado"] = input("Nombre : ")
    nuevaVenta["cargo"]=input("Cargo : ")
    print("-----------------------------------------------")
    print("DATOS DEL MEDICAMENTO")
    print("")
    nuevaVenta["nombreMedicamento"] = (input("Nombre : "))
    nuevaVenta["cantidadVendida"] = int(input("Cantidad : "))
    nuevaVenta["precio"] = int(input("Precio : "))
   
    miInfo = abrirArchivo()
    miInfo[0]["ventas"].append(nuevaVenta)
    guardarArchivo(miInfo)
    print("venta registrada exitosamente.")


