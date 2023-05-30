#Importar bibliotecas

import tkinter as tk #
from tkinter import filedialog
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from tkinter import PhotoImage

#Definir variáveis globais
concentration_values = []
medias = []
medias_sub = []
listaX = []
kDa = [260,160,110,80,60,50,40,30,20,15,10]
coordenadas_cm = []
graph_name = ''

class EletroScreen(tk.Frame): #Classe referente a tela do Eletroforese
    graph_name = ''
    def generate_graph_eletro(self):#Função que plota o gráfico com a equação da reta

        kDalog = []

        for k in kDa: #Aplica um log de base 10 nos kDa
            a = np.log10(k)
            kDalog.append(a)

        #Essa parte pode trocar
        for coord_pixel in listaX: #Multiplica as coordenadas y por uma constante para transformar em cm
          coord_cm = coord_pixel * 0.02645 
          coordenadas_cm.append(coord_cm)

        #print(coordenadas_cm)
        #print(kDalog)

        x = coordenadas_cm
        y = kDalog

        print(y,x)

        plt.figure()

        plt.scatter(x, y, s=10) # Use o argumento s para definir o tamanho dos pontos

        coeffs = np.polyfit(x, y, 1) # cria um polinomio de grau 1
        a = coeffs[0]
        b = coeffs[1]
        y_pred = a * np.array(x) + b # polinomio do y

        plt.plot(x, y_pred, color='green', label=f"Reta de Regressão: y = {a:.4f}x + {b:.4f}")#Mostra na tela qual a equação da reta

        plt.title(self.graph_name, color='red') # Titulo em cima
        plt.xlabel("Distância(cm)", color='green') # Titulo do eixo X
        plt.ylabel("Peso Molecular(kDa)", color='green') # Titulo do eixo Y

        # Mostra as coordenadas de cada ponto em cima das bolas azuis
        for i in range(len(x)):
            plt.annotate(f"({x[i]:.2f}, {y[i]:.3f})", (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

        plt.legend()
        plt.show()

    def __init__(self, master=None): #Função que inicia a tela
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self): #Função que vai adiconar botões e textos
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Selecionar imagem"
        self.select_button["command"] = self.select_image
        self.select_button.pack(side="top")

        self.point_count_label = tk.Label(self, text='Pontos: 0')
        self.point_count_label.pack(side='top')

        self.quit_button = tk.Button(self, text="Sair", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")
        self.points_label = tk.Label(self)
        self.points_label.pack(side="top", pady=5)

        self.graph_button = tk.Button(self, text='Montar gráfico', command=self.generate_graph_eletro, font=('Arial',12,'bold'), width=20)
        self.graph_button.pack(side='top', pady=10)


    def select_image(self):
        file_path = filedialog.askopenfilename()
        self.image = io.imread(file_path)
        self.fig, self.ax = plt.subplots()

        #self.reso = self.imagem.info.get("dpi")

        #print(self.reso)

        self.ax.imshow(self.image)
        self.ax.set_title('Selecione os pontos de interesse')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        plt.show()

    
    def on_click(self, event):
        if event.button == 1:  # Verifica se o botão esquerdo do mouse foi clicado
            if hasattr(self, 'points'):
                self.points = np.vstack((self.points, [event.xdata, event.ydata]))
            else:
                self.points = np.array([[event.xdata, event.ydata]])
            self.ax.plot(event.xdata, event.ydata, 'o', color='red')
            self.fig.canvas.draw()
        
        # Atualiza o widget tk.Label com as coordenadas dos pontos
        self.points_label.configure(text="Pontos: {}".format(self.points))

        # Guarda as coordenadas X e Y em variáveis separadas
        x, y = event.xdata, event.ydata

        listaX.append(y)
        print(listaX)


        

class SpectroScreen(tk.Frame): #Classe referente a tela do Espectrofotrômetro
    graph_name = ''
    def generate_graph(self):

        medias_sem = []

        for i in medias:
            
            medias_sem.append(i - min(medias))

        print(f'sem{medias}')
        print(f'com{medias_sem}')

        x = medias_sem[:len(medias_sem)]
        y = concentration_values[:len(medias_sem)]

        print(y,x)

        x.reverse()
        y.reverse()

        print(y,x)

        plt.scatter(x, y, s=10) # Use o argumento s para definir o tamanho dos pontos

        # Regressão linear
        coeffs = np.polyfit(x, y, 1)
        a = coeffs[0]
        b = coeffs[1]
        y_pred = a * np.array(x) + b

        plt.plot(x, y_pred, color='green', label=f"Reta de Regressão: y = {a:.4f}x + {b:.4f}")

        plt.title(self.graph_name, color='red') # Titulo em cima
        plt.xlabel("Concentração(mol/L)", color='green')
        plt.ylabel("Absorbância", color='green')

        # Mostra as coordenadas de cada ponto em cima das bolas azuis
        for i in range(len(x)):
            plt.annotate(f"({x[i]:.2f}, {y[i]:.3f})", (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

        plt.legend()
        plt.show()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side='top', fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
    
        self.logo = tk.Label(self, text='Coloque as amostras que você deseja abaixo', font=('Arial', 17, 'bold'), fg='black')
        self.logo.pack(side='top', pady=20)

        # Adiciona a label para o nome do gráfico
        self.graph_name_label = tk.Label(self, text='Nome do gráfico:', font=('Arial', 12, 'bold'))
        self.graph_name_label.pack(side='top', pady=10)

       # Adiciona o campo para o usuário digitar o nome do gráfico
        self.graph_name_entry = tk.Entry(self, width=30)
        self.graph_name_entry.pack(side='top')

        # Adiciona o botão de salvar nome
        self.save_name_button = tk.Button(self, text="Salvar Nome", command=self.save_graph_name)
        self.save_name_button.pack(side='top', pady=10)

        # Guarda o valor digitado pelo usuário em uma variável do tipo str
        self.graph_name = self.graph_name_entry.get()

        graph_name = self.graph_name

        # Adiciona a grade com as células
        self.cells_frame = tk.Frame(self)
        self.cells_frame.pack(side='top', padx=10, pady=10)

        # Adiciona as labels das colunas (1 a 12)
        for i in range(12):
            label = tk.Label(self.cells_frame, text=str(i+1))
            label.grid(row=0, column=i+1)

        # Adiciona as labels das linhas (A a H) e as células em branco
        self.cells = []
        for i in range(8):
            row_cells = []
            label = tk.Label(self.cells_frame, text=chr(65+i))
            label.grid(row=i+1, column=0)
            for j in range(12):
                cell = tk.Entry(self.cells_frame, width = 8)
                cell.grid(row=i+1, column=j+1)
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Adiciona a linha de concentração
        concentration_label = tk.Label(self.cells_frame, text='Concentração')
        concentration_label.grid(row=9, column=0)
        self.concentration_cells = []
        for j in range(12):
            cell = tk.Entry(self.cells_frame, width=8)
            cell.grid(row=9, column=j+1)
            self.concentration_cells.append(cell)

        # Adiciona o botão de cálculo
        self.calculate_button = tk.Button(self, text='Calcular a média das absorbâncias', command=self.calculate_average, font=('Arial',12,'bold'), width=30)
        self.calculate_button.pack(side='top', pady=10)
        self.calculate_button.pack(side='left', pady=10)

        # Adiciona o botão de gráfico
        self.graph_button = tk.Button(self, text='Montar gráfico de absorbância por concentração', command=self.generate_graph, font=('Arial',12,'bold'), width=40)
        self.graph_button.pack(side='top', pady=10)
        self.graph_button.pack(side='left', pady=10)

        #Limpar as listas
        self.remove_button = tk.Button(self, text="Limpar as listas", command=self.remove_button, font=('Arial',12,'bold'), width=20)
        self.remove_button.pack(side='top', pady=10)
        self.remove_button.pack(side='left', pady=10)

        # Adiciona a label de resultado
        self.result_label = tk.Label(self, text='',font=('Arial',12,'bold'))
        self.result_label.pack(side='left', pady=10)
        

        self.graph_name = self.graph_name_entry.get()

    def remove_button(self):
        print(medias, concentration_values)
        medias.clear()
        concentration_values.clear()
        print(medias, concentration_values)
        self.result_label.configure(text='Médias: {}\nConcentrações: {}'.format(medias, concentration_values))
        return medias, concentration_values

    def save_graph_name(self):
        # Obtém o valor do Entry para o nome do gráfico
        self.graph_name = self.graph_name_entry.get()
        return self.graph_name

    def calculate_average(self):
        # Cria uma lista com as colunas que contém valores
        column_values = [[] for _ in range(12)]
        for row_cells in self.cells:
            for i, cell in enumerate(row_cells):
                value = cell.get()
                if value:
                    column_values[i].append(float(value))

        # Calcula a média de cada coluna e atualiza a label de resultado
        for values in column_values:
            if values:
                average = sum(values) / len(values)
                medias.append(round(average, 2))
            #else:
                #medias.append('')
        self.result_label.configure(text='Médias: {}'.format(medias))

        # Adiciona a concentração correspondente às médias
        
        for cell in self.concentration_cells:
            value = cell.get()
            if value:
                concentration_values.append(float(value))
           # else:
               # concentration_values.append('')
        #concentration_values.append('')  # adiciona uma célula vazia para corresponder à primeira célula vazia das outras linhas
        self.cells.append(self.concentration_cells)
        #averages.append('Concentração')
        self.result_label.configure(text='Médias: {}\nConcentrações: {}'.format(medias, concentration_values), padx= 40)
        

        
class StartScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side='top', fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Adiciona uma label com a logo do projeto
    
        self.logo_image = tk.PhotoImage(file="logoilumilab.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.pack(side="top")
        

        # Adiciona os botões
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side='top')

        self.spectro_button = tk.Button(self.button_frame, text='ESPECTROFOTÔMETRO', command=self.open_spectro,font=('Arial',12,'bold'))
        self.spectro_button.pack(side='left', padx=70)
        #self.spectro_button.pack(side='top', padx=70)

        self.eletro_button = tk.Button(self.button_frame, text='ELETROFORESE', command=self.open_eletro,font=('Arial',12,'bold'))
        self.eletro_button.pack(side='left', padx=70)

    def open_eletro(self):
        self.master.destroy()  # Fecha a tela de entrada
        root = tk.Tk()
        app = EletroScreen(master=root)
        app.mainloop()

    def open_spectro(self):
         self.master.destroy()  # Fecha a tela de entrada
         root = tk.Tk()
         spect_screen = SpectroScreen(master=root)
         spect_screen.mainloop()
    
# Inicia o programa com a tela de entrada
root = tk.Tk()
start_screen = StartScreen(master=root)
start_screen.mainloop()
