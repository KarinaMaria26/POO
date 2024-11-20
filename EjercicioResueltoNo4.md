EdadJuan = int(input("Ingrese la edad de Juan"))           #Permite que el usuario ingrese la edad de Juan

EdadAlberto = int(EdadJuan * (2/3))                                #Permite el cálculo de la edad de Alberto
EdadAna = int(EdadJuan * (4/3))                                     #Permite el cálculo de la edad de Ana
EdadMama = int(EdadJuan + EdadAna + EdadAlberto) #Permite el cálculo de la edad de la mamá

print("La edad de Juan es:", EdadJuan)
print("La edad de Alberto es:", EdadAlberto)
print("La edad de Ana es:", EdadAna)
print("La edad de Mamá es:", EdadMama)
