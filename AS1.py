#PUCPR - ADS
#Outubro 2022
#Segurança da Tecnologia da informação
#Leonardo Dalla Porta Paim

#Adaptado para AS1 DEV OPS Março 2023 

import pyrebase
from permissao import registro, registronegado
import email.mime.multipart 
import email.mime.text 



firebaseConfig = {
    "apiKey": "AIzaSyADUwsV3zvVjkMwFRXznkIgMIbf7mwbqu0",
    "authDomain": "pucpr-leopaim.firebaseapp.com",
    "projectId": "pucpr-leopaim",
    "storageBucket": "pucpr-leopaim.appspot.com",
    "messagingSenderId": "893950675030",
    "appId": "1:893950675030:web:4c4d0df3b67ac4624493f7",
    "measurementId": "G-PW9SQZHXQD",
    "databaseURL": "https://pucpr-leopaim-default-rtdb.firebaseio.com/"
}

while True:
    email=input("Digite seu email: ")
    senha=input("Digite sua senha: ")
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    status = auth.sign_in_with_email_and_password(email,senha)
    id_Token = status["idToken"]
    info = auth.get_account_info(id_Token)
    usuario = info["users"]
    status_Email = usuario[0]["emailVerified"]
    if status_Email:
        
        print ("Usuário Autenticado")
        registro (email)
        
    else:
        print ("Email não verificado")
        print ("Acesse seu email e confirme sua conta")
        registronegado (email)
        
