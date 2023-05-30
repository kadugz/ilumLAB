# IlumLab 🌈

## Tema 👋

Tratamento de dados de espectroscopia para cálculo de substâncias desconhecidas e de eletroforese.

## Alunos 🤓

- André de Araújo 😈
- Carlos Eduardo 🤠
- Vinicius André 🥶
- Paulo Henrique 👨‍🦳

## Atualização ✨

Versão 1.1v - 30/05/23

## Problemática ❌🚭

Todo projeto tem que partir de um problema para que a solução seja encontrada. Nossa problemática se estabelece da nossa relação com a disciplina de "Práticas Básicas de Laboratório", onde precisávamos calcular a absorbância de uma substância desconhecida a partir de uma série de substâncias que nós preparamos. A dificuldade principal veio da necessidade de realizar cálculos matemáticos para tirar uma média das substâncias conhecidas e criar uma reta de absorbância por concentração (mol/L) com o objetivo de descobrir a equação da reta para descobrir a substância desconhecida. Esse trabalho foi bem desgastante não pela parte química, mas sim por calcular esses valores. Além disso, quase o mesmo ocorre para a eletroforese, em que para se determinar o peso molecular de proteína são necessários diversos cálculos utilizando Ln e estimação de distâncias para comparar as moléculas pelo arraste.

## Objetivos 📈

Nosso objetivo principal, para o caso da espectroscopia, é criar um programa que vai computar esses dados matriciais, tirar a média da triplicata das amostras e plotar automaticamente uma reta, juntamente com a função da reta, para calcular quaisquer substâncias desconhecidas que precisem ser descobertas. Dessa forma, nosso trabalho vai agilizar, tornar mais simples e solucionar problemas tanto de cálculo quanto de descoberta de substâncias desconhecidas. Para a eletroforese, o projeto visa criar uma reta que pode ser aplicada posteriormente em qualquer outra proteína por meio da sua função matriz.

## Objetivos Específicos 🔱

- Programar um calculador de média. ✅
- Criar um código simples que vai receber quantas amostras foram produzidas e irá tirar a média delas e colocá-las em uma lista. ✅
- Realizar novas amostras no laboratório úmido para testar o código. 
- Ir para o laboratório e produzir mais amostras para calcular a concentração e a absorbância com o objetivo de calcular manualmente e usando o programa, verificando se ambos funcionam. 
- Programar o código que vai plotar as retas. ✅
- Fazer um código que consegue pegar o valor das listas do eixo X e Y e plotar um gráfico para realizar a equação da reta e o gráfico das amostras. ✅
- Adicionar uma forma de abrir uma imagem no programa (eletroforese). ✅
- Transformar as distâncias de pixel para centímetros (eletroforese).
- Subtração das medidas do branco no espectrofotômetro. 
- (Adicionais) Plotar automaticamente as áreas de interesse na imagem (eletroforese).
- (Adicionais) Criar uma ideia de tela para o programa. ✅
- (Adicionais) Pesquisar ou criar um código que cria um PDF em Python.


## Resumo do projeto 

O código apresentado é um programa em Python que utiliza a biblioteca Tkinter para criar uma interface gráfica com o usuário. O programa possui três classes: EletroScreen, SpectroScreen e StartScreen.

A classe EletroScreen é responsável por criar uma tela de eletroforese. A função generate_graph_eletro plota um gráfico com base nos valores de coordenadas e kDa fornecidos. O usuário pode selecionar uma imagem, escolher pontos de interesse na imagem e o programa irá exibir o gráfico correspondente.

A classe SpectroScreen cria uma tela para um espectrofotômetro. A função generate_graph plota um gráfico de absorbância em função da concentração com base nos valores fornecidos pelo usuário. O usuário pode digitar valores de absorbância e concentração em células correspondentes e o programa calculará a média das absorbâncias e plotará o gráfico.

A classe StartScreen é responsável pela tela inicial do programa. Ela exibe uma imagem de logo e possui dois botões para acessar as telas de eletroforese e espectrofotômetro.

O programa começa na tela de entrada, onde o usuário pode escolher entre eletroforese e espectrofotômetro. A partir da escolha, a respectiva classe é instanciada e a tela correspondente é exibida.

Nosso objetivo técnico é reduzir o tempo e o trabalho que cientistas que usam esses dois aparelhos tem ao usar essas máquinas. Atualmente, eles tem que fazer os cálculos e plotar os gráficos tudo usando o excel.

Então no presente momento, ja concluimos 99% do projeto e a única coisa que falta é adicionar uma forma de converter as distâncias das proteínas, na etapa de eletroforese, de pixel para cm.
