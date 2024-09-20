import pyodbc
import os
from openpyxl import load_workbook
from datetime import datetime


# captura do arquivo config

dias = open('C:\\Program Files (x86)\\Averics\\Unity\\Limpeza_hbm\\config.txt', 'r', encoding="utf8")

def arquivo():
    teste = (dias.read())
    print('*************0'*3)
    print(teste)
    print('*************1'*3)
    print(teste.replace('\n','"',))
    nteste = teste.replace('\n','"',)

    print('****************************2')
    print(nteste.split('"'))
    ateste = nteste.split('"')
    print('****************************3')
    t = (ateste[0])
    p = (ateste[1])
    c = (ateste[2])

    tipo = t[14:]
    periodo = p[8:]
    caminho = c[8:]
    print('****************************4')
    print(tipo)
    print(periodo)
    print(caminho)

    dias.close()
    return tipo, periodo, caminho

def arquivo_transack():
    teste = (dias.read())
    print('*************0'*3)
    print(teste)
    print('*************1'*3)
    print(teste.replace('\n','"',))
    nteste = teste.replace('\n','"',)

    print('****************************2')
    print(nteste.split('"'))
    ateste = nteste.split('"')
    print('****************************3')
    t = (ateste[0])
    p = (ateste[1])
    c = (ateste[2])

    tipo = t[14:]
    periodo = p[8:]
    caminho = c[8:]
    print('****************************4')
    print(tipo)
    print(periodo)
    print(caminho)

    dias.close()
    return tipo, periodo, caminho

def Tipo():
    tipo = open('C:\\Program Files (x86)\\Averics\\Unity\\Limpeza_hbm\\config.txt', 'r', encoding="utf8")
    ttipo = tipo.read()
    ntipo = ttipo.replace('\n', '"', )
    atipo = ntipo.split('"')
    t = (atipo[0])
    tipo = t[14:]

    return tipo

def Periodo():
    peri = open('C:\\Program Files (x86)\\Averics\\Unity\\Limpeza_hbm\\config.txt', 'r', encoding="utf8")
    tper = (peri.read())
    nper = tper.replace('\n', '"', )
    aper = nper.split('"')
    p = (aper[1])
    per = p[8:]

    return per

def Arquivos():
    cami = open('C:\\Program Files (x86)\\Averics\\Unity\\Limpeza_hbm\\config.txt', 'r', encoding="utf8")
    tcam = (cami.read())
    ncam = tcam.replace('\n', '"', )
    acam = ncam.split('"')
    c = (acam[2])
    cam = c[16:]
    return cam


# ------------
nome = 'AUDIT_SESSION_'
nome1 = "TRANSACK_"
tipo = Tipo()
print(tipo)
# linhas = dias.readline()
# dias.close()
caminho = 'C:\\Program Files (x86)\\Averics\\Unity\\Limpeza_hbm\\logs\\'
arquivos = Arquivos()
print(arquivos)
hora = nome + (datetime.today().strftime('%d-%m-%Y %H.%M')) + f'.{tipo}'
hora1 = nome1 + (datetime.today().strftime('%d-%m-%Y %H.%M')) + f'.{tipo}'
print(hora)
print(hora1)
linhas = Periodo()
print(linhas)



Driver = 'ODBC Driver 11 for SQL Server'
Driver1 = 'SQL Server Native Client 11.0'
Driver2 = 'ODBC Driver 17 for SQL Server'
Server = '.\\AVSQLSRV'
Database = 'HID_BIOMANAGER'
UID = 'sa'
PWD = 'Sh@ll0w15y'



conexao = pyodbc.connect(Driver=Driver2, Server=Server, Database=Database, UID=UID, PWD=PWD)
print("Conexao Bem Sucedida")
print(f'periodo menor que {linhas} dias a serem apagados')
cursor = conexao.cursor()
arquivoTexto = open(caminho + hora, "a", encoding="utf8")
arquivotexto1 = open(caminho + hora1, "a", encoding="utf8")

cursor.execute(f"select * from AUDIT_SESSION where cast(AS_DATETIMELOCAL as date) < DATEADD(day, DATEDIFF(day, 0, GETDATE()), -{linhas})")

for i in cursor:
    print(i)
    arquivoTexto.write(str(i))
    arquivoTexto.write('\n')

arquivoTexto.close()
cursor.commit()

cursor.execute(f"delete from AUDIT_SESSION where cast(AS_DATETIMELOCAL as date) < DATEADD(day, DATEDIFF(day, 0, GETDATE()), -{linhas})")

cursor.commit()

# TERMINO DO PROCEDIMENTO DE EXCLUSÃO DAS LINHAS AUDIT_SESSION

cursor.execute(f"select * from TRANSACK where cast(TR_DATETIMELOCAL as date) < DATEADD(day, DATEDIFF(day, 0, GETDATE()), -{linhas})")

for i in cursor:
    print(i)
    arquivotexto1.write(str(i))
    arquivotexto1.write('\n')

arquivotexto1.close()

cursor.commit()

cursor.execute(f"delete from TRANSACK where cast(TR_DATETIMELOCAL as date) < DATEADD(day, DATEDIFF(day, 0, GETDATE()), -{linhas})")

cursor.commit()
# TERMINO DO PROCEDIMENTO DE EXCLUSÃO DAS LINHAS TRANSACK

cursor.close()
ccaminho = caminho.rstrip('\\')
print(ccaminho)
print(arquivos)

os.system(f'ForFiles /p "{ccaminho}" /s /d -{arquivos} /c "cmd /c del @file"')
print("FIM")

