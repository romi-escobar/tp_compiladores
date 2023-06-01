import gradio as gr

input_string = input("Por favor, ingrese la entrada: ")
current_position = 0
lista_decimal = []
decimal = 0
p = 0
x = 0
y = 0
resultado = 0


# Definicion de la funcion del no terminal "lista_binario"
def lista_binario():
    decimal = binario()
    lista_decimal.append(decimal)
    R_lista()
    return lista_decimal


# Definicion de la funcion del no terminal "R_lista"
def R_lista():
    global current_position, p
    if current_position < len(input_string):
        if (input_string[current_position] == ' '):
            espacio()
#            match(' ')
            lista_binario()
    else:
        return None


# Definicion de la funcion del no terminal "binario"
def binario():
    global current_position, p
    if current_position < len(input_string):
        if (input_string[current_position] == '0'):
            match('0')
            x = R()
            y = x if x is not None else 0
            return y
        elif (input_string[current_position] == '1'):
            match('1')
            x = R()
            x = x if x is not None else 0
            y = 1 * (2 ** p) + x
            return y
        else:
            error_invalido()
    else:
        error_final()


# Definicion de la funcion del no terminal "binario"
def R():
    global current_position, p
    if current_position < len(input_string):
        if input_string[current_position] == '0' or input_string[current_position] == '1':
            x = binario()
            p += 1
            return x
    else:
        return 0


# Definicion de la funcion del no terminal "espacio"
def espacio():
    global current_position, p
    if current_position < len(input_string):
        if input_string[current_position] == ' ':
            match(' ')
#            current_position += 1
            p = 0
            return True
    else:
        return False


# FUNCION MATCH: valida y avanza la entrada
def match(expected):
    global current_position
    if current_position < len(input_string):
        if input_string[current_position] == expected or (expected == ' ' and input_string[current_position].isspace()):
            current_position += 1
        else:
            error_invalido()
    else:
        error_final()


# Manejo de error de caracter invalido
def error_invalido():
    print("caracter invalido")
#    raise ValueError("Error de sintaxis: No se esperaba el caracter '{}'".format(input_string[current_position]))


# Manejo de error de fin de cadena
def error_final():
    print("fin de cadena")
#    raise ValueError("Error: Se alcanzo el final de la cadena")


resultado = lista_binario()
print("El resultado es: ", resultado)



def greet(input_string):
    return resultado

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch()   