"""há vários exemplos de como usar o csv e o Pandas"""
#Using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


#Using csv library
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
'''O que está acontecendo aqui é que estou abrindo um arquivo csv(excel, libreofficecalc)
 através de uma biblioteca própria, que é a csv, depois o for loop serve para printar cada elemento que virá, separado assim ['day', 'temp', 'condition']. A vantagem é que o método reader, acima comentado, vai vir sem formatação. Depois, o print foi substituído pelo código que pega a temperatura na posição 01, desde que seja um número, e acrescenta ao dicionário vazio temperatures, transformando-o em um int.
   No entanto, esses códigos todos são trabalhosos para se trabalhar com tabelas, para o que utilizaremos
   o Panda. O Panda é uma biblioteca nativa própria para trabalhar com dados em formato de tabela'. Uma dica é sempre imprimir o tipo da variável, o data type, assim, na documentação, pode constar como trabalhar com ela.
   No pandas, uma tabela é um data frame, enquanto uma coluna é uma série. Esses são os dois tipos primários no  Panda. Por padrão, o Panda vai relacionar o nome da primeira fileira como o nome da coluna'''


# Using the pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

'''o método mean serve para calcular a média, nesse caso, ele pegou as informações
 na coluna temp e já fez o cálculo, o que poupa todo o código, já o método max, 
 retorna o maior valor, esses são os dois métodos para printar o condition 
 imprimem a coluna, eles fazem a mesma coisa. Atentar se o nome está exatamente
  igual ao do arquivo.'''


#Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

'''esse método verifica se na coluna day tem a palavra Monday'''
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


#Central Park Squirrel Data Analysis

'''o objetivo desse código é ler as informações em uma tabela e criar outra tabela com os dados extraídos.
Primeiro é atribuido à variável data o comando para ler o arquivo 2018_Centra... que está em.csv, depois,
 para cada variável a linha de comando determina -> vai obter os dados da coluna ["Primary Fur Color"]
  comparando-os com a palavra que se está buscando -> depois, cria-se uma lista, por isso (), com essa informação
   -> obtem-se a quantidade de itens na lista através do comando len e é esse resultado que é passado para cada
   variável. Mais abaixo, cria-se um dicionário com os 3 itens em uma sequência correspondente e abaixo
   são os comandos do pandas para tratar o dicionário como um DataFrame(uma tabela), depois o comando transforma
   a variável para CSV. '''

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")







