---
name: 2-existentes
description: Fase 2 do nao-reinventar-roda. Levanta produtos e soluções que já existem ou estão em andamento (comerciais, gratuitos, código aberto, financiamento coletivo) e lê fabricante, documentação e datasheet da lista curta. Use depois da fase 1.
argument-hint: <nome-da-pasta-da-ideia>
disable-model-invocation: true
---

# Fase 2: produtos e soluções existentes

Leia primeiro `${CLAUDE_PLUGIN_ROOT}/referencia/regras.md` e `${CLAUDE_PLUGIN_ROOT}/referencia/modelos.md`. As regras de lá valem aqui e não são repetidas.

Ideia: $ARGUMENTS

## Passos

1. **Localizar e travar.** Resolva a pasta e confira `00-ideia.md` e `01-ideias-e-demanda.md` pela seção 2 das regras. Faltando, pare com a mensagem de lá; o comando a indicar é `/nao-reinventar-roda:1-demanda <a ideia em uma frase>`.
2. **Plano.** Faça a busca de teste. Anuncie o plano. Parta de "Candidatos vistos de passagem" de `01`. Frentes padrão:
   - **Prontos:** produtos comerciais e gratuitos.
   - **Abertos e em andamento:** código aberto, financiamento coletivo, anúncios, abandonados.

   Com 4 pesquisadores, separe: comerciais; código aberto; em andamento e financiamento coletivo; descontinuados e abandonados.
3. **Lista longa.** Lance os pesquisadores pedindo só candidatos, sem abrir páginas de detalhe. Junte, remova repetidos e mostre a lista longa ao usuário, com no máximo 12 linhas e a categoria de cada uma. Tudo aqui é "não conferido (trecho de busca)".
4. **Saída antecipada.** Se algum candidato parece cobrir a ideia inteira, diga qual e pergunte se o usuário quer continuar.
5. **Lista curta.** Peça ao usuário que escolha de 3 a 5. Sugira os seus, com uma linha de motivo, mas espere a escolha.
6. **Leitura da lista curta.** Lance pesquisadores só para a lista curta, com as fontes do tipo da ideia (seção 10 das regras). Para cada produto, o mínimo a conferir é: responsável, página principal, situação, e preço ou licença. Para cada capacidade de `00`, se o produto tem ou não, com fonte.
7. **Documentos.** Datasheet e manual: tente abrir pela URL. Leia o sumário e só as seções dos atributos da matriz. Registre página ou seção em cada linha. Se não abrir, registre o link e a condição "não conferido (bloqueado)"; não baixe o arquivo.
8. **Montar `02-produtos-existentes.md`** pelo modelo. Em "Capacidades por produto", inclua também o que os produtos têm e a ideia não (X1, X2...). Em "Em andamento", registre a data prometida de entrega e a data da última atividade.
9. **Encerrar.** Grave o arquivo e responda com: caminho, situação, contagens, produtos da lista curta que ficaram abaixo do mínimo conferido, e o comando da fase 3:

   `/nao-reinventar-roda:3-veredito <nome-da-pasta>`

## Não faça

- Não compare a ideia com os produtos nem diga qual é melhor. Isso é da fase 3.
- Não registre licença e preço na mesma coluna: "gratuito" e "código aberto" são coisas diferentes.
- Não complete de memória o que a página não mostrou.
