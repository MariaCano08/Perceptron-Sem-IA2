import matplotlib.pyplot as plt

def run():
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    # Dibujar puntos
    #ax.scatter(x=[i for i in range(1,10)],y=[i for i in range(1,10)])
    
    #Dibuja la linea
    ax.plot([1,-0.5],[3,6])

    
    # Guardar el gráfico en formato png
    #plt.savefig('diagrama-dispersion.png')
    # Mostrar el gráfico
    plt.show()


if __name__ == '__main__':
    run()