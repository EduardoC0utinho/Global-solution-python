# ============================================================
#  GS CitizenTech · Computational Thinking with Python
#  Atividade: O Cérebro da CitizenTech
#
#  Equipe: Manoel Simião Cavalcante Neto - RM575499,
#          Eric Sia Mapurunga de Aguiar - RM576304,
#          Eduardo Coutinho de Lima - RM575349
#  CitizenTech: AgroConnect RJ
#  Problema, em uma frase: o alimento fresco do pequeno produtor
#  estraga no caminho do campo até a cidade quando a temperatura
#  da caixa de transporte passa do ponto, e ninguém avisa.
#  (Confira se esta frase é igual à da Ficha da CitizenTech.)
# ============================================================
#
#  Como a ideia funciona (o caminho do dado):
#    o sensor mede a temperatura da caixa -> o Python decide a faixa
#    -> o aviso aparece para o produtor e para quem vai comprar.
#
#  Partes do programa:
#    PARTE 1 - Dados       (lista com 12 registros simulados)
#    PARTE 2 - Faixas      (limites e avisos)
#    PARTE 3 - Menu        (loop que só termina no Sair)
#    PARTE 4 - Opções      (classificar, resumir, consultar, adicionar)
# ============================================================


# ------------------------------------------------------------
# PARTE 1 - DADOS
# Cada registro simula uma leitura do sensor de temperatura
# colocado dentro da caixa de verduras e frutas durante a entrega
# (Nova Friburgo -> Rio de Janeiro). Os valores são SIMULADOS
# pela equipe: não são medições reais e não têm dados pessoais.
# Cada registro é um dicionário com a hora e a temperatura.
# ------------------------------------------------------------

nome_local = "Sítio Boa Colheita (Nova Friburgo) -> Rio de Janeiro"
grandeza = "Temperatura da caixa de transporte"
unidade = "°C"

leituras = [
    {"hora": "06:00", "valor": 6.5},
    {"hora": "06:30", "valor": 7.2},
    {"hora": "07:00", "valor": 8.9},
    {"hora": "07:30", "valor": 9.8},
    {"hora": "08:00", "valor": 10.6},
    {"hora": "08:30", "valor": 12.4},
    {"hora": "09:00", "valor": 14.1},
    {"hora": "09:30", "valor": 15.8},
    {"hora": "10:00", "valor": 17.3},
    {"hora": "10:30", "valor": 13.7},
    {"hora": "11:00", "valor": 9.4},
    {"hora": "11:30", "valor": 7.1},
]


# ------------------------------------------------------------
# PARTE 2 - FAIXAS DE DECISÃO
# Limites definidos pela equipe para frutas e verduras frescas
# (referência simples: até 10 °C o alimento se conserva bem).
# O circuito de Edge e a página usam os mesmos números e textos.
# ------------------------------------------------------------

limite_atencao = 10.0   # a partir daqui: ATENÇÃO
limite_perigo = 15.0    # a partir daqui: PERIGO

aviso_normal = "Alimento bem conservado. Pode comprar e consumir com tranquilidade."
aviso_atencao = "Caixa esquentando. Priorize consumir logo e mantenha na geladeira."
aviso_perigo = "Risco de estragar. Não compre este lote e avise o produtor."


# Função que recebe uma temperatura e devolve a faixa e o aviso.
# Assim a regra if/elif/else fica escrita em um só lugar.
def classificar(valor):
    if valor >= limite_perigo:
        faixa = "PERIGO"
        aviso = aviso_perigo
    elif valor >= limite_atencao:
        faixa = "ATENÇÃO"
        aviso = aviso_atencao
    else:
        faixa = "NORMAL"
        aviso = aviso_normal
    return faixa, aviso


# ------------------------------------------------------------
# PARTE 3 - MENU
# O menu repete até o usuário escolher 0.
# Entrada inválida NUNCA pode derrubar o programa.
# ------------------------------------------------------------

print("=" * 52)
print("  Alerta AgroConnect RJ · Cadeia fria do alimento")
print(f"  Rota: {nome_local}")
print("=" * 52)

opcao = ""
while opcao != "0":
    print()
    print("1 - Ver todas as leituras classificadas")
    print("2 - Resumo da entrega")
    print("3 - Consultar uma leitura")
    print("4 - Registrar uma nova leitura")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    # --------------------------------------------------------
    # PARTE 4 - OPÇÕES
    # --------------------------------------------------------

    if opcao == "1":
        # Percorre a lista e classifica cada registro.
        print()
        print(f"{grandeza} ({unidade}):")
        for posicao in range(len(leituras)):
            registro = leituras[posicao]
            faixa, aviso = classificar(registro["valor"])
            print(f"  Leitura {posicao + 1:02d} · {registro['hora']}: "
                  f"{registro['valor']:.1f} {unidade} -> {faixa}")

    elif opcao == "2":
        # Resumo: média, maior valor e % de leituras em alerta
        # (alerta = ATENÇÃO ou PERIGO).
        soma = 0
        maior = leituras[0]["valor"]
        qtd_atencao = 0
        qtd_perigo = 0
        for registro in leituras:
            valor = registro["valor"]
            soma = soma + valor
            if valor > maior:
                maior = valor
            faixa, aviso = classificar(valor)
            if faixa == "ATENÇÃO":
                qtd_atencao = qtd_atencao + 1
            elif faixa == "PERIGO":
                qtd_perigo = qtd_perigo + 1

        total = len(leituras)
        media = soma / total
        qtd_alerta = qtd_atencao + qtd_perigo
        percentual_alerta = qtd_alerta / total * 100

        print()
        print(f"Média da entrega: {media:.1f} {unidade}")
        print(f"Maior valor: {maior:.1f} {unidade}")
        print(f"Leituras em alerta: {qtd_alerta} de {total} ({percentual_alerta:.0f}%)")
        print(f"  ATENÇÃO: {qtd_atencao} | PERIGO: {qtd_perigo}")

        # O aviso final usa a pior faixa que apareceu na entrega.
        if qtd_perigo > 0:
            print(f"AVISO: {aviso_perigo}")
        elif qtd_atencao > 0:
            print(f"AVISO: {aviso_atencao}")
        else:
            print(f"AVISO: {aviso_normal}")

    elif opcao == "3":
        # Consulta com validação: o programa insiste até receber um número válido.
        numero = input(f"Número da leitura (1 a {len(leituras)}): ").strip()
        while not numero.isdigit() or int(numero) < 1 or int(numero) > len(leituras):
            print("Valor inválido. Digite apenas o número da leitura.")
            numero = input(f"Número da leitura (1 a {len(leituras)}): ").strip()

        registro = leituras[int(numero) - 1]
        faixa, aviso = classificar(registro["valor"])
        print(f"Leitura {numero} · {registro['hora']}: {registro['valor']:.1f} {unidade}")
        print(f"Faixa: {faixa}")
        print(f"AVISO: {aviso}")

    elif opcao == "4":
        # Nova leitura: usa try/except para não quebrar com texto.
        hora = input("Hora da leitura (ex.: 12:00): ").strip()
        if hora == "":
            print("Hora vazia. Leitura não registrada.")
        else:
            texto = input(f"Temperatura em {unidade}: ").strip().replace(",", ".")
            try:
                valor = float(texto)
            except ValueError:
                print("Valor inválido. Digite um número, por exemplo 11.5")
            else:
                # Limite de bom senso para um sensor de caixa de transporte.
                if valor < -10 or valor > 60:
                    print("Temperatura fora do que o sensor mede (-10 a 60). Não registrada.")
                else:
                    leituras.append({"hora": hora, "valor": valor})
                    faixa, aviso = classificar(valor)
                    print(f"Leitura registrada: {valor:.1f} {unidade} -> {faixa}")
                    print(f"AVISO: {aviso}")

    elif opcao == "0":
        print("Até logo! Alimento bom é alimento bem cuidado.")

    else:
        print("Opção inválida. Escolha um número do menu.")
