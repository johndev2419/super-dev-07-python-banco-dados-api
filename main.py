from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/greetings")
def saudacoes():
    return {"mensagem": "hello world"}


#query param 
#/calculadora?numero1=10&numero2=10
@app.get("/calculadora")
def calculadora(numero1:int, numero2: int):
    soma = numero1 + numero2
    return{"resultado": soma}


#query vai depois da ? ex: /calculadora/expert?operacao=soma&n1=100&n2=200

@app.get("/calculadora/expert")
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair"]:
        return HTTPException(
            status_code=400,
            detail="Operação invalída. Opções disponiveis [somar/subtrair]"
        )




    if operacao == "somar":
        resultado = n1 + n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }


# Criar um endpoint 'pessoa/nome-completo' para concatenar o nome da pessoa
#   Receber dois query params: nome e sobrenome
#   Retornar no seguinte formato {"nomeCompleto": "John Doe"}
# Criar um endpoint 'pessoa/calcular-ano-nascimento' para calcular o ano de nascimento
#   Query param: idade
#   Calcular o ano de nascimento
#   Retornar {"anoNascimento": 1991}
# Criar um endpoint 'pessoa/imc' para calcular o imc da pessoa
#   Query param: altura, peso
#   Calcular o imc
#   Retornar {"imc": 20.29}
# Alterar o endpoint 'pessoa/imc' para retornar o status do imc
#   Descobrir o status do IMC
#   Retornar {"imc"': 20.29, "Obesidade III"}




# fastapi dev main.py

# 127.0.0.1:8000/docs
# 127.0.0.1:8000/greetings



@app.get("/pessoa/nome-completo")
def nome_comppleto(nome: str, sobrenome: str):
    nome_comppleto = nome + sobrenome
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "nome completo": nome_comppleto
        }


@app.get("/pessoa/calcular-ano-nascimento")
def calcular_ano_nascimento (idade: int):
    ano_atual = 2025
    ano_de_nascimento = ano_atual - idade
    return{
        "idade" : idade,
        "ano de nascimento": ano_de_nascimento
    }   