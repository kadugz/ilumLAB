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

## Como utilizar?

Manual de Instruções
(Se quiser entender melhor abra o PDF dentro da pasta do projeto)

Aqui você pode escolher entre utilizar o Espectrofotômetro ou a Eletroforese, vamos começar pela Eletroforese.

1 – Eletroforese

Ao clicar em Eletroforese, uma tela com o botão de abrir imagem e um para montar o gráfico. Ao clicar no botão de abrir imagem, você deve procurar no seu explorador de arquivos que será aberto pela pasta, exemplos e lá você deve abrir a imagem exemplo_eletroforese.

Após abrir a imagem você verá uma tela que tem sua imagem e onde você deve selecionar com o mouse e o botão esquerdo 11 pontos do seu exemplo.

Os pontos são o da primeira coluna intitulada de M, onde de cima para baixo(começando em 260 kDa) a escala vai diminuindo e você deve selecionar de cima para baixo os pontos.

Após isso clique em Montar gráfico e seja feliz!

2 - Espectrofotômetro

Ao clicar em Espectrofotômetro uma tela nada sujestiva irá abrir, ela constara uma tabela com linhas de A até H e colunas de 1 até 12.

Nela você deve inserir em cada coluna sua amostra que deseja utilizar, na pasta "exemplos" há um "exemplo" de como se preencher essa tabela, novamente para maior explicação abra o manual.

Após preencher clique em calcular médias para calcular as medias das suas substâncias com mesma concentração e depois clique em montar gráfico de absorbãncia por concentração.

Com isso você consegue montar seu gráfico + reta de regressão.
