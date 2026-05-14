import random
tablero1={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
tablero2={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
class ConNumeros:
    def __init__(self, nombre, simbolo):
        self.nombre=nombre
        self.simbolo=simbolo
    def mostrar_tablero(self,tablero1):
        print(f'{tablero1[1] | tablero1[2] | tablero1[3]}')
        print(f'{tablero1[4] | tablero1[5] | tablero1[6]}')
        print(f'{tablero1[7] | tablero1[8] | tablero1[9]}')
    def colocar_ficha(self, tablero1, posicion):
        if posicion<0 or posicion>9:
            print('Escoge una posicion entre 1 y 9.')
        elif tablero1[posicion]=='X':
            print('Posicion ya tomada.')
        elif tablero1[posicion]=='O':
            print('Posicion ya tomada.')
        else:
            tablero1[posicion]=self.simbolo
    def verificar_ganador(self, tablero1):
        combinaciones=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for combo in combinaciones:
            if tablero1[combo[0]]==tablero1[combo[1]]==tablero1[combo[2]]==self.simbolo:
                return True
            return False
class SinNumeros:
    def __init__(self, nombre, simbolo):
        self.nombre=nombre
        self.simbolo=simbolo
    def mostrar_tablero(self,tablero2):
        print(f'{tablero2[1] | tablero2[2] | tablero2[3]}')
        print(f'{tablero2[4] | tablero2[5] | tablero2[6]}')
        print(f'{tablero2[7] | tablero2[8] | tablero2[9]}')
    def colocar_ficha(self, tablero2, posicion):
        if posicion<0 or posicion>9:
            print('Escoge una posicion entre 1 y 9.')
        elif tablero2[posicion]=='X':
            print('Posicion ya tomada.')
        elif tablero2[posicion]=='O':
            print('Posicion ya tomada.')
        else:
            tablero2[posicion]=self.simbolo
    def verificar_ganador(self, tablero2):
        combinaciones=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for combo in combinaciones:
            if tablero2[combo[0]]==tablero2[combo[1]]==tablero2[combo[2]]==self.simbolo:
                return True
            return False

#jugador1(ConNumeros)=('Paco','X')
jugador1=(ConNumeros,'Paco','X')
jugador1.mostrar_tablero()

def main():
    turno=random.randint(0,1)
    numeros=input('Quiere que el tablero muestre numeros? (s/n)')
    #if numeros=='s':
    jugador