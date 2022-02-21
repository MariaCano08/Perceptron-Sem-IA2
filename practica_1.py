import matplotlib.pyplot as plt
import numpy 


def y(x,m,b):
    return m*x+b


def window(x1,x2,y,m,b,compuerta):
    i=0
    fig, ax = plt.subplots()
    for y_es in y:
        if y_es == False:
            ax.scatter(x=x1[i],y=x2[i],color='tab:cyan')
        else:
            ax.scatter(x=x1[i],y=x2[i],color='tab:pink')
        ax.plot([x1[i],x2[i]],[m*x1[i]+b, m*x2[i]+b], color='tab:red')
        
        i=i+1
    plt.plot(1,1,'tab:cyan',label="Estimada 0")
    plt.plot(1,1,'tab:pink',label="Estimada 1")
    plt.legend(loc = "upper right")
    plt.title("Perceptron: "+compuerta)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()

def inputs():
    inputs_=[]
    input_=[]
    x1=[]
    x2=[]
    flag=True
    txt=open('input.txt')
    for linea in txt:
        input_=[]
        for lettle in linea:
            if lettle=='\n':
                continue
            elif  lettle == ",":
                continue
            else:
                change=int(lettle)
                input_.append(change)
                if flag :
                    x1.append(change)
                    flag= False
                else:
                    x2.append(change)
                    flag= True
        
        inputs_.append(input_) 
    txt.close()
    return inputs_,x1,x2


def activation_funtion(u):
    if u<0:
        return False
    else:
        True


def to_string(input_,boleano):
    if boleano == False :
        print("     ",input_, 0)
    else:
        print("     ",input_, 1)


def perceptron(inputs, theta):
    w=[1,1]
    y=[]
    #print(inputs)
    for input_ in inputs:
        u=numpy.dot(w,input_)-theta
        y.append(activation_funtion(u))
        to_string(input_,activation_funtion(u))
        # print(input_,u )
        # print(activation_funtion(u)) 
    m=-(w[0]/w[1])
    b=theta/w[1]
    return y,m,b


def start(theta):
    input_,x1,x2=inputs()
    y,m,b=perceptron(input_,theta)
    if theta== 1.5:
        window(x1,x2,y,m,b,"AND")
    else:
        window(x1,x2,y,m,b,"OR")


def run():
    opcion=0
    while opcion != 3:
        print("""Perceptron 💕
    Elija la opcion deseada 😊
    1 Para perceptron con la compuerta AND
    2 Para perceptron con la compuerta OR  
    3 Para salir😢""")
        opcion=int(input())
        if opcion == 1:
            start(1.5)
        elif opcion == 2:
            start(0.4)
        elif opcion == 3:
            print("Bye bye 😘")
        else: 
            opcion=input(int("Opcion incorrecta ❌, verifique "))
    


if __name__ == '__main__':
    run()