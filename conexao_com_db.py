#Bibliotecas:
#mysql-connector-python
import mysql.connector


#Variáveis
mydb = mysql.connector.connect(host="localhost", user="root")

cursor = mydb.cursor()

bd = None
#Funções
def oque_vc_quer_rappa():
  lista = [""]
  a = input("")
  lista[0]
def create_database(nome):
  cursor.execute("CREATE DATABASE IF NOT EXISTS {nome}")
  return "USE {nome};"
#Início do código:

print(mydb)


while True:
  oque_vc_quer_rappa()
  