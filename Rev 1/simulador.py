import xlrd
import numpy as np

book = xlrd.open_workbook("teste.xlsx")
sh = book.sheet_by_index(0)
tabela = np.zeros((sh.nrows,sh.ncols))

print(tabela)

print(sh.name, sh.nrows, sh.ncols, book.sheet_names(), book.nsheets)

nrows = int(sh.nrows)
ncols = int(sh.ncols)

for i in range(sh.ncols):
    for j in range(1,sh.nrows):
        print(sh.cell_value(rowx=j, colx=i))
        tabela[j,i] = sh.cell_value(rowx=j, colx=i)

print(tabela)



def movimento(S,V,tabela):
    for j in range(1,sh.nrows):
        if tabela[j,1] <= S < tabela[j,2]:
            if V < tabela[j,3]:
                #print(tabela[j,3])
                #print("Trem com velocidade " + str(V) + " está no circuito " + str(tabela[j,0]) + " com codigo " + str(tabela[j,3]) + " ACELERAR!")
                return 1
            elif V == tabela[j,3]:
                #print(tabela[j,3])
                #print("Trem com velocidade " + str(V) + " está no circuito " + str(tabela[j,0]) + " com codigo " + str(tabela[j,3]) + " MANTER!")
                return 2
            elif V > tabela[j,3]:
                #print(tabela[j,3])
                #print("Trem com velocidade " + str(V) + " está no circuito " + str(tabela[j,0]) + " com codigo " + str(tabela[j,3]) + " FREIAR!")
                return 3

    
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

print("INÍCIO")


S = 0
S0 = 0
V0 = 0
t = 0
a = 0
tempo = 0

print(str(tabela[sh.nrows-1,2]))



while (S < tabela[sh.nrows-1,2]) or (t>= 5000) or (S < 0):
    
    if movimento(S, V0*3.6, tabela) == 1:
        a = 1.2
    elif movimento(S, V0*3.6, tabela) == 2:
        a = 0
    elif movimento(S, V0*3.6, tabela) == 3:
        a = -0.8
        
    S = S0 + V0*t +0.5*a*(t**2)
    
    V = V0 + a*t
    
    V0 = V

    print("Tempo = " + str(tempo) + " //  Vel. = " + str(V*3.6) + "  //  Pos. = " + str(S) + "  // Acc = " + str(a))
    
    t = 0.5
    tempo = tempo + 0.5
    
    S0 = S

print("FIM")
