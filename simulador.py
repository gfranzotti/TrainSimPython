import xlrd
import numpy as np


#Rev 2.0
#26/01/2017

book = xlrd.open_workbook("teste2.xlsx")
sh = book.sheet_by_index(0)
tabela = np.zeros((sh.nrows,sh.ncols))

#print(tabela)

#print(sh.name, sh.nrows, sh.ncols, book.sheet_names(), book.nsheets)

nrows = int(sh.nrows)
ncols = int(sh.ncols)

for i in range(sh.ncols):
    for j in range(1,sh.nrows):
        print(sh.cell_value(rowx=j, colx=i))
        tabela[j,i] = sh.cell_value(rowx=j, colx=i)

#print(tabela)

ACC = 1.12
JERKIN = 1.0
JERKOUT = -1.0
BRAKE = -1.2


def movimento(S,V,tabela,a, ACC, JERKIN, JERKOUT, BRAKE):
    for j in range(1,sh.nrows):
        if tabela[j,1] <= S < tabela[j,2]:
            if V < tabela[j,3]-3:
                if a < ACC:
                    J = JERKIN
                elif a > ACC:
                    J = -1
                else:
                    J = 0
                    
                #print(tabela[j,3])
                #print("Trem com velocidade " + str(V) + " está no circuito " + str(tabela[j,0]) + " com codigo " + str(tabela[j,3]) + " ACELERAR!")
                return [1,J]
            
            elif (V > (tabela[j,3]-3) )and( V < (tabela[j,3])):
                if a > 0:
                    J = JERKOUT
                elif a < 0:
                    J = JERKIN
                else:
                    J=0
                                   
                                    
                #print(tabela[j,3])
                #print("Trem com velocidade " + str(V) + " está no circuito " + str(tabela[j,0]) + " com codigo " + str(tabela[j,3]) + " MANTER!")
                return [2,J]
            
            elif V > tabela[j,3]:
                if a > BRAKE:                 
                    J = -1
                elif a < BRAKE:
                    J = JERKIN
                else:
                    J = 0
                    
                    
                #print(tabela[j,3])
                #print("Trem com velocidade " + str(V) + " está no circuito " + str(tabela[j,0]) + " com codigo " + str(tabela[j,3]) + " FREIAR!")
                return [3,J]

    
'''
S = 550
V = 40
print("teste movimento deve ser 1 : " + str(movimento(S,V,tabela)))

S= 1050
V= 50
print("teste movimento deve ser 3 : " + str(movimento(S,V,tabela)))

S= 1202
V= 30
print("teste movimento deve ser 2 : " + str(movimento(S,V,tabela)))
'''

print("************\n\n***INÍCIO***\n\n************")


S = tabela[1,1]
S0 = tabela[1,1]
V0 = 0
t = 0
a = 0
a0 = 0
tempo = 0
J=0
MOV=0

#print(str(tabela[sh.nrows-1,2]))



while (S < tabela[sh.nrows-1,2]) or (t>= 5000) or (S < 0):
    '''
    if movimento(S, V0*3.6, tabela) == 1:
        a = 1.2
    elif movimento(S, V0*3.6, tabela) == 2:
        a = 0
    elif movimento(S, V0*3.6, tabela) == 3:
        a = -0.8
    '''
    MOV, J = movimento(S, V0*3.6, tabela, a, ACC, JERKIN, JERKOUT, BRAKE)
                                             
    a = a0 + J*t
                                             
    S = S0 + V0*t +0.5*a*(t**2)+(J/6)*(t**3)
    
    V = V0 + a*t
    
    V0 = V

    a0 = a

    print("Tempo = {0:.1f} /// Vel. = {1:.1f} /// Pos. = {2:.1f} /// Acel. = {3:.3f} /// Jerk = {4:.3f} /// Mov. = {5:.0f}".format(tempo, V*3.6, S, a, J, MOV))
          
   # print("Tempo = " + str(tempo) + " //  Vel. = " + str(V*3.6) + "  //  Pos. = " + str(S) + "  // Acc = " + str(a))
    
    t = 0.05
                                             
    tempo = tempo + 0.05
    
    S0 = S

print("FIM")
