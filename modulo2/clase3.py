# trabajo con archivos CSV
import csv
from pathlib import Path

FILE_PATH = Path('users.csv')

def read_csv():
    try:
        with open(FILE_PATH,'r')as file:
            reader = csv.DictReader(file)
            for row in reader:
                    print(row.get('first_name'),':',row.get('email'))
    except:
        print('No se encontro el archivo')
        
def write_csv():
    try:
        with open(FILE_PATH,'a') as file:
            writer = csv.DictWriter(
                file,fieldnames = ['first_name','last_name','email']
            )
            
            writer.writerows([
                {
                'first_name':'Cesar',
                'last_name':'Mayta',
                'email':'cesarmayta@ed.team'
                },
                {
                'first_name':'Alvaro',
                'last_name':'Felipe',
                'email':'alvFelipe@ed.team'    
                },
            ]) 
            print("datos agregados")
    except:
        print("no se encontro el archivo")
    
if __name__ == '__main__':
    write_csv()
    read_csv()
    

