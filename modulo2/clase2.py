"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
"""
import platform, socket
from pathlib import Path
FILE_PATH = 'pc.txt'


def guardar_pc_info():
    pc_data ="====== INFO DE PC ======\n "
    pc_data += "SISTEMA OPERATIVO: "+platform.system()
    pc_data += " "+platform.version()+'\n'
    pc_data += "ARQUITECTURA : "+platform.machine() + '\n'
    pc_data += "PROCESADOR : "+platform.processor() + '\n'
    pc_data += "HOSTNAME : "+ socket.gethostname() + '\n'
    pc_data += 'IP :'+socket.gethostbyname(socket.gethostname())+"\n"
    
    
    with open(FILE_PATH,'w') as pc_file:
        pc_file.write(pc_data)
    
    print('El archivo se guardo con Exito!!')


def leer_pc_info():
    try:
        with open(FILE_PATH,'r') as pc_file:
            pc_data = pc_file.read()
            print(pc_data)            
    except:
        print("No se encontro el archivo")
        
        
if __name__=='__main__':
    guardar_pc_info()
    leer_pc_info()