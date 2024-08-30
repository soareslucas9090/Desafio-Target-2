import json


def q1_pseudocodigo() -> int:
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    return soma


def q2_fibonacci(n: int) -> bool:
    # É o mesmo código que passei na resposta da vaga para Ribeirão Preto
    fib = [0, 1]

    aux = 0

    while aux < n:
        aux = fib[-1] + fib[-2]
        fib.append(aux)

    return n in fib


def q3_faturamento(vetor: list[float]) -> dict:
    # Estou excluindo todos os valores 0 do vetor, para não interferir no calculo
    # da média e do menor valor
    new_vetor = [x for x in vetor if x > 0]
    new_vetor.sort()

    menor_valor = new_vetor[0]
    maior_valor = new_vetor[len(new_vetor) - 1]
    media = sum(new_vetor) / len(new_vetor)
    num_dias = [x for x in new_vetor if x > media and x > 0]

    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "num_dias_maior_que_media": len(num_dias),
    }


def q4_percentual(faturamento: dict) -> dict:
    total = sum(faturamento.values())
    sp = (faturamento["sp"] * 100) / total
    rj = (faturamento["rj"] * 100) / total
    mg = (faturamento["mg"] * 100) / total
    es = (faturamento["es"] * 100) / total
    outros = (faturamento["outros"] * 100) / total

    resultado = {"sp": sp, "rj": rj, "mg": mg, "es": es, "outros": outros}

    return resultado


def q5_reverse(str: str) -> str:
    inversa = ""

    for i in range(len(str) - 1, -1, -1):
        inversa += str[i]

    return inversa


###### q1 ######

print("Executando o código da função 1...\n")

print(f"A soma dada no pseudo código é {q1_pseudocodigo()}")


###### q2 ######
print("Executando o código da função 2...\n")
n = input("Digite o número que você deseja verificar se está em fibonacci: ")

if q2_fibonacci(int(n)):
    print(f"\nO número {n} está em fibonacci\n")
else:
    print(f"\nO número {n} não está em fibonacci\n")


###### q3 ######
print("Executando o código da função 3...\n")
print("Lendo arquivo json...\n")
with open("json.json") as arquivo:
    dados = json.load(arquivo)

result = q3_faturamento(dados["faturamento_por_dia"])
print(
    f"""Menor valor: {result["menor_valor"]}\n
Maior valor: {result["maior_valor"]}\n
Número de dias do mês com faturamento maior que a média: {result["num_dias_maior_que_media"]}\n"""
)

###### q4 ######
print("Executando o código da função 4...\n")
valores = {
    "sp": 67836.43,
    "rj": 36678.66,
    "mg": 29229.88,
    "es": 27165.48,
    "outros": 19849.53,
}
result = q4_percentual(valores)
print(
    f"""Os percentuais de faturamento de cada estado é:
      SP: {result["sp"]}
      RJ: {result["rj"]}
      MG: {result["mg"]}
      ES: {result["es"]}
      Outros: {result["outros"]}\n"""
)

###### q5 ######

print("Executando o código da função 5...\n")
str = input("Digite a string que deseja inverter: ")

print(f"\nString invertida: {q5_reverse(str)}")
