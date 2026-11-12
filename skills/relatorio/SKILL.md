---
name: relatorio
description: Relatório executivo do nao-reinventar-roda. Lê os arquivos de uma ou mais ideias e gera uma one page em HTML para C-level, com a ideia, o veredito, o termômetro de espaço de mercado, os motivos, quem já faz, os casos do setor, quem usa e a recomendação. Não busca nada novo. Use depois da fase 3, ou depois da fase 1 como prévia.
argument-hint: <nome-da-pasta> [<outra-pasta> ...]
disable-model-invocation: true
---

# Relatório executivo (one page)

Leia primeiro `${CLAUDE_PLUGIN_ROOT}/referencia/regras.md`, a seção `05-relatorio.html` de `${CLAUDE_PLUGIN_ROOT}/referencia/modelos.md` e o modelo `${CLAUDE_PLUGIN_ROOT}/referencia/relatorio-modelo.html`.

Pastas: $ARGUMENTS

## Passos

1. **Localizar e travar.** Resolva cada pasta (seção 1 das regras). Até 3 pastas por relatório. Cada uma precisa de `00-ideia.md` e `01-ideias-e-demanda.md`; faltando, pare com a mensagem da seção 2 das regras. Escreva o caminho absoluto de cada pasta na primeira resposta.
2. **Modo.** Se todas as pastas têm `03-veredito.md`, o modo é **final**. Se alguma não tem, o modo é **prévia**: avise o usuário uma vez e marque a página com o selo "Prévia". Avise também sobre entrada `parcial` ou com mais de 30 dias.
3. **Juntar o conteúdo.** Leia `00`, `01`, `02` e `03` de cada pasta e preencha as seções da tabela abaixo. Não busque na web. Não acrescente fato que não esteja nesses arquivos. Fato da memória não entra.
4. **Calcular a temperatura** de cada ideia pela regra de "Temperatura" abaixo. Mostre no rodapé a conta usada.
5. **Escrever a página** a partir do modelo HTML. Troque cada `{{marcador}}` e apague os comentários de instrução. Mantenha os tokens de cor, a grade, os dois temas e o rodapé.
6. **Gravar** em `./pesquisa-ideia/<primeira-pasta>/05-relatorio.html`. Se já existir, renomeie o antigo para `05-relatorio.<AAAA-MM-DD>.html` antes.
7. **Publicar, se der.** Se a sessão tiver ferramenta de publicar página (por exemplo, Artifact), publique o arquivo gravado e devolva o link. Sem ela, devolva só o caminho.
8. **Encerrar.** Responda com: caminho, link (se houver), modo, a temperatura de cada ideia com a faixa, os três motivos em uma linha cada, e o que ficou de fora da página por falta de dado.

## Conteúdo da página

| Seção | De onde vem | Regra |
| --- | --- | --- |
| Título | `03` Resultado | O veredito em uma frase, com o nome da ideia. Ex.: "Ferramenta X: não é viável como produto". Em prévia, use a faixa da temperatura. |
| A ideia | `00` | Enunciado e capacidades em um parágrafo de até 60 palavras, sem jargão. |
| Pesquisa realizada | Cobertura de `01` e `02` | Totais de buscas, páginas lidas, empresas e projetos avaliados, produtos lidos a fundo. Somar das tabelas; não arredondar para cima. |
| Veredito e termômetro | `03` e a regra de temperatura | Rótulo da faixa, medidor com uma agulha por ideia, uma linha por ideia com a nota. |
| Três motivos | `03` "O caso mais forte contra" e "Prós e contras" | Exatamente três. Título curto e duas frases cada. Se o resultado é seguir, os motivos são a favor. |
| Quem já faz | `02` Lista curta e Lista longa | Até 10 linhas: empresa, o que entrega, modelo (preço ou licença, nunca os dois numa célula). Selo "brasileira" ou do mercado de `00` quando a fonte disser. |
| Casos do setor | `01` Sinais contrários e Ideias parecidas sem produto | Linha do tempo por ano: compras, encerramentos, lançamentos de gigantes. Só o que tem data. |
| Quem usa e como resolve | `01` Sinais de demanda | Organizações e pessoas nomeadas nos sinais. Nunca invente cliente de fornecedor. Sem nomes, escreva "não encontrado nas buscas". |
| Recomendação | `03` "O que incluir" e "Comentário do agente principal" | Três colunas: não fazer, fazer (se houver alternativa), única peça própria (se houver). Sem alternativa, escreva "nenhuma encontrada". |
| Rodapé | Cabeçalhos dos arquivos | Pastas e datas, modo, situação de cada fase, conta da temperatura, o que não foi avaliado (custo, técnica, legal) e as estimativas sem fonte. |

Cada linha de "Quem já faz", "Casos" e "Quem usa" leva o identificador de origem em letra pequena (`02:F10`, `01:N5`). É assim que o leitor executivo pode pedir a fonte.

## Temperatura

Escala de 0 a 100: quanto espaço livre sobra para a ideia como produto. 0 é "já existe"; 100 é "lacuna aberta com demanda".

Conta, por ideia, com as capacidades C de `00`:

- `N` = número de capacidades C.
- `D` = capacidades C classificadas como "diferencial" na matriz de `03`.
- `R` = capacidades C classificadas como "diferencial em risco".
- `S` = capacidades C "sem classificação" (não encontradas em produto, sem demanda).
- Base = `100 × (D + 0,5·R + 0,25·S) / N`, arredondada.

Depois aplique o teto ou o piso do resultado de `03`:

| Resultado de `03` | Ajuste |
| --- | --- |
| `não seguir: use X` | teto 20 |
| `não seguir` | teto 30 |
| `inconclusivo` | teto 49 |
| `seguir com mudanças` | piso 50, teto 74 |
| `seguir` | piso 65 |

No modo prévia, sem `03`, estime a classificação de cada C a partir de `02` (presente em algum produto = não conta; ausente e com sinal em `01` = D; ausente sem sinal = S), aplique teto 49 e escreva "estimativa" ao lado do número.

Faixas e rótulos:

| Temperatura | Rótulo |
| --- | --- |
| 0 a 34 | Não construir: já existe |
| 35 a 49 | Não construir como produto |
| 50 a 64 | Construir com mudanças |
| 65 a 100 | Construir |

## Medidor

Semicírculo com centro (120, 120) e raio 100 no `viewBox="0 0 240 140"`. Para uma temperatura `t`:

- ângulo `θ = 180 − 1,8·t` graus;
- ponta da agulha principal: `(120 + 90·cos θ, 120 − 90·sin θ)`; agulhas secundárias usam 80;
- rótulo da agulha: a 62 do centro no mesmo ângulo, deslocado 8 para a direita; se duas notas diferirem menos de 10, use 50 e 70 de distância.

Confira as coordenadas com a conta antes de gravar. A agulha da ideia principal (primeira pasta) é a mais escura.

## Escrita

- Português do Brasil, frases curtas, sem jargão sem explicação. Siglas na primeira vez: "análise estática de segurança (SAST)".
- Uma página: tudo cabe numa tela larga com rolagem curta. Nada de seção extra.
- Números com fonte; estimativa sem fonte só no rodapé, marcada como estimativa.
- Não diga "viável" ou "inviável" em sentido técnico ou financeiro: o rodapé diz que custo, técnica e questões legais não foram avaliados. "Não é viável como produto" fala de espaço de mercado e pode ser usado quando a faixa for 0 a 49.

## Não faça

- Não busque na web nem abra páginas.
- Não mude o resultado do juiz de `03`.
- Não use selos de "conferido" na página; a condição de cada fato fica nos arquivos de origem.
