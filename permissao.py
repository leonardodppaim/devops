import os
import stat
import datetime

def registro (email: str):
    if os.path.isfile("acesso.txt"):
        os.chmod("acesso.txt", stat.S_IRWXU)
        arquivo = open ("acesso.txt",'a')
    else:
        arquivo = open("acesso.txt", 'a+')

    hoje = datetime.datetime.now()
    hoje = hoje.strftime("%Y/%m/%d %H:%M:%S;")
    arquivo.write("\n"+email+" "+hoje)

    os.chmod("acesso.txt", stat.S_IRUSR)

    
def registronegado (email: str):
    if os.path.isfile("acesso.txt"):
        os.chmod("acesso.txt", stat.S_IRWXU)
        arquivo = open ("acesso.txt",'a')
    else:
        arquivo = open("acesso.txt", 'a+')

    hoje = datetime.datetime.now()
    hoje = hoje.strftime("%Y/%m/%d %H:%M:%S;")
    arquivo.write("\n"+"FALHA "+ email+" "+hoje)

    os.chmod("acesso.txt", stat.S_IRUSR)
