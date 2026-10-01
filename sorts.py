from item import less, exch, compexch

def selection_sort(input_data):
    valores = input_data
    itens = len(input_data)
   
    i = 1
    j = 0
    b = True

    while b:
        
        if less(int(valores[i]), int(valores[j])):
            valores[j], valores[i] = exch(valores[j], valores[i])
            #print(f"minimo:{valores[j]}, valor:{valores[i]}")
            
        i+=1

        if i == itens:
        
            j+=1
            i = j + 1
            if j == itens -1 :
                b = False
            
    return valores
    
        
def insertion_sort(input_data):

    valores = input_data
    itens = len(input_data)
   
    i = 1

    while i < itens:
        j = i

        while j > 0 and less(int(valores[j]), int(valores[j-1])):
            valores[j], valores[j-1] = exch(valores[j], valores[j-1])
            j -= 1

        i += 1

    return valores
            

def bubble_sort(input_data):
    valores = input_data
    itens = len(input_data)
   
    i = 1
    j = 0
    b = True
    p = False

    while b:
        
        if less(int(valores[i]), int(valores[j])):
            valores[i], valores[j] = exch(valores[i], valores[j])
           # print(f"maior:{valores[i]}, menor:{valores[j]}")
            p = True

        j+=1
        i+=1

        if i == itens :
            if p == False:
                b = False
            else:
                j = 0
                i = 1
                p = False
            
    return valores

def shaker_sort(input_data):

    valores = input_data
    itens = len(input_data)
   
    i = 1
    j = 0
    b = True
    p = False
    ida = True

    while b:
        if ida:
            if less(int(valores[i]), int(valores[j])):
                valores[i], valores[j] = exch(valores[i], valores[j])
               # print(f"maior:{valores[i]}, menor:{valores[j]}")
                p = True

            j+=1
            i+=1

            if i == itens :
                if p == False:
                    b = False
                else:
                    j = itens - 2
                    i = itens - 1
                    p = False
                    ida = False
        else:
            if less(int(valores[j]), int(valores[i])):
                valores[j], valores[i] = exch(valores[i], valores[j])
               # print(f"maior:{valores[i]}, menor:{valores[j]}")
                p = True

            j-=1
            i-=1

            if i == 0 :
                if p == False:
                    b = False
                else:
                    j = 0
                    i = 1
                    p = False
                    ida = True
            
    return valores

#A = 2
#B = 3
#A,B = compexch(A,B)
#print(A,B)