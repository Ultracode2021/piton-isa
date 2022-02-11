def crearFixie():
    fix=open("fax.txt", "w")
    fix.close=()

def escribirFixi():
    fix=open("fax.txt","a")
    fix.write("Mis conocimientos\n")
    fix.write("Intro")
    fix.close

def leerDram():
    fix=open("fax.txt","r")
    frase=fix.readline()
    while frase !="":
        print(frase)
        frase=fix.readline()
    fix.close()    
    
crearFixie()
escribirFixi()
leerDram()
    
