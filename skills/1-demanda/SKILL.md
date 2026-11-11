---
name: 1-demanda
description: Fase 1 do nao-reinventar-roda. Registra a ideia em 00-ideia.md e pesquisa ideias parecidas e sinais de que alguém precisa dela. Use quando o usuário tem uma ideia nova e quer saber se há demanda.
argument-hint: <a ideia em uma frase>
disable-model-invocation: true
---

# Fase 1: ideias parecidas e demanda

Leia primeiro `${CLAUDE_PLUGIN_ROOT}/referencia/regras.md` e `${CLAUDE_PLUGIN_ROOT}/referencia/modelos.md`. As regras de lá valem aqui e não são repetidas.

Ideia recebida: $ARGUMENTS

## Passos

1. **Ideia.** Se não veio argumento, peça a ideia em uma frase e pare.
2. **Registrar.** Monte `00-ideia.md` pelo modelo: enunciado, tipo, público, finalidade, mercado e idioma, restrições, capacidades numeradas (C1, C2...) e o nome da pasta. Preencha o que a frase permite e pergunte só o que faltar, em uma única mensagem. Não invente capacidades.
3. **Confirmar.** Mostre o `00-ideia.md` e o caminho absoluto da pasta. Avise uma vez que os termos da ideia saem nas consultas de busca. Só grave e siga depois que o usuário confirmar.
4. **Plano.** Faça a busca de teste. Anuncie o plano. Frentes padrão, uma por pesquisador:
   - **Pedidos e improvisos:** gente pedindo, pagando ou improvisando a solução (fóruns, issues, perguntas e respostas, avaliações de produtos vizinhos).
   - **Contrários e parecidos:** ideias parecidas que não viraram produto, campanhas que fracassaram, produtos descontinuados, pedidos antigos sem resposta.
5. **Pesquisar.** Lance os pesquisadores em uma única mensagem, conforme a seção 6 das regras.
6. **Montar `01-ideias-e-demanda.md`.** Copie as linhas devolvidas para as seções do modelo e numere as fontes. Regra de corte: o que dá para comprar, baixar, usar ou apoiar não é analisado aqui; vai, só com nome e fonte, para "Candidatos vistos de passagem".
7. **Sinais contrários.** A seção é obrigatória. Vazia, escreva "nenhum encontrado" e aponte as consultas.
8. **Encerrar.** Grave o arquivo e responda com: caminho, situação, contagens, os três sinais mais fortes a favor e os três contra, e o comando da fase 2:

   `/nao-reinventar-roda:2-existentes <nome-da-pasta>`

## Não faça

- Não estime tamanho de mercado.
- Não diga se a ideia é boa. Isso é da fase 3.
- Não descreva produtos em detalhe. Isso é da fase 2.
