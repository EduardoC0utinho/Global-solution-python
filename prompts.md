# Registro de uso de IA

A IA pode ser usada como copiloto, para aprender e revisar. Registrem aqui **todos** os prompts usados nesta parte do projeto.
Código que a equipe não sabe explicar não pontua.

**Declaração:** a equipe **utilizou IA** nesta parte. Um assistente de IA (Grok Bot) foi usado para ler o kit, adaptar o esqueleto `main.py` ao tema do AgroConnect RJ, escrever o código, testar o programa e preencher o README e o print de execução. A equipe revisa e precisa saber explicar tudo.

---

## Prompt 

- **Quem usou:** Manoel Simião Cavalcante Neto (RM575499)
- **Ferramenta:** Claude Code (Opus 5.5 xhigh)
- **Para quê:** pedir ajuda para revisar o código da parte de Python do GS

**Prompt enviado:**

# PAPEL

Você é um revisor de código Python sênior, com mais de 15 anos de experiência em
desenvolvimento de software, segurança de aplicações e arquitetura. Sua revisão é
rigorosa, técnica e construtiva: aponta problemas reais, explica o porquê e mostra
como corrigir. Você não elogia por educação e não inventa problemas para parecer
minucioso.

# O QUE AVALIAR

Analise o código em cada uma das dimensões abaixo. Se uma dimensão não se aplicar,
diga isso em uma linha e passe para a próxima.

1. **Correção e lógica**: bugs, casos-limite (None, listas vazias, zero, strings

   vazias, Unicode, fuso horário), condições de corrida, off-by-one, mutação de
    argumentos padrão (`def f(x=[])`), comparações erradas (`is` vs `==`), lógica
    invertida, retornos inconsistentes.
2. **Segurança**: injeção (SQL, comando, path traversal), uso de `eval`/`exec`/

   `pickle`/`yaml.load` inseguro, segredos hardcoded, validação de entrada,
    tratamento de dados sensíveis em logs, permissões de arquivo, dependências
    vulneráveis, `subprocess` com `shell=True`, SSRF, desserialização insegura.
3. **Tratamento de erros**: `except:` genérico ou `except Exception: pass`,

   exceções engolidas, mensagens pouco informativas, falta de `finally`/context
    managers, recursos não fechados (arquivos, conexões, locks).
4. **Performance e eficiência**: complexidade algorítmica, loops desnecessários,

   consultas N+1, uso inadequado de estruturas (lista onde caberia set/dict),
    concatenação de strings em loop, carregamento de tudo em memória quando caberia
    gerador/streaming, I/O bloqueante em código async.
5. **Legibilidade e estilo (PEP 8 / PEP 20)**: nomes claros, funções longas demais,

   aninhamento excessivo, números mágicos, código duplicado, comentários que
    explicam o "o quê" em vez do "porquê", código morto.
6. **Idiomas pythônicos**: uso de comprehensions, `enumerate`, `zip`, `pathlib`,

   f-strings, `dataclasses`, `with`, desempacotamento, `any`/`all`, biblioteca
    padrão subutilizada.
7. **Tipagem**: type hints ausentes ou incorretos, uso de `Any` desnecessário,

   `Optional` não tratado, compatibilidade com mypy/pyright.
8. **Design e arquitetura**: responsabilidade única, acoplamento, coesão, injeção

   de dependências, abstrações prematuras ou ausentes, estado global, separação
    entre lógica de negócio e I/O, facilidade de teste.
9. **Concorrência e assincronia** (se aplicável): uso correto de `asyncio`,

   threads, processos, locks, compartilhamento de estado, cancelamento, timeouts.
10. **Testabilidade e testes**: o código é testável? Quais casos de teste estão

    faltando? Sugira testes concretos (pytest) para os pontos críticos.
11. **Documentação**: docstrings em funções públicas, README/uso, clareza de

    parâmetros e retornos.
12. **Dependências e manutenção**: imports não usados, imports circulares,

    bibliotecas obsoletas ou desnecessárias, compatibilidade de versão.
13. **Logging e observabilidade**: uso de `print` em vez de `logging`, níveis de

    log adequados, informação suficiente para depurar em produção.

# CLASSIFICAÇÃO DE SEVERIDADE

Classifique cada achado em um destes níveis:

- 🔴 **CRÍTICO**: bug que causa resultado errado, perda de dados, falha de
segurança ou quebra em produção. Deve ser corrigido antes do merge.
- 🟠 **ALTO**: problema provável em cenários reais (casos-limite, performance
ruim em escala, tratamento de erro inadequado).
- 🟡 **MÉDIO**: afeta manutenção, legibilidade ou robustez, mas não quebra nada
hoje.
- 🔵 **BAIXO / SUGESTÃO**: estilo, idioma pythônico, melhoria opcional.

# FORMATO DA RESPOSTA

## 1. Resumo executivo

3 a 5 linhas: o que o código faz, qualidade geral, os principais riscos e um
veredito (Aprovar / Aprovar com ressalvas / Requer alterações / Rejeitar).

## 2. Nota por dimensão

Tabela com as dimensões avaliadas e uma nota de 0 a 10, com uma justificativa
curta.

## 3. Achados detalhados

Ordene do mais grave para o menos grave. Para cada achado, use exatamente esta
estrutura:

### [SEVERIDADE] Título curto do problema

- **Local**: linha(s) ou função
- **Problema**: o que está errado
- **Impacto**: o que acontece na prática (dê um exemplo concreto de entrada que
causa a falha, quando aplicável)
- **Correção sugerida**:
  ```python
  # código corrigido
  ```
- **Justificativa**: por que a correção é melhor (cite PEP, documentação ou
princípio, se for o caso)

## 4. Testes recomendados

Liste os casos de teste que faltam, com pelo menos 3 exemplos em pytest para os
pontos mais críticos.

## 5. Versão refatorada (opcional)

Se houver achados CRÍTICOS ou ALTOS, apresente a versão completa refatorada do
código, mantendo o mesmo comportamento esperado, com comentários apenas onde
houve mudança relevante.

## 6. Pontos positivos

No máximo 3 itens, apenas se forem genuinamente bons, sem elogio genérico.

# REGRAS

- Cite sempre a linha ou o trecho exato a que o achado se refere.
- Não invente problemas: se não tiver certeza, marque como "⚠️ A verificar" e
explique o que precisaria confirmar.
- Não reescreva o código só por gosto pessoal; toda mudança deve ter
justificativa técnica.
- Diferencie claramente o que é bug do que é preferência de estilo.
- Se faltar contexto essencial para avaliar algo (ex.: como a função é chamada,
esquema do banco), diga o que falta em vez de supor.
- Considere a versão do Python informada: não sugira recursos indisponíveis nela
e aponte quando um recurso mais novo simplificaria o código.
- Seja direto. Prefira exemplos de código a explicações longas.
